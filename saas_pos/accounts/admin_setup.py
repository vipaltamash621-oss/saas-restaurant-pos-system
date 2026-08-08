"""
Admin setup view - accessible without login
"""
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.contrib.auth import get_user_model

User = get_user_model()

@require_http_methods(["POST"])
def create_admin_user(request):
    """Create admin user if none exists"""
    
    # Check if admin already exists
    if User.objects.filter(username='admin').exists():
        return JsonResponse({
            'status': 'error',
            'message': 'Admin user already exists'
        })
    
    try:
        # Create admin user
        user = User.objects.create_user(
            username='admin',
            email='admin@example.com',
            password='admin123'
        )
        user.is_staff = True
        user.is_superuser = True
        user.role = 'SUPERADMIN'
        user.save()
        
        return JsonResponse({
            'status': 'success',
            'message': 'Admin user created successfully!',
            'username': 'admin',
            'password': 'admin123'
        })
    except Exception as e:
        return JsonResponse({
            'status': 'error',
            'message': str(e)
        })
