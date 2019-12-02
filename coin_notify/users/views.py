from django.shortcuts import render
from rest_framework import viewsets, generics, status, authentication, permissions
from django.http import Http404
from rest_framework.response import Response

from . import models
from . import serializers
from rest_framework.views import APIView

class UsersView(viewsets.ModelViewSet):
    queryset = models.CustomUser.objects.all()
    serializer_class = serializers.UserSerializer
