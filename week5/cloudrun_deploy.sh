#!/usr/bin/env bash
set -euo pipefail

# --- CONFIG ---
PROJECT_ID="${PROJECT_ID:-your-gcp-project-id}"
REGION="${REGION:-europe-west1}"
SERVICE="${SERVICE:-house-price-api}"

# Enable services (first time only)
gcloud services enable run.googleapis.com artifactregistry.googleapis.com --project "$PROJECT_ID"

# Create a repo for images (first time only)
gcloud artifacts repositories create containers --repository-format=docker --location="$REGION" --project "$PROJECT_ID" || true

# Build & push image
gcloud builds submit --tag "$REGION-docker.pkg.dev/$PROJECT_ID/containers/$SERVICE:latest" . --project "$PROJECT_ID"

# Deploy to Cloud Run (fully managed)
gcloud run deploy "$SERVICE"   --image="$REGION-docker.pkg.dev/$PROJECT_ID/containers/$SERVICE:latest"   --region="$REGION"   --platform=managed   --allow-unauthenticated   --max-instances=2   --port=8080   --project "$PROJECT_ID"
