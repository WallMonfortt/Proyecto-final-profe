from http import server
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import User
from .serializers import UserSerializer, CreateUserSerializer
# Create your views here.

class UserViewSet(ModelViewSet):
    queryset  = User.objects.all().filter(is_superuser=False)
    serializer_class = UserSerializer

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CreateUserSerializer
        return UserSerializer