# import os
# import urllib.request
# from datetime import datetime
#
# import nasapy
#
# # Initialize Nasa class by creating an object:
# k = "Hdd633EbwbQ8elJKig6Ub8AJHhXS5MYKBev6yKdS"
# nasa = nasapy.Nasa(key=k)
# # Get today’s date in YYYY-MM-DD format:
# d = datetime.today().strftime("%Y-%m-%d")

from random import randint


class MagneticStormsManager:
    def __init__(self):
        self.api_key = "Hdd633EbwbQ8elJKig6Ub8AJHhXS5MYKBev6yKdS"

    def get_magnetic_storms(self) -> int:
        return randint(3, 6)
