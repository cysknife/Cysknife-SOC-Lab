#!/bin/bash
# Cysknife SOC Lab - Environment Setup Script

echo "Setting up Cysknife SOC Lab directories..."

# Create necessary data directories
mkdir -p ../data/logs
mkdir -p ../data/pcaps
mkdir -p ../configs/splunk
mkdir -p ../configs/wazuh

# Create Labs directories
mkdir -p ../Labs/week1-foundations
mkdir -p ../Labs/week2-siem-core
mkdir -p ../Labs/week3-incident-response
mkdir -p ../Labs/week4-capstone

# Set execute permissions for python scripts
chmod +x *.py

echo "Setup complete! Directory structure is ready."