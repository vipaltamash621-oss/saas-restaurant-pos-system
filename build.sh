#!/usr/bin/env bash
set -o errexit

cd saas_pos

# Install dependencies
pip install -r requirements.txt

# Collect static files
python manage.py collectstatic --no-input

# Run migrations
python manage.py migrate

# Create admin user with Python (simple and reliable)
python << 'EOF'
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.contrib.auth import get_user_model
User = get_user_model()

# Remove if exists
User.objects.filter(username='admin').delete()

# Create new admin
try:
    u = User(
        username='admin',
        email='admin@example.com',
        is_staff=True,
        is_superuser=True,
        is_active=True,
        role='SUPERADMIN'
    )
    u.set_password('admin123')
    u.save()
    print('Admin user created: admin/admin123')
except Exception as e:
    print(f'Error: {e}')
EOF