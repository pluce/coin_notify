# Generated by Django 2.2.7 on 2019-11-29 01:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alert', '0003_auto_20191126_1719'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alert',
            name='bigger_than',
            field=models.BooleanField(default='1'),
        ),
    ]
