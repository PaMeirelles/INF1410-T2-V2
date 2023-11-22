from blog.serializers import PostSerializer
from rest_framework.views import APIView
from blog.models import Post
from rest_framework.response import Response
import requests
from django.shortcuts import render
from rest_framework import status


def home(request):
    return render(request, 'blog/home.html')

def blog_posts(request):
    api_url = 'http://127.0.0.1:8000/api/lista/' 
    response = requests.get(api_url)
    blog_posts = response.json()

    return render(request, 'blog/blog_posts.html', {'blog_posts': blog_posts})