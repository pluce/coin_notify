from django.db import models
from users.models import CustomUser

# Create your models here.

AVAILABLE_CURRENCY = [
    ('BTC', 'bitcoins'),
]

class Alert(models.Model):
    """
    bigger_than : tell if the alert is for BTC rate bigger or smaller than alert value
                  if true alert will be send if BTC rate is bigger than alert value
    """
    created = models.DateTimeField(auto_now=True)
    currency = models.CharField(choices=AVAILABLE_CURRENCY, default='BTC', max_length=255)
    value = models.IntegerField(null=False)
    bigger_than = models.BooleanField(default='1')
    owner = models.ForeignKey(CustomUser, related_name='alert', on_delete=models.CASCADE)

    class Meta:
        ordering = ['created']
