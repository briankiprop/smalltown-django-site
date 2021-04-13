import random
from datetime import datetime
import requests
from django.shortcuts import render
from .models import notices, news_updates, events_model


# Create your views here.
def home_page(request):
    notices_list = notices.objects.all()[:10]
    notices_list = reversed(notices_list)
    news = news_updates.objects.all()[:5]
    list1 = list(news_updates.objects.all())
    if list1 != []:
        item = random.choice(list1)
    else:
        item = news_updates.objects.all()[:1]
    news = reversed(news)
    event = events_model.objects.all()

    try:
        url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=271d1234d3f497eed5b1d80a07b3fcd1'
        city = 'Eldama Ravine'
        r = requests.get(url.format(city)).json()
        now = datetime.now()
        city_weather = {
            'city': city,
            'time_now': now.strftime("%H:%M:%S"),
            'temperature': r["main"]["temp"],
            'description': r["weather"][0]["description"],
            'icon': r["weather"][0]["icon"],
        }
    except:
        city_weather = {
            'city': 'loading',
            'time_now': 'loading',
            'temperature': 'loading',
            'description': 'loading',
            'icon': 'loading',
        }
    context = {
        'notices': notices_list,
        'news': news,
        'item': item,
        'events': event,
        'city_weather': city_weather,
    }
    return render(request, 'home_page.html', context)


def download_notice(request):
    return render()


def about_us(request):
    context = {

    }
    return render(request, 'about_us.html', context)


def news(request):
    news_latest = news_updates.objects.all()[:5]
    news = news_updates.objects.all()
    context = {
        'news': news,
        'news_latest': news_latest,
    }
    return render(request, 'news.html', context)


def news_view(request, id):
    news_view = news_updates.objects.get(id=id)
    context = {
        'news_view': news_view,
    }
    return render(request, 'news_view.html', context)


def events(request):
    event = events_model.objects.all()
    context = {
        'events': event,
    }
    return render(request, 'events.html', context)


def event_view(request, id):
    event = events_model.objects.get(id=id)
    context = {
        'event': event,
    }
    return render(request, 'event_view.html', context)


def weather(request):
    try:
        url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=271d1234d3f497eed5b1d80a07b3fcd1'
        city = 'Voi'
        r = requests.get(url.format(city)).json()
        city_weather = {
            'city': city,
            'temperature': r["main"]["temp"],
            'description': r["weather"][0]["description"],
            'icon': r["weather"][0]["icon"],
        }

        context = {
            'city_weather': city_weather,
        }
    except:
        context = {

        }
    return render(request, 'weather.html', context)
