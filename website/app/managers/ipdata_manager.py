from typing import Dict, Tuple

from ipdata import ipdata


class IpdataManager:
    def __init__(self, ip: str):
        self.api_key = "b28c6ec534269b0b98d175759a442f2f02e709871e8cd30c288ec911"
        self.response: Dict[str, int] or Dict[str, str or int] = self.get_response(ip=ip)

    def get_response(self, ip: str) -> Dict[str, int] or Dict[str, str or int]:
        ip_data = ipdata.IPData(self.api_key)
        response = ip_data.lookup(ip)
        return response

    def get_lat_and_lon(self) -> Tuple[float, float]:
        lat = float(self.response["latitude"])
        lon = float(self.response["longitude"])
        answer = (lat, lon)
        return answer

    def get_city(self) -> str:
        city = self.response["city"]
        return city

