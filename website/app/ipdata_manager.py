from ipdata import ipdata
from config import Config


class IpdataManager:
    def __init__(self):
        self.api_key = Config.IPDATA_API_KEY

    def get_lat_and_lon(self, ip: str) -> (float, float):
        ip_data = ipdata.IPData(self.api_key)
        response = ip_data.lookup(ip)
        lat = float(response["latitude"])
        lon = float(response["longitude"])
        answer = (lat, lon)
        return  answer



