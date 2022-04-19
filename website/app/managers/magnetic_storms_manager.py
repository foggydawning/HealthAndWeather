import nasapy
import os
from datetime import datetime
import urllib.request

#Initialize Nasa class by creating an object:
k = "Hdd633EbwbQ8elJKig6Ub8AJHhXS5MYKBev6yKdS"
nasa = nasapy.Nasa(key=k)
#Get today’s date in YYYY-MM-DD format:
d = datetime.today().strftime('%Y-%m-%d')
