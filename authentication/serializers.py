from rest_framework import serializers

from django.contrib.auth import authenticate

from .models import User


class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=128,
        min_length=8,
        write_only=True
    )

    token = serializers.CharField(max_length=256, read_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'token']

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=256, read_only=True)
    email = serializers.CharField(max_length=256)
    password = serializers.CharField(max_length=128, write_only=True)
    token = serializers.CharField(max_length=256, read_only=True)

    def validate(self, data):
        email = data.get('email', None)
        password = data.get('password', None)

        if email is None:
            raise serializers.ValidationError('An email address is required tp log in.')

        if password is None:
            raise serializers.ValidationError('A password is required to log in.')

        user = authenticate(username=email, password=password)

        if user is None:
            raise serializers.ValidationError('A user with this email and password was not found.')

        if not user.is_active:
            raise serializers.ValidationError('This user has been deactivated.')

        return {
            'email': user.email,
            'username': user.username,
            'token': user.token
        }
