from django.urls import path
from accounts import views
from .views import login_page
app_name = 'accounts'

urlpatterns = [
    path("login/", login_page, name='login'),
    path('token-auth/', views.CustomAuthToken.as_view(), name='token-auth'),
]
