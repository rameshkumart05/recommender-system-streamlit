#!/bin/bash

# Helper script to set up movie recommendation
# service on render. Makes directory structure,
# installs Python dependencies and runs python 
# script to train model.

# Make asset directories
mkdir data
mkdir models

# Install Python dependencies
pip install --upgrade pip
pip install -r requirements.txt

# Train the model
python ./src/train_model.py