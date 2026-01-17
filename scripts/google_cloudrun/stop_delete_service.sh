#!/bin/bash
gcloud run services delete gemini-slackbot --region us-central1 --project "$PROJECT_ID"
