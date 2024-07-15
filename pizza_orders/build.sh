#!/usr/bin/env bash
# Exit on error
set -o errexit

# Install dependencies
pip install -r ../requirements.txt

# Navigate to the pizza_orders directory
cd pizza_orders

# Convert static asset files
python manage.py collectstatic --no-input

# Apply any outstanding database migrations
python manage.py migrate