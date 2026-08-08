#!/usr/bin/env python
"""
Simple script to set admin password without shell access
Run this locally if needed
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

# Delete existing admin
User.objects.filter(username='admin').delete()

# Create new admin
user = User.objects.create_user(
    username='admin',
    email='admin@example.com',
    password='admin123'
)
user.is_staff = True
user.is_superuser = True
user.role = 'SUPERADMIN'
user.save()

print('✅ Admin user created!')
print('Username: admin')
print('Password: admin123')
print('URL: /admin/')
