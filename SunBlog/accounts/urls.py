from django.urls import path
from accounts import views
from .views import register_page, login_page, RegisterView
app_name = 'accounts'

urlpatterns = [
    path('register-api/', RegisterView.as_view(), name='register-api'),
    path('register/', register_page, name='register'),
    path('login/', login_page, name='login'),
    path('token-auth/', views.CustomAuthToken.as_view(), name='token-auth'),
]
