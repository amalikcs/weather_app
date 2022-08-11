import requests

data = {
    'appid': 'b60aba54ebb9059c59b9a55c2657518b',
    'q': 'dehradun',
}
print(data['appid'])
url = "https://api.openweathermap.org/data/2.5/weather"

response = requests.get(url, params=data)


