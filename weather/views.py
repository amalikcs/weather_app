from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
import requests
from .models import Weather


def home(request):
    return render(request, 'weather/base.html')


@login_required()
def weather(request):
    # if request.method is not 'POST': return HttpResponse("Method not allowed")
    city = request.POST.get('search') if 'search' in request.POST else None
    user = request.user

    if city: Weather.objects.create(city_name=city, user=user)
    param = {
        'appid': 'b60aba54ebb9059c59b9a55c2657518b',
        'q': f"{city}"
    }
    url = 'https://api.openweathermap.org/data/2.5/weather'
    response = requests.get(url, params=param)
    print(response.status_code)
    list_of_data = response.json() if response.status_code == 200 else []
    print(list_of_data)
    if list_of_data:
        display_data = {
            "country_name": list_of_data['sys']['country'],
            "city_name": list_of_data['name'],
            "temp": list_of_data['main']['temp'],
            "kind_of_weather": list_of_data['weather'][0]['main'],
            "icon": list_of_data['weather'][0]['icon']
        }
        print("displaying data", display_data)
    else:
        display_data = {'status': response.status_code, 'message': response.json()}
        print(display_data)
    display_data.update({'recently_search_cites': Weather.objects.filter(user=user).order_by('created_at')[:10]})
    return render(request, 'weather/weather_home.html', display_data)

