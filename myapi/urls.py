from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from myapi import views

urlpatterns = [
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>', views.UserDetail.as_view()),
    path('posts/', views.PostList.as_view()),
    path('posts/<int:pk>/', views.PostDetail.as_view()),
    path('users/register', views.UserCreateAPIView.as_view(), name='register'),
    path('users/login', views.UserLoginAPIView.as_view(), name='login'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
