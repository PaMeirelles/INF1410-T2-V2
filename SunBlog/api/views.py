from django.shortcuts import render
from blog.serializers import PostSerializer
from rest_framework.views import APIView
from blog.models import Post
from rest_framework.response import Response
import requests
from rest_framework import status

class PostView(APIView):
    def singlePost(self, id_arg):
        try:
            queryset = Post.objects.get(id=id_arg)
            return queryset
        except Post.DoesNotExist: 
            return None

    def get(self, request, id_arg=None):
        if id_arg is None:
            # Handle the case where no id_arg is provided
            queryset = Post.objects.all().order_by('dt_publicado')
            serializer = PostSerializer(queryset, many=True)
            return Response(serializer.data)
        else:
            # Handle the case where id_arg is provided
            queryset = self.singlePost(id_arg)
            if queryset:
                serializer = PostSerializer(queryset)
                return Response(serializer.data)
            else:
                return Response({
                    'msg': f'Post com id #{id_arg} não existe'
                }, status.HTTP_400_BAD_REQUEST)
        
    def put(self, request, id_arg):
        post = self.singlePost(id_arg)
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)