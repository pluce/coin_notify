from django.shortcuts import render
from rest_framework import viewsets, generics, status
from django.http import Http404
from rest_framework.response import Response

from . import models
from . import serializers

class UsersView(viewsets.ModelViewSet):
    queryset = models.CustomUser.objects.all()
    serializer_class = serializers.UserSerializer
