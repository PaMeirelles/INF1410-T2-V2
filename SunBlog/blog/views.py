from blog.serializers import PostSerializer
from rest_framework.views import APIView
from blog.models import Post
from rest_framework.response import Response
import requests
from django.shortcuts import render, redirect, get_object_or_404
from rest_framework import status
from .forms import PostForm
from django.http import JsonResponse
from django.shortcuts import render
import requests
from api.views import PostView
from django.views import View
from django.views.decorators.csrf import csrf_exempt


def home(request):
    return render(request, 'blog/home.html')


# Função para retornar um JSON
def api_blog_posts(request):
    post_view = PostView()
    response = post_view.get(request)

    if response.status_code != 200:
        return JsonResponse({'error': 'An error occurred'}, status=response.status_code)

    blog_posts = response.data

    return JsonResponse(blog_posts, safe=False)

# Função para renderizar a página HTML
def blog_posts(request):
    post_view = PostView()
    response = post_view.get(request)

    if response.status_code != 200:
        return HttpResponse(status=response.status_code)

    blog_posts = response.data

    return render(request, 'blog/blog_posts.html', {'blog_posts': blog_posts})

def post_detail(request, post_id):
    post_view = PostView()
    post = post_view.get(request, post_id)

    if post is None:
        return HttpResponse(status=404)

    return render(request, 'blog/post_detail.html')

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
                return redirect('blog:blog_posts')
            else:
                # Handle the error, e.g., by displaying an error message
                error_message = f"Failed to create post. API responded with {response.status_code} status."
                return render(request, 'blog/error.html', {'error_message': error_message})
    else:
        form = PostForm()

    return render(request, 'blog/new_blog.html', {'form': form})

def edit_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)

        if 'delete' in request.POST:
            # Handle post deletion through the API endpoint
            api_url = f'http://127.0.0.1:8000/api/umpost/{post_id}/'
            headers = {"Content-Type": "application/json"}
            response = requests.delete(api_url, headers=headers)

            if response.status_code == 204:
                # Successful deletion, you can redirect to a success page or post list page
                return redirect('blog:blog_posts')
            else:
                print("oioio")
                # Handle the error, maybe show an error message to the user
                pass
        elif form.is_valid():
            form.save()

            # Update the post through the API endpoint
            api_url = f'http://127.0.0.1:8000/api/umpost/{post_id}/'
            data = {
                "titulo": form.cleaned_data['titulo'],
                "slug": form.cleaned_data['slug'],
                "autor": form.cleaned_data['autor'].id,
                "corpo": form.cleaned_data['corpo'],
                "dt_publicado": form.cleaned_data['dt_publicado'].isoformat(),
                "status": form.cleaned_data['status'],
            }
            headers = {"Content-Type": "application/json"}

            response = requests.delete(api_url, json=data, headers=headers)

            if response.status_code == 200:
                # Successful update, you can redirect to a success page or post detail page
                return redirect('blog:blog_posts')
            else:
                # Handle the error, maybe show an error message to the user
                pass
    else:
        form = PostForm(instance=post)

    return render(request, 'blog/edit_post.html', {'form': form, 'post': post})