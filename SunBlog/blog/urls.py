from django.urls import path
from .views import blog_posts


urlpatterns = [
    path('posts/', blog_posts, name='blog_posts')

]