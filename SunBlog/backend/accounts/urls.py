from django.urls import path
from .views import register_page, login_page, RegisterView, logout_page, CustomAuthToken
app_name = 'accounts'

urlpatterns = [
    path('register-api/', RegisterView.as_view(), name='register-api'),
    path('register/', register_page, name='register'),
    path('logout/', logout_page, name='logout'),
    path('token-auth/', CustomAuthToken.as_view(), name='token-auth'),
]
