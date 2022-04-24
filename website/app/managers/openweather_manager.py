import requests

from app import Config

from typing import Optional

class OpenweatherManager:
    def __init__(self, lat: float, lon: float):
        self.api_key = Config.OPENWEATHER_API_KEY
        self.lat = lat,
        self.lon = lon

    def get_temperature(self) -> Optional[float]:
        request_string = "http://api.openweathermap.org/data/2.5/weather?}"
        try:
            res = requests.get(
                request_string, params={"lat": self.lat,
                                        "lon": self.lon,
                                        "appid": self.api_key}
            )
            data = res.json()
            temperature = float(data["main"]["temp"]) - 271.1
            return temperature
        except Exception as e:
            print("Exception (find):", e)
            return None

    def get_pressure(self) -> Optional[float]:
        request_string = "http://api.openweathermap.org/data/2.5/weather?}"
        try:
            res = requests.get(
                request_string, params={"lat": self.lat,
                                        "lon": self.lon,
                                        "appid": self.api_key}
            )
            data = res.json()
            pressure = float(data["main"]["pressure"]) / 10 * 7.500616827041698
            return pressure
        except Exception as e:
            print("Exception (find):", e)
            return None
