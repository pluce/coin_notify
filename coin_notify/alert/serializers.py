from rest_framework import serializers
from . import models

class AlertSerializer(serializers.ModelSerializer):
    class Meta:
        owner = serializers.ReadOnlyField(source='owner.username')
        model = models.Alert
        fields = ('id', 'currency', 'value', 'bigger_than')
