#!/bin/bash
if [ ! -f .env ]; then
    echo "Error: .env file not found. Please ensure it exists in the root directory."
    exit 1
fi

# Source the .env file to load environment variables
set -a
source .env
set +a

gcloud logging read "resource.type = cloud_run_revision" --project="$PROJECT_ID" --limit=100 > latest_logs.txt
