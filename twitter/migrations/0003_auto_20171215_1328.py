# Generated by Django 2.0 on 2017-12-15 13:28

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitter', '0002_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='author',
            field=models.OneToOneField(on_delete=False, to=settings.AUTH_USER_MODEL),
        ),
    ]
