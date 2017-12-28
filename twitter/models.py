from django.db import models
from django.contrib.auth.models import User


class Tweet(models.Model):
    content = models.CharField(max_length=140)
    creation_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)


class Message(models.Model):
    content = models.TextField()
    creation_date = models.DateField(auto_now_add=True)
    author = models.ForeignKey(User,
                               on_delete=False,
                               related_name="message_author")
    recipient = models.ForeignKey(User,
                                  on_delete=False,
                                  related_name="message_recipient")
    seen = models.BooleanField(default=False)