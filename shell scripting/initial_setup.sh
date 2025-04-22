#!/bin/bash

# Exit immediately on any error
set -e

REPO_URL="https://github.com/jdanninger/Jakobs-LinkedIn-App.git"
REPO_NAME="Jakobs-LinkedIn-App"

echo "Cloning the repository..."
if ! git clone "$REPO_URL"; then
    echo "❌ Failed to clone repository: $REPO_URL"
    exit 1
fi

cd "$REPO_NAME" || {
    echo "❌ Failed to enter directory: $REPO_NAME"
    exit 1
}

echo "Installing Python and pip..."


sudo apt update

# Install Python
if ! command -v python3 &> /dev/null; then
    echo "Installing Python 3..."
    sudo apt install -y python3
fi

# Install pip
if ! command -v pip3 &> /dev/null; then
    echo "Installing pip..."
    sudo apt install -y python3-pip
fi

# Upgrade pip
echo "Upgrading pip..."
python3 -m pip install --upgrade pip

# Install depends
if [[ -f requirements.txt ]]; then
    echo "Installing Python packages from requirements.txt..."
    pip3 install -r requirements.txt
else
    echo "❌ requirements.txt not found!"
    exit 1
fi

echo "✅ Setup complete!"
