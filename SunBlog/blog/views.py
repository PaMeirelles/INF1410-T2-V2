from blog.serializers import PostSerializer
from rest_framework.views import APIView
from blog.models import Post
from rest_framework.response import Response
import requests
from django.shortcuts import render
from rest_framework import status


def home(request):
    return render(request, 'blog/home.html')

class PostView(APIView):
    def get(self, request):
        queryset = Post.objects.all().order_by('dt_publicado')
        serializer = PostSerializer(queryset, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

def blog_posts(request):
    api_url = 'http://127.0.0.1:8000/blog/lista/'  # Replace with your API endpoint
    response = requests.get(api_url)
    blog_posts = response.json()

    return render(request, 'blog/blog_posts.html', {'blog_posts': blog_posts})