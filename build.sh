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

# Load initial data (admin user)
python manage.py loaddata accounts/fixtures/initial_data.json || python manage.py create_admin