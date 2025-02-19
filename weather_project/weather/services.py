import requests
from urllib.parse import quote  # Для кодирования города в URL

API_KEY = '0006ef2e7c518c7926e0ecb960a6bf7a'


def get_weather_data(city):
    city_encoded = quote(city)  # Кодируем имя города
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city_encoded},KZ&appid=0006ef2e7c518c7926e0ecb960a6bf7a&units=metric'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return {
            'temperature': data['main']['temp'],
            'description': data['weather'][0]['description']
        }
    else:
        return {'error': response.json().get('message', 'Unknown error')}
