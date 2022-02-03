from ast import Mod
from django.db import router
from rest_framework.serializers import ModelSerializer
from .models import User

class CreateUserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('password', 'username', 'first_name', 'last_name', 'cellphone', 'is_admin', 'email')

    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            cellphone = validated_data["cellphone"],
            is_admin = validated_data["is_admin"],
            is_active=True
        )
        user.set_password(validated_data["password"])
        user.save()
        return user


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name',
        'last_login', 'date_joined'
        )