#!/bin/bash

set -e  # Exit on any error

# Get the directory of this script
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(dirname "$SCRIPT_DIR")"
STREAMLIT_FILE="main.py"
NGROK_DOMAIN="jakobs-linkedin-reviewer"
PORT=8501

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

echo "🚀 Launching Streamlit on port $PORT..."
nohup streamlit run "$STREAMLIT_FILE" --server.port "$PORT" > streamlit.log 2>&1 &

sleep 5  # Give streamlit time to start

echo "🌐 Starting ngrok tunnel in background..."
nohup ngrok http http://localhost:$PORT --hostname="$NGROK_DOMAIN.ngrok.app" > ngrok.log 2>&1 &


