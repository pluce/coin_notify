# Generated by Django 2.2.7 on 2019-11-26 17:09

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('alert', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Alert',
            new_name='AlertView',
        ),
    ]
