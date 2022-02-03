import re
from django.shortcuts import render

from .serializers import NewsletterSerializer, CreateNewsletterSerializer,NewsletterNoAdminSerializer
from .models import Newsletter
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework import status
from rest_framework.response import Response
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated, IsAdminUser

# Create your views here.

class NewsLetterViewSet(ModelViewSet):
    queryset = Newsletter.objects.all()
    serializer_class = NewsletterSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['id', 'tags']
    search_fields = ['=name']
    ordering_fields = ['name', 'id']

    def get_serializer_class(self):
        if self.action == 'create' or self.action == 'update':
            return CreateNewsletterSerializer
        else:
            return NewsletterSerializer

    def get_queryset(self):
        filter = self.request.query_params.get('tag')
        if filter:
            newsletters = self.queryset.filter(
                tags__slug__contains=filter
            )
            return newsletters
        return self.queryset

    @action(methods=["PATCH"], detail=True)
    def vote(self, request, pk=None):
        user = request.user
        id = user.id
        newslettter = self.get_object()
        votes = newslettter.voters.all()
        if user in votes:
            newslettter.voters.remove(id)
            return Response(status=status.HTTP_200_OK, data={
            "vote": "The vote was removed"
        })

        newslettter.voters.add(id)
        return Response(status=status.HTTP_200_OK, data={
            "vote": "The vote was add"
        })

    
    @action(methods=["PATCH"], detail=True)
    def subscribe(self, request, pk=None):
        user = request.user
        id = user.id
        newslettter = self.get_object()
        users = newslettter.members.all()
        if newslettter.target >=  10:
            if user in users:
                newslettter.members.remove(id)
                return Response(status=status.HTTP_200_OK, data={
                    "subscibre": "The subscribe was removed"
                })
            newslettter.members.add(id)
            return Response(status=status.HTTP_200_OK, data={
                    "subscibre": "The subscribe was add"
                })
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED, data={
            "message": "El boletin no ha alcanzado los votos suicientes"
        })

    # delete method for admin
    @action(methods=["DELETE"], detail=True)
    def delete(self, request, pk=None):
        user = request.user
        if user.is_superuser or user.is_admin:
            newslettter = self.get_object()
            newslettter.delete()
            return Response(status=status.HTTP_200_OK, data={
                "message": "The newsletter was deleted"
            })
        return Response(status=status.HTTP_401_UNAUTHORIZED, data={
            "message": "You are not authorized to delete this newsletter"
        })

    # update method for admin and author
    def update(self, request, *args, **kwargs):
        user = request.user
        if user.is_superuser or user.is_admin:
            return super().update(request, *args, **kwargs)
        elif user.is_author:
            newslettter = self.get_object()
            if newslettter.author == user:
                return super().update(request, *args, **kwargs)
        return Response(status=status.HTTP_401_UNAUTHORIZED, data={
            "message": "You are not authorized to update this newsletter"
        })

