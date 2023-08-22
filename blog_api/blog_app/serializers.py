from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Blog, News


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

    def create(self, validate_data):
        user = User.objects.create_user(**validate_data)
        return user


class BlogSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', read_only=True)

    class Meta:
        model = Blog
        fields = ('id', 'title', 'content', 'created_at')


class NewsSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', read_only=True)

    class Meta:
        model = News
        fields = ('id', 'title', 'desc', 'created_at')
