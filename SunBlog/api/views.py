from django.shortcuts import render
from blog.serializers import PostSerializer
from rest_framework.views import APIView
from blog.models import Post
from rest_framework.response import Response
import requests
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema

class PostView(APIView):
    def singlePost(self, id_arg):
        try:
            queryset = Post.objects.get(id=id_arg)
            return queryset
        except Post.DoesNotExist: 
            return None

    @swagger_auto_schema(
        operation_summary='Get a post or list all posts',
        operation_description="Get information about a specific post if id_arg is provided, otherwise list all posts",
        request_body=None,  # optional
        responses={
            200: 'PostSerializer(many=True)',
            400: "Bad request - Post with provided id does not exist"
        }
    )
    def get(self, request, id_arg=None):
        """
        Returns a list of posts or a specific post
        Depends on:
        - APIView
        - Post
        - PostSerializer
        - Response
        :param APIView self: the object itself
        :param Request request: an object representing the HTTP request
        :param id_arg: optional argument representing the id of a specific post
        :return: a list of posts in JSON format or a specific post in JSON format
        :rtype: JSON
        """
        if id_arg is None:
            queryset = Post.objects.all().order_by('dt_publicado')
            serializer = PostSerializer(queryset, many=True)
            return Response(serializer.data)
        else:
            queryset = self.singlePost(id_arg)
            if queryset:
                serializer = PostSerializer(queryset)
                return Response(serializer.data)
            else:
                return Response({
                    'msg': f'Post com id #{id_arg} não existe'
                }, status.HTTP_400_BAD_REQUEST)
        
    @swagger_auto_schema(
        operation_summary='Create a post',
        operation_description="Create a new post",
        request_body=PostSerializer,
        responses={
            201: 'PostSerializer',
            400: "Bad request - Invalid data"
        }
    )
    def post(self, request):
        """
        Creates a new post
        Depends on:
        - APIView
        - Post
        - PostSerializer
        - Response
        :param APIView self: the object itself
        :param Request request: an object representing the HTTP request
        :return: the created post in JSON format
        :rtype: JSON
        """
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_summary='Update a post',
        operation_description="Update a specific post given its id",
        request_body=PostSerializer,
        responses={
            200: 'PostSerializer',
            400: "Bad request - Post with provided id does not exist or invalid data"
        }
    )
    def put(self, request, id_arg):
        """
        Updates a specific post
        Depends on:
        - APIView
        - Post
        - PostSerializer
        - Response
        :param APIView self: the object itself
        :param Request request: an object representing the HTTP request
        :param id_arg: argument representing the id of a specific post
        :return: the updated post in JSON format
        :rtype: JSON
        """
        post = self.singlePost(id_arg)
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id_arg):
        '''
        Remove um post existente
        Depende de:
        - APIView
        - Post
        - PostSerializer
        - Response
        :param APIView self: o próprio objeto
        :param Request request: um objeto representando o pedido HTTP 
        :param int id_arg: o ID do post a ser removido
        :return: uma resposta HTTP sem conteúdo
        :rtype: HTTPResponse
        '''
        try:
            post = Post.objects.get(pk=id_arg)
        except Post.DoesNotExist:
            return Response({'error': f'item [{id_arg}] não encontrado'}, status=status.HTTP_404_NOT_FOUND)

        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)