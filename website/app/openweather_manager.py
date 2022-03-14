import requests

from config import Config
from app.weather import Weather


class OpenweatherManager:
    def __init__(self):
        self.api_key = Config.OPENWEATHER_API_KEY

    def get_weather(self, lat: float, lon: float) -> Weather:
        request_string = "http://api.openweathermap.org/data/2.5/weather?}"
        try:
            res = requests.get(request_string,
                               params={'lat': lat, 'lon': lon, 'appid': self.api_key})
            data = res.json()
            temperature = float(data["main"]["temp"]) - 271.1
            pressure = float(data["main"]["pressure"])
            weather = Weather(pressure=pressure, temperature=temperature)
            return  weather
        except Exception as e:
            print("Exception (find):", e)
            return Weather(pressure = None, temperature=None)
