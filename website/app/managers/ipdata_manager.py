from typing import Tuple

from ipdata import ipdata

from config import Config


class IpdataManager:
    def __init__(self):
        self.api_key = Config.IPDATA_API_KEY

    def get_response(self, ip: str) -> dict[str, int] | dict[str, str | int]:
        ip_data = ipdata.IPData(self.api_key)
        response = ip_data.lookup(ip)
        return response

    def get_lat_and_lon(self, ip: str) -> Tuple[float, float]:
        response = self.get_response(ip)
        lat = float(response["latitude"])
        lon = float(response["longitude"])
        answer = (lat, lon)
        return answer

    def get_city(self, ip: str) -> str:
        response = self.get_response(ip)
        city = response["city"]
        return city
