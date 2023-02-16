from random import randint

from django.http import JsonResponse
from django.shortcuts import render, redirect

from .forms import TweetForm
from .models import Tweet


def home_view(request):
    return render(request, context={}, template_name='Tweet\\pages\\home.html')


def create_tweet(request):
    form = TweetForm(request.POST or None)
    next_url = request.POST.get("next")
    print(next_url)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        if next_url != None:
            return redirect(next_url)
        form = TweetForm()

    return render(request, context={'form': form}, template_name='Tweet\\pages\\create_tweet.html')


def tweets_list_view(request):
    objects = Tweet.objects.all()
    tweets_list = [{"id": tweet.id, "content": tweet.details, "count": randint(1, 100)} for tweet in objects]
    data = {
        "response": tweets_list
    }
    return JsonResponse(data, status=200)


def tweet_details_view(request, tweet_id):
    try:
        obj = Tweet.objects.get(id=tweet_id)
        data = {
            "id": obj.id,
            "content": obj.details
        }
        status = 200
    except:
        status = 404
        data = {
            "content": "Page Not Found"
        }

    return JsonResponse(data, status=status)
