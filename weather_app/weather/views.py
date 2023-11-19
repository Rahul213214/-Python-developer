from django.shortcuts import render
# from .utils import get_weather
# weather/views.py
import requests
from django import forms


class CityForm(forms.Form):
    city = forms.CharField(label='Enter city name', max_length=100)

def get_weather(city):
    api_key = 'a8c991141c63fbe2cf9b00fa064b9de2'  # Your OpenWeatherMap API key
    base_url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    response = requests.get(base_url)
    if response.status_code == 200:
        data = response.json()
        weather = {
            'city': data['name'],
            'temperature': data['main']['temp'],
            'description': data['weather'][0]['description'],
            'icon': data['weather'][0]['icon'],
            'humidity': data['main']['humidity'],
            'wind_speed': data['wind']['speed']
        }
        return weather
    else:
        return None


def weather(request):
    form = CityForm()
    weather_data = None

    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            city = form.cleaned_data['city']
            weather_data = get_weather(city)

    context = {'form': form, 'weather_data': weather_data}
    return render(request, 'weather/weather.html', context)
