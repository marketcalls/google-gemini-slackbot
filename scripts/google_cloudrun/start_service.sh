#!/bin/bash
# -----------------------------------------------------------------------------
# Configuration
# Source the .env file to load environment variables
set -a
source .env
set +a

# The name you want to give your Cloud Run service
SERVICE_NAME="gemini-slackbot"

# The Google Cloud region to deploy your service in (e.g., us-central1)
REGION="us-central1"


# -----------------------------------------------------------------------------
# --- Script starts here ---

echo "Authenticating with Google Cloud..."
gcloud auth login
gcloud config set project "$PROJECT_ID"

echo "Enabling necessary Google Cloud services..."
gcloud services enable run.googleapis.com \
    artifactregistry.googleapis.com \
    cloudbuild.googleapis.com \
    --project="$PROJECT_ID"

echo "Starting deployment to Cloud Run..."

# This command builds the container and deploys it in one step.
# It reads variables from your .env file and passes them to the Cloud Run service.
gcloud run deploy "$SERVICE_NAME" \
    --project="$PROJECT_ID" \
    --region="$REGION" \
    --source="../.." \
    --platform="managed" \
    --allow-unauthenticated \
    --env-vars-file="../../.env"

echo "-------------------------------------------"
echo "Deployment successful!"

# Get the service URL after deployment
SERVICE_URL=$(gcloud run services describe "$SERVICE_NAME" --project="$PROJECT_ID" --region="$REGION" --format="value(status.url)")

echo
echo "Your service is available at: $SERVICE_URL"
echo
echo "IMPORTANT: Update your Slack App's Event Subscription Request URL to:"
echo "$SERVICE_URL/slack/events"
echo "-------------------------------------------"
