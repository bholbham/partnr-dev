from django.shortcuts import render
from .models import BlogPost, Comment
from .serializers import BlogPostSerializer, CommentSerializer 
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User 
from rest_framework import status 

class RegisterView(APIView):
    def post(self,request):
        print('request data',request.data)
        username=request.data.get('username')
        password=request.data.get('password')

        if User.objects.filter(username=username).exists():
            return Response({'error':'Username already exists'},status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.create_user(username=username,password=password)
        return Response({'message':'User is registered successfully'},status=status.HTTP_201_CREATED)
        
class LoginView(APIView):
    def post(self,request):
        username=request.data.get('username')
        password=request.data.get('password')
        user = User.objects.filter(username=username).first()
        
        if user and user.check_password(password):
            refresh = RefreshToken.for_user(user)
            return Response({'message':'User is successfully logged in'},status=status.HTTP_200_OK)
        return Response({'error':'Invalid credentials'},status=status.HTTP_400_BAD_REQUEST)

class BlogPostViewSet(viewsets.ModelViewSet):
    serializer_class = BlogPostSerializer

    def get_queryset(self):
        return BlogPost.objects.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer

    def get_queryset(self):
        return Comment.objects.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)