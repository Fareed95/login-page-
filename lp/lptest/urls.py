from django.urls import path
from .views import api_register, api_login, api_welcome

urlpatterns = [
    path('api/register/', api_register, name='api_register'),
    path('api/login/', api_login, name='api_login'),
    path('api/welcome/', api_welcome, name='api_welcome'),
    # Add other URL patterns if needed
]
