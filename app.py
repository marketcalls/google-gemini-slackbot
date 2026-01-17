from flask import Flask, request, jsonify
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
import threading
import pathlib
import textwrap
import os
import time
from dotenv import load_dotenv

import google.generativeai as genai
from threading import Thread, Lock

# --- Configuration & Globals ---
load_dotenv()

# Thread-safe duplicate handling
processed_ids_lock = Lock()
processed_ids = {}  # Format: {client_msg_id: timestamp}
DEDUPE_RETENTION_SECONDS = 600  # Keep IDs for 10 minutes

# Define Google API Key and Set Gemini Pro Model
google_api_key = os.getenv('GOOGLE_API_KEY')
genai.configure(api_key=google_api_key)
# Note: Ensure the model version is correct (e.g., 'gemini-1.5-flash' or 'gemini-pro')
model = genai.GenerativeModel('gemini-2.5-flash')

# Initialize a Web Client with the Slack bot token
slack_token = os.getenv('SLACK_BOT_TOKEN')
client = WebClient(token=slack_token)

# Get BOT_USER_ID
BOT_USER_ID = os.getenv('BOT_USER_ID')

# Internal API Key for protecting the /gemini route
INTERNAL_API_KEY = os.getenv('INTERNAL_API_KEY')

app = Flask(__name__)

def cleanup_processed_ids():
    """Remove IDs older than DEDUPE_RETENTION_SECONDS."""
    current_time = time.time()
    with processed_ids_lock:
        # Create a list of keys to remove to avoid runtime error during iteration
        to_remove = [msg_id for msg_id, ts in processed_ids.items()
                     if current_time - ts > DEDUPE_RETENTION_SECONDS]
        for msg_id in to_remove:
            del processed_ids[msg_id]

def is_duplicate(client_msg_id):
    """Check if message ID is processed, in a thread-safe way."""
    if not client_msg_id:
        return False

    # Lazy cleanup on check (simplest approach for this scale)
    cleanup_processed_ids()

    with processed_ids_lock:
        if client_msg_id in processed_ids:
            return True
        processed_ids[client_msg_id] = time.time()
        return False

def handle_event_async(data):
    thread = Thread(target=handle_event, args=(data,), daemon=True)
    thread.start()

def handle_event(data):
    event = data["event"]

    # --- Consolidated Bot Filtering ---
    # Ignore messages from any bot, including itself
    if "bot_id" in event or event.get("user") == BOT_USER_ID:
        return

    # --- Prevent Duplicate Processing from Slack Retries ---
    client_msg_id = event.get("client_msg_id")
    if is_duplicate(client_msg_id):
        return

    channel_id = event["channel"]
    user_message = event.get("text", "")
    thread_ts = event.get("thread_ts") or event.get("ts")

    # If it's an app mention, remove the bot's user ID from the message text
    if f"<@{BOT_USER_ID}>" in user_message:
        user_message = user_message.replace(f"<@{BOT_USER_ID}>", "").strip()

    if not user_message:
        return

    try:
        conversation_history = []
        if thread_ts:
            # Fetch thread history
            result = client.conversations_replies(channel=channel_id, ts=thread_ts)
            messages = result.get("messages", [])

            # Construct conversation history for the model
            for msg in messages:
                # Skip the current message being processed, it's added at the end
                if msg.get("client_msg_id") == client_msg_id:
                    continue

                text = msg.get("text", "").replace(f"<@{BOT_USER_ID}>", "").strip()

                if msg.get("user") == BOT_USER_ID or "bot_id" in msg:
                    conversation_history.append(f"Bot: {text}")
                else:
                    conversation_history.append(f"User: {text}")

        # Add the current user message to form the complete prompt
        conversation_history.append(f"User: {user_message}")
        full_prompt = "\n".join(conversation_history)

        # Generate response from Gemini
        gemini = model.generate_content(full_prompt)
        textout = gemini.text.replace("**", "*")

        # Post the response back to the thread
        client.chat_postMessage(
            channel=channel_id,
            text=textout,
            thread_ts=thread_ts,
            mrkdwn=True
        )

    except SlackApiError as e:
        print(f"Error posting message: {e.response['error']}")
    except Exception as e:
        print(f"An error occurred: {e}")

@app.route('/gemini', methods=['GET'])
def helloworld():
    # --- Security Check ---
    request_key = request.headers.get('X-API-KEY')
    if not INTERNAL_API_KEY or request_key != INTERNAL_API_KEY:
        # 401 Unauthorized if key is missing or wrong
        return jsonify({"error": "Unauthorized"}), 401

    if request.method == 'GET':
        gemini = model.generate_content("Hi")
        return gemini.text

@app.route("/slack/events", methods=["POST"])
def slack_events():
    data = request.json
    if "challenge" in data:
        return jsonify({"challenge": data["challenge"]})

    if "event" in data:
        handle_event_async(data)

    return "", 200

if __name__ == "__main__":
    app.run(debug=True)
