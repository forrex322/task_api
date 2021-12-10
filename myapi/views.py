from rest_framework import generics, permissions
from myapi import serializers
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from myapi.models import Post
from myapi.permissions import IsOwnerOrReadOnly
from .pagination import PostLimitOffsetPagination, PostPageNumberPagination
from .serializers import UserCreateSerializer

User = get_user_model()


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = serializers.PostSerializer
    permissions_classes = [permissions.IsAuthenticatedOrReadOnly]
    pagination_class = PostPageNumberPagination

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = serializers.PostSerializer
    permissions_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    pagination_class = PostPageNumberPagination


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


class UserCreateAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer
