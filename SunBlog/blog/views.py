from blog.serializers import PostSerializer
from rest_framework.views import APIView
from blog.models import Post
from rest_framework.response import Response
import requests
from django.shortcuts import render
from rest_framework import status
from .forms import PostForm


def home(request):
    return render(request, 'blog/home.html')

def blog_posts(request):
    api_url = 'http://127.0.0.1:8000/api/lista/' 
    response = requests.get(api_url)
    blog_posts = response.json()

    return render(request, 'blog/blog_posts.html', {'blog_posts': blog_posts})

def insert_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post_data = {
                'titulo': form.cleaned_data['titulo'],
                'slug': form.cleaned_data['slug'],
                'autor': form.cleaned_data['autor'].id,
                'corpo': form.cleaned_data['corpo'],
                'dt_publicado': form.cleaned_data['dt_publicado'].isoformat(),
                'status': form.cleaned_data['status'],
            }

            api_url = 'http://127.0.0.1:8000/api/umpost/'
            response = requests.post(api_url, json=post_data)

            # Check if the request was successful
            if response.status_code == 201:  # Assuming 201 means created
                # Redirect or handle success as needed
                return redirect('success_url')
            else:
                # Handle the error, e.g., by displaying an error message
                error_message = f"Failed to create post. API responded with {response.status_code} status."
                return render(request, 'blog/error.html', {'error_message': error_message})
    else:
        form = PostForm()

    return render(request, 'blog/new_blog.html', {'form': form})