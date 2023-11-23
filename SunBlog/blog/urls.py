from django.urls import path
from .views import blog_posts, insert_post

app_name = 'blog'

urlpatterns = [
    path('posts/', blog_posts, name='blog_posts'),
    path('insert/', insert_post, name='insert_post')
]