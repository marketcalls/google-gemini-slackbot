# Slack Bot with Google Gemini

This Slack Bot integrates Google Gemini's AI technology into Slack, offering a smart, responsive assistant that enhances productivity. Follow these steps to set up and deploy your bot.

## Accessing the SlackBot from Slack Channel with an App Mention

![Accessing the SlackBot from Slack Channel with an App Mention
](https://i0.wp.com/www.marketcalls.in/wp-content/uploads/2024/02/image-38.png?resize=1024%2C463&ssl=1)

## Accessing the SlackBot Using Direct Message

![Accessing the SlackBot Using Direct Message](https://i0.wp.com/www.marketcalls.in/wp-content/uploads/2024/02/image-37.png?resize=1024%2C439&ssl=1)


## New Features in v1.1.0
### Multi-turn Conversations:
The bot now supports threaded replies. You can ask follow-up questions within a thread (e.g., "Add 10 more"), and the bot will remember previous interactions to maintain context.
<img width="1280" height="595" alt="image" src="https://github.com/user-attachments/assets/abdab5e4-8752-403e-88c1-70b83b3f6061" />


### Cloud Run Support:
Includes helper scripts and a Dockerfile to easily build and deploy the bot to Google Cloud Run. 
E.g.
```
$ cd scripts/google_cloudrun/
$ ./start_service.sh
Authenticating with Google Cloud...
Your browser has been opened to visit:
...
Starting deployment to Cloud Run...
Building using Dockerfile and deploying container to Cloud Run service [gemini-slackbot] in project [api-project-<ID>] region [us-central1]
✓ Building and deploying... Done.
  ✓ Validating Service...
  ✓ Uploading sources...
  ✓ Building Container... Logs are available at [https://console.cloud.google.com/cloud-build/builds;region=us-central1
  /09910f15-4729-4e78-b879-367e497886cf?project=<ID>].
  ✓ Creating Revision...
  ✓ Routing traffic...
  ✓ Setting IAM Policy...
Done.
Service [gemini-slackbot] revision [gemini-slackbot-00004-s5s] has been deployed and is serving 100 percent of traffic.
Service URL: https://gemini-slackbot-<ID>.us-central1.run.app
-------------------------------------------
Deployment successful!

Your service is available at: https://gemini-slackbot-<ID>-uc.a.run.app

IMPORTANT: Update your Slack App's Event Subscription Request URL to:
https://gemini-slackbot-<ID>-uc.a.run.app/slack/events
-------------------------------------------
$
```


## Resources

For a detailed step-by-step guide on building this digital assistant, visit [Building a Digital Assistant in Slack with Google Gemini: A Step-by-Step Guide](https://www.marketcalls.in/python/building-a-digital-assistant-in-slack-with-google-gemini-a-step-by-step-guide.html).

## Prerequisites

- Google Gemini API Key
- Slack App with OAuth & Permissions configured
- Python environment with necessary libraries
- Google Cloud CLI: Required if using the included deployment scripts for Cloud Run.
- Docker: Required if deploying via container or running locally with Docker.

## Configuration

Before running the project, you need to set up your environment variables. A sample environment file `.env.sample` is provided in the project. Copy this file to a new file named `.env` and update the variables with your own values.

The `.env.sample` file contains the following structure:
```
GOOGLE_API_KEY=your_google_api_key_here
SLACK_BOT_TOKEN=your_slack_bot_token_here
BOT_USER_ID=your_bot_user_id_here
FLASK_APP=your_entry_point_script_here # e.g., "app.py"
PROJECT_ID=your_google_cloud_project_id # Required for Cloud Run deployment
```


### Steps to configure your environment:

1. Copy the `.env.sample` file to a new file named `.env` in the root directory of the project.
2. Replace `your_google_api_key_here`, `your_slack_bot_token_here`, `your_bot_user_id_here`, `your_entry_point_script_here`, and `your_google_cloud_project_id` with your actual configuration values.

**Note:** Never commit your `.env` file or any sensitive credentials to version control. The `.env` file is included in the `.gitignore` to prevent accidental upload.


## Setup Instructions

1. **Obtain Google Gemini API Key**: Visit [Google AI Studio](https://aistudio.google.com/) and generate an API key for the [Gemini API](https://aistudio.google.com/api-keys).
2. **Generate Slack App**: Create a new app in [Slack](https://api.slack.com/apps) and configure basic information, including OAuth scopes required for the bot to function.
3. **Setup Event Subscriptions**: Subscribe to bot events in your Slack app settings to listen for and respond to messages.
4. **Install Your App**: Add your app to your workspace with the necessary permissions.
5. **Development Environment**:
   - Use Visual Studio Code or your preferred IDE.
   - Create a Python virtual environment and activate it.
   - Install necessary Python libraries including Flask, Slack SDK, and Google Gemini libraries.
6. **Implement Your Slack Bot**: Use Flask for handling Slack events and Google Gemini for generating responses.
7. **Deploy Your Application**: Choose between local testing with ngrok, deploying to [Google Cloud App Engine](https://cloud.google.com/appengine), or [Google Cloud Run](https://cloud.google.com/run).
8. **Configure Slack Event Subscriptions**: Update your Slack app's event subscriptions with your deployment's request URL.
9. **Access Your Slack Bot**: Test your bot via direct message or by mentioning it in a channel.

## Dependencies

Ensure your project has all the necessary dependencies by installing the required libraries which include Flask, various Google and Slack SDKs, and other utility libraries.
```
Flask
google-ai-generativelanguage
google-api-core
google-auth
google-generativeai
googleapis-common-protos
gunicorn
requests
slack_sdk
colorama
python-dotenv
```

To install the required dependencies for this project, follow the steps below:
Run the following command to install the dependencies listed in `requirements.txt`:

<code>pip install -r requirements.txt</code>

## Deployment

### Deployment to Google Cloud Run

This project now includes scripts to automate the deployment process to Google Cloud Run using Docker.

**1. Deploy Service**
Run the following script to build the container and deploy it to your Google Cloud project:
```bash
./scripts/google_cloudrun/start_service.sh
```


## License
This project is licensed under the MIT License
