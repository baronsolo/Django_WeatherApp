from django.shortcuts import render
import requests
from .models import City
from .forms import CityForm
from django.urls import reverse
from django.http import HttpResponseRedirect


def index(request):
    appid = '3baec9b4db41557a92b87ea88a293d54'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + appid
    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()
    form = CityForm()
    cities = City.objects.all()
    all_cities = []
    for city in cities:
        res = requests.get(url.format(city.name)).json()
        city_info = {
            'id': city.id,
            'city': city.name,
            'temp': res["main"]["temp"],
            'feels_like': res["main"]["feels_like"],
            'pressure': res["main"]["pressure"],
            'visibility': res["visibility"],
            'wind_speed': res["wind"]["speed"],
            'deg': res["wind"]["deg"],
            'clouds': res["clouds"]["all"],
            'icon': res["weather"][0]["icon"]
        }
        all_cities.append(city_info)
    context = {'all_info': all_cities, 'form': form}
    return render(request, 'weather/index.html', context)


def delete(request, id):
    city = City.objects.get(id=id)
    city.delete()
    return HttpResponseRedirect(reverse('index'))


def info(request):
    appid = '3baec9b4db41557a92b87ea88a293d54'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + appid
    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()
    form = CityForm()
    cities = City.objects.all()
    all_cities = []
    for city in cities:
        res = requests.get(url.format(city.name)).json()
        city_info = {
            'id': city.id,
            'city': city.name,
            'temp': res["main"]["temp"],
            'feels_like': res["main"]["feels_like"],
            'pressure': res["main"]["pressure"],
            'visibility': res["visibility"],
            'wind_speed': res["wind"]["speed"],
            'deg': res["wind"]["deg"],
            'clouds': res["clouds"]["all"],
            'icon': res["weather"][0]["icon"]
        }
        all_cities.append(city_info)
    context = {'all_info': all_cities, 'form': form}
    return render(request, 'weather/info.html', context)


def about(request):
    return render(request, 'weather/about.html')
