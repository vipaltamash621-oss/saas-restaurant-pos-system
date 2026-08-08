from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

User = get_user_model()

class Command(BaseCommand):
    help = 'Create admin superuser'

    def handle(self, *args, **options):
        # Delete existing admin if exists
        User.objects.filter(username='admin').delete()
        
        # Create new admin user
        user = User.objects.create_superuser(
            username='admin',
            email='admin@example.com',
            password='admin123',
            role='SUPERADMIN'
        )
        
        self.stdout.write(
            self.style.SUCCESS('✅ Successfully created superuser: admin / admin123')
        )
