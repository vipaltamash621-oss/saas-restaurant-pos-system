#!/usr/bin/env bash
# exit on error
set -o errexit

# Navigate to Django project directory
cd saas_pos

# Install minimal dependencies
pip install -r requirements.txt

# Collect static files
python manage.py collectstatic --no-input

# Run migrations
python manage.py migrate

# Create admin user using custom command
python manage.py create_admin