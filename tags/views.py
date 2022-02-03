from django.shortcuts import render
from .serializers import TagSerializer
from .models import Tag
# Create your views here.
from rest_framework.viewsets import ModelViewSet

class TagViewSet(ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

        