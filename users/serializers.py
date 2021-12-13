from djoser.serializers import UserCreateSerializer, UserSerializer
from rest_framework import serializers
from .models import User, Profile


class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ('id', 'email', 'username', 'password')


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'phone', 'full_name')
        read_only_fields = ['user']


class ProfileSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField('get_username')
    full_name = serializers.SerializerMethodField('get_fullname')

    class Meta:
        model = Profile
        fields = ['id', 'username', 'full_name', 'user', 'profile_pic','bio','user_profile_pic']
        read_only_fields = ['user']

    def get_username(self, user):
        username = user.user.username
        return username

    def get_fullname(self, user):
        full_name = user.user.full_name
        return full_name
