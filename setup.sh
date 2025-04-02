#!/bin/bash

# Helper script to set up movie recommendation service on Render. Makes directory structure,
# installs Python dependencies and runs Python script to get/encode movie dataset & train model.

echo ''
echo '###################################'
echo '# KNN movie recommendation system #'
echo '###################################'
echo ''
echo 'Running set-up'

# Make asset directories
mkdir -p data
mkdir -p models

echo ''

# Install Python dependencies
pip install --upgrade pip
pip install -r requirements.txt

echo ''

# Train the model
python ./src/train_model.py