from django.views.generic.base import RedirectView
from django.urls import path
from .views import blog_posts

app_name = 'blog'

urlpatterns = [
    path('', blog_posts, name='blog_posts')]