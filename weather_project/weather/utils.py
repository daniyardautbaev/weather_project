from django.utils.timezone import now
from datetime import timedelta
import requests
from django.conf import settings
def is_weather_data_outdated(weather_data):

    if not weather_data:
        return True
    return now() - weather_data.updated_at > timedelta(minutes=10)




def fetch_weather_from_api(city_name):

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={settings.OPENWEATHER_API_KEY}&units=metric"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return {
            "temperature": data["main"]["temp"],
            "description": data["weather"][0]["description"]
        }

    return None  #
