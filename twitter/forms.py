from django import forms
from django.forms import ModelForm, PasswordInput
from django.contrib.auth.models import User
from .models import Tweet, Message


class LoginForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        labels = {
            'username': 'Nazwa użytkownika',
            'password': 'Hasło'
        }
        widgets = {
            'password': PasswordInput(),
        }


class TweetForm(forms.Form):
    content = forms.CharField(label="Ćwierkaj")


class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ['content', 'recipient']
