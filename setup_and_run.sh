#!/usr/bin/env bash
# setup_and_run.sh
# This script prepares the environment and runs the Project-G2 Trivia Game web app.
# Usage: bash setup_and_run.sh

set -e

# Check for Python 3
if ! command -v python3 &> /dev/null; then
  echo "Python 3 is not installed. Please install Python 3.8 or higher."
  exit 1
fi

# Check for venv module
if ! python3 -m venv --help &> /dev/null; then
  echo "Python venv module is not available. Please ensure you have python3-venv installed."
  exit 1
fi

# Check for pip
if ! python3 -m pip --version &> /dev/null; then
  echo "pip is not installed. Attempting to install pip..."
  curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
  python3 get-pip.py
  rm get-pip.py
fi

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
  echo "Creating virtual environment..."
  python3 -m venv venv
fi

# Activate virtual environment
if [[ "$OSTYPE" == "msys" || "$OSTYPE" == "win32" ]]; then
  source venv/Scripts/activate
else
  source venv/bin/activate
fi

# Upgrade pip
pip install --upgrade pip

# Install dependencies
if [ -f requirements.txt ]; then
  pip install -r requirements.txt
else
  echo "requirements.txt not found!"
  exit 1
fi

# Run the Flask app
cd src
export FLASK_APP=app.py
export FLASK_ENV=development
python app.py
