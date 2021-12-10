from rest_framework import serializers
from django.contrib.auth.models import User
from myapi.models import Post
from django.contrib.auth import get_user_model
from rest_framework.serializers import (
    HyperlinkedIdentityField,
    ModelSerializer,
    SerializerMethodField,
    ValidationError
)

User = get_user_model()


class PostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Post
        fields = ['id', 'title', 'body', 'owner']


class UserSerializer(serializers.ModelSerializer):
    posts = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'posts']


class UserCreateSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        extra_kwargs = {'password':
                            {'write_only': True}
                        }

    def create(self, validated_data):
        username = validated_data['username']
        email = validated_data['email']
        password = validated_data['password']
        user_obj = User(
            username=username,
            email=email
        )
        user_obj.set_password(password) # stoped on 27 video
        user_obj.save()
        return validated_data
