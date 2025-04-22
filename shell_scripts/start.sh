#!/bin/bash

set -e  # Exit on any error

# Get the directory of this script
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(dirname "$SCRIPT_DIR")"
STREAMLIT_FILE="main.py"
NGROK_DOMAIN="jakobs-linkedin-reviewer"

# Move to the repo root
cd "$REPO_ROOT" || {
    echo "❌ Failed to move to repo root: $REPO_ROOT"
    exit 1
}

echo "🔄 Pulling latest changes from main branch..."
git checkout main
git pull origin main

# Activate virtual environment
if [[ -d "venv" ]]; then
    echo "🐍 Activating virtual environment..."
    source venv/bin/activate
else
    echo "❌ Virtual environment not found! Run setup.sh first."
    exit 1
fi

# Start Streamlit in the background
echo "🚀 Launching Streamlit app: $STREAMLIT_FILE"
streamlit run "$STREAMLIT_FILE" &

# Give it a few seconds to spin up
sleep 5

# Start ngrok with the given subdomain
echo "🌐 Starting ngrok tunnel: https://$NGROK_DOMAIN.ngrok.app"
ngrok http http://localhost:8501 --hostname="$NGROK_DOMAIN.ngrok.app"
