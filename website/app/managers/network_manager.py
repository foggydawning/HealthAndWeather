import flask_login
from typing import Dict, Tuple
from flask import request
from app.weather import Weather
from app.managers.ipdata_manager import IpdataManager
from app.managers.openweather_manager import OpenweatherManager


class NetworkManager:
    def __init__(self):
        self.ipdata_manager = IpdataManager()
        self.openweather_manager = OpenweatherManager()

    def get_ip(self):
        return "178.68.70.67"

    def get_user_answer(self) -> Dict[str, str]:
        return request.form

    def get_user_id(self) -> int:
        return flask_login.current_user.id

    def get_user_username(self) -> str:
        return  flask_login.current_user.username

    def get_lat_and_lon(self) -> Tuple[float, float]:
        ip = self.get_ip()
        return self.ipdata_manager.get_lat_and_lon(ip)

    def get_weather(self) -> Weather:
        lat, lon = self.get_lat_and_lon()
        return self.openweather_manager.get_weather(lat, lon)

    def get_city(self) -> str:
        ip = self.get_ip()
        return self.ipdata_manager.get_city(ip)
