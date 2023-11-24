from django.shortcuts import render
from blog.serializers import PostSerializer
from rest_framework.views import APIView
from blog.models import Post
from rest_framework.response import Response
import requests
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from rest_framework.decorators import authentication_classes


@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
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

    def post(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id_arg):
        id_erro = ""
        erro = False
        post = Post.objects.get(id=id_arg)
        if post:
            post.delete()
        else:
            id_erro += str(id_arg)
            erro = True
        if erro:
            return Response({'error': f'item [{id_erro}] não encontrado'},status.HTTP_404_NOT_FOUND)
        else:
            return Response(status=status.HTTP_204_NO_CONTENT)