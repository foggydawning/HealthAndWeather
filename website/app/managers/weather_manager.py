from app.managers.openweather_manager import OpenweatherManager
from app.models import Weather
from app.managers.magnetic_storms_manager import MagneticStormsManager

class WeatherManager:
    def __init__(self, lat: float, lon: float):
        self.lat = lat,
        self.lon = lon
        self.openweather_manager = OpenweatherManager(lat, lon)
        self.magnetic_storms_managers = MagneticStormsManager()

    def get_weather(self) -> Weather:
        temperature = self.openweather_manager.get_temperature()
        pressure = self.openweather_manager.get_pressure()
        magnetic_storms = self.magnetic_storms_managers.get_magnetic_storms()
        weather = Weather(
            pressure=pressure,
            temperature=temperature,
            magnetic_storms=magnetic_storms
        )
        return weather