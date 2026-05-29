#!/bin/bash

# 1. Update system packages
echo "Updating system..."
sudo apt-get update -y

# 2. Install Python and venv (Idempotent: apt handles 'already installed' checks)
echo "Installing Python3 and pip..."
sudo apt-get install -y python3-pip python3-venv

# 3. Create Virtual Environment
VENV_PATH="/mnt/ml-data/venv"

if [ -d "$VENV_PATH" ]; then
    echo "Virtual environment already exists at $VENV_PATH."
else
    echo "Creating virtual environment..."
    python3 -m venv $VENV_PATH
fi

# 4. Activate and Install Libraries
source $VENV_PATH/bin/activate

echo "Installing ML libraries..."
# Using pip install --upgrade to ensure idempotency without errors
pip install --upgrade pip
pip install pandas scikit-learn joblib boto3

echo "Setup Complete!"
