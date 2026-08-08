#!/usr/bin/env bash
# exit on error
set -o errexit

# Navigate to Django project directory
cd saas_pos

# Install minimal dependencies (without Pillow to avoid build issues)
pip install -r requirements.txt

# Collect static files
python manage.py collectstatic --no-input

# Run migrations
python manage.py migrate

# Create superuser with explicit creation
python manage.py shell << END
from django.contrib.auth import get_user_model
User = get_user_model()

# Delete if exists and recreate
User.objects.filter(username='admin').delete()

# Create new superuser
User.objects.create_superuser(
    username='admin',
    email='admin@example.com',
    password='admin123',
    first_name='Admin',
    last_name='User'
)
print('✅ Superuser created: admin / admin123')
END