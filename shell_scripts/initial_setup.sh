#!/bin/bash

set -e  # Exit on any error

REPO_URL="https://github.com/jdanninger/Jakobs-LinkedIn-App.git"
REPO_NAME="Jakobs-LinkedIn-App"
VENV_DIR="venv"

echo "🔄 Cloning the repository..."
if ! git clone "$REPO_URL"; then
    echo "❌ Failed to clone repository: $REPO_URL"
    exit 1
fi

cd "$REPO_NAME" || {
    echo "❌ Failed to enter directory: $REPO_NAME"
    exit 1
}

echo "🐍 Checking for Python 3 and venv support..."

# Ensure Python 3 is installed
if ! command -v python3 &> /dev/null; then
    echo "Installing Python 3..."
    sudo apt update && sudo apt install -y python3
fi

# Ensure venv is available
if ! python3 -m venv --help &> /dev/null; then
    echo "Installing python3-venv..."
    sudo apt install -y python3-venv
fi

echo "📦 Creating virtual environment..."
python3 -m venv "$VENV_DIR"

echo "⚙️ Activating virtual environment..."
source "$VENV_DIR/bin/activate"

echo "⬆️ Upgrading pip..."
pip install --upgrade pip

echo "📄 Installing Python dependencies..."
if [[ -f requirements.txt ]]; then
    pip install -r requirements.txt
else
    echo "❌ requirements.txt not found!"
    deactivate
    exit 1
fi

echo "🌐 Installing ngrok via official apt source..."

# Add ngrok's GPG key and repo, then install
curl -sSL https://ngrok-agent.s3.amazonaws.com/ngrok.asc \
  | sudo tee /etc/apt/trusted.gpg.d/ngrok.asc >/dev/null

echo "deb https://ngrok-agent.s3.amazonaws.com buster main" \
  | sudo tee /etc/apt/sources.list.d/ngrok.list

sudo apt update
sudo apt install -y ngrok

echo "✅ Setup complete!"
echo "👉 To activate the virtual environment later, run:"
echo "   source $REPO_NAME/$VENV_DIR/bin/activate"
