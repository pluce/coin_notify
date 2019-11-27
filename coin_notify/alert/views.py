from django.shortcuts import render
from rest_framework import viewsets, generics
from rest_framework import permissions

from . import models
from . import serializers
from .permissions import IsOwnerOrReadOnly

class AlertView(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly
        , IsOwnerOrReadOnly]
    queryset = models.Alert.objects.all()
    serializer_class = serializers.AlertSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
