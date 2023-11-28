from blog.serializers import PostSerializer
from rest_framework.views import APIView
from blog.models import Post
from rest_framework.response import Response
import requests
from django.shortcuts import render, redirect, get_object_or_404
from rest_framework import status
from .forms import PostForm
from django.http import Http404, HttpResponse, JsonResponse
from django.shortcuts import render
import requests
from api.views import PostView
from django.views import View
from django.views.decorators.csrf import csrf_exempt


def blog_posts(request):
    return render(request, 'public/blog_posts.html')