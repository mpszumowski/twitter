from django.contrib.auth.mixins import (LoginRequiredMixin,
                                        PermissionRequiredMixin)
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic.edit import CreateView

from .models import Tweet, Message
from .forms import MessageForm, TweetForm


class MainView(LoginRequiredMixin, View):

    def get(self, request):
        form = TweetForm()
        tweets = Tweet.objects.order_by('-creation_date')
        users = User.objects.all()
        return render(request, 'main.html', {'tweets': tweets,
                                             'users': users,
                                             'form': form})

    def post(self, request):
        form = TweetForm(request.POST)
        if form.is_valid():
            content = form.cleaned_data['content']
            current_user = request.user
            Tweet.objects.create(content=content, author=current_user)
            return redirect('main')


class UserView(LoginRequiredMixin, View):

    def get(self, request, user_id):
        user = User.objects.get(pk=int(user_id))
        user_tweets = Tweet.objects.filter(author=user)
        return render(request, 'user_front.html', {'user': user,
                                                   'tweets': user_tweets})


class TweetView(LoginRequiredMixin, View):

    def get(self, request, user_id, tweet_id):
        user = User.objects.get(pk=int(user_id))
        tweet = Tweet.objects.get(pk=int(tweet_id))
        return render(request, 'tweet_view.html', {'user': user,
                                                   'tweet': tweet})


class MessagesView(LoginRequiredMixin, View):

    def get(self, request, user_id, tweet_id):
        user = User.objects.get(pk=int(user_id))
        messages = Message.objects.filter(Q(author=user) | Q(recipient=user))
        return render(request, 'tweet_view.html', {'user': user,
                                                   'messages': messages})


class CreateUserView(CreateView):
    model = User
    fields = ['username', 'password', 'first_name', 'last_name', 'email']



