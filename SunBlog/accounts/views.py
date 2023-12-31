from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from django.contrib.auth import login, logout
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.views import APIView
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import authentication_classes, permission_classes

class CustomAuthToken(ObtainAuthToken):
    @swagger_auto_schema(
        operation_summary='Obter o token de autenticação',
        operation_description='Retorna o token em caso de sucesso na autenticação ou HTTP 401',
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'username': openapi.Schema(type=openapi.TYPE_STRING),
                'password': openapi.Schema(type=openapi.TYPE_STRING),
            },
            required=['username', 'password', ],
        ),
        responses={
            status.HTTP_200_OK: 'Token is returned.',
            status.HTTP_401_UNAUTHORIZED: 'Unauthorized request.',
        },
    )
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                token, _ = Token.objects.get_or_create(user=user)
                login(request, user)
                return Response({'token': token.key})
        return Response(status=status.HTTP_401_UNAUTHORIZED)
    
    @swagger_auto_schema(
        operation_summary='Obtém o username do usuário',
        operation_description="Retorna o username do usuário ou apenas visitante se o usuário n",
        security=[{'Token':[]}],
        manual_parameters=[
            openapi.Parameter(
                'Authorization',
                openapi.IN_HEADER,
                type=openapi.TYPE_STRING,
                description='Token de autenticação no formato "token \<<i>valor do token</i>\>"',
                default='token ',
            ),
        ],
        responses={
            200: openapi.Response(
                description='Nome do usuário',
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={'username': openapi.Schema(type=openapi.TYPE_STRING)},
                ),
            )   
        }
    )
    def get(self, request):
        '''
        Parâmetros: o token de acesso
        Retorna: o username ou 'visitante'
        '''
        try:
            token = request.META.get('HTTP_AUTHORIZATION').split(' ')[1] # token
            token_obj = Token.objects.get(key=token)
            user = token_obj.user
            return Response(
                {'username': user.username},
                status=status.HTTP_200_OK)
        except (Token.DoesNotExist, AttributeError):
            return Response(
                {'username': 'visitante'},
                status=status.HTTP_404_NOT_FOUND)
        
    @swagger_auto_schema(
        operation_description='Realiza logout do usuário, apagando o seu token',
        operation_summary='Realiza logout',
        security=[{'Token':[]}],
        manual_parameters=[
            openapi.Parameter('Authorization', openapi.IN_HEADER,
            type=openapi.TYPE_STRING, default='token ',
            description='Token de autenticação no formato "token \<<i>valor do token</i>\>"',
            ),
        ],
        request_body=None,
        responses={
            status.HTTP_200_OK: 'User logged out',
            status.HTTP_400_BAD_REQUEST: 'Bad request',
            status.HTTP_401_UNAUTHORIZED: 'User not authenticated',
            status.HTTP_403_FORBIDDEN: 'User not authorized to logout',
            status.HTTP_500_INTERNAL_SERVER_ERROR: 'Erro no servidor',
        },
    )
    def delete(self, request):
        try:
            token = request.META.get('HTTP_AUTHORIZATION').split(' ')[1]
            token_obj = Token.objects.get(key=token)
        except (Token.DoesNotExist, IndexError):
            return Response({'msg': 'Token não existe.'}, status=status.HTTP_400_BAD_REQUEST)
        user = token_obj.user
        if user.is_authenticated:
            request.user = user
            logout(request)
            token = Token.objects.get(user=user)
            token.delete()
            return Response({'msg': 'Logout bem-sucedido.'},
                status=status.HTTP_200_OK)
        else:
            return Response({'msg': 'Usuário não autenticado.'},
                status=status.HTTP_403_FORBIDDEN)


    
def login_page(request):
    return render(request, "accounts/login.html")

@authentication_classes([])
@permission_classes([])
class RegisterView(APIView):
    @swagger_auto_schema(
        operation_summary='Register a new user',
        operation_description='Creates a new user account',
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'username': openapi.Schema(type=openapi.TYPE_STRING),
                'email': openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_EMAIL),
                'password': openapi.Schema(type=openapi.TYPE_STRING),
            },
            required=['username', 'email', 'password'],
        ),
        responses={
            status.HTTP_201_CREATED: 'User registered successfully.',
            status.HTTP_400_BAD_REQUEST: 'Bad request - Invalid data or user already exists.',
        },
    )
    def post(self, request):
        username = request.data.get('username')
        email = request.data.get('email')
        password = request.data.get('password')

        if not username or not email or not password:
            return Response({'error': 'Username, email, and password are required.'}, status=status.HTTP_400_BAD_REQUEST)

        # Check if the username or email already exists
        if User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists():
            return Response({'error': 'Username or email already exists.'}, status=status.HTTP_400_BAD_REQUEST)

        # Create a new user
        user = User.objects.create_user(username=username, email=email, password=password)

        # Create a token for the new user
        token, _ = Token.objects.get_or_create(user=user)

        return Response({'token': token.key}, status=status.HTTP_201_CREATED)

def register_page(request):
    return render(request, "accounts/register.html")

def logout_page(request):
    return render(request, "accounts/logout.html")