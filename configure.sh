#!/usr/bin/bash

# Create hadoop directory
hadoop fs -mkdir -p trabajo
# Add the dataset into the directory
hadoop fs -put ./dataset trabajo

# Install Python libraries
pip install prettytable
pip install httpx
pip install matplotlib
pip install random

# Create SSH-RSA key to access AWS_LAB
ssh-keygen -b 2048 -t rsa -f access_lab -q -N ""