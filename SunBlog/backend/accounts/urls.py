from django.urls import path
from .views import RegisterView, CustomAuthToken
app_name = 'accounts'

urlpatterns = [
    path('register-api/', RegisterView.as_view(), name='register-api'),
    path('token-auth/', CustomAuthToken.as_view(), name='token-auth'),
]
