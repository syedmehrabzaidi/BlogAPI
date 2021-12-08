from rest_framework import serializers

from profiles.models import ProfileCustomUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileCustomUser
        fields = ('id', 'username', 'email')


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileCustomUser
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = ProfileCustomUser.objects.create_user(**validated_data)
        return user

