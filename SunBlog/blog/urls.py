from django.urls import path
from blog import views
from .views import blog_posts


urlpatterns = [
    path('posts/', blog_posts, name='blog_posts'),
    path("lista/", views.PostView.as_view(), name='lista-posts')
]