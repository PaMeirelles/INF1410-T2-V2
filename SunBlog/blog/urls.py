from django.urls import path
from .views import api_blog_posts, blog_posts, insert_post, edit_post, post_detail

app_name = 'blog'

urlpatterns = [
    path('api/blog/posts/', api_blog_posts, name='api_blog_posts'),
    path('posts/', blog_posts, name='blog_posts'),
    path('insert/', insert_post, name='insert_post'),
    path('edit_post/<int:post_id>/', edit_post, name='edit_post')
    path('post/<int:post_id>/', post_detail, name='post_detail'),
]