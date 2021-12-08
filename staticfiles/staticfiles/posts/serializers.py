from rest_framework import serializers

from blog.models import Post
from profiles.models import ProfileCustomUser
from profiles.managers import CustomUserManager


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'author', 'title', 'body', 'created_at',)
        model = Post


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileCustomUser
        manager_class = CustomUserManager
        fields = ['email', 'password', ]
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = ProfileCustomUser.objects.create_user(validated_data['email'],
                                                     validated_data['password'])

        return user
