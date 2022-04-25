import time
from typing import Optional

from requests import get


class MagneticStormsManager:
    def __init__(self):
        self.api_key = "Hdd633EbwbQ8elJKig6Ub8AJHhXS5MYKBev6yKdS"

    def get_magnetic_storms(self) -> Optional[int]:
        request_string = "https://api.nasa.gov/DONKI/GST?"
        try:
            startDate = time.strftime("%Y-%m-%d")
            res = get(
                request_string,
                params={
                    "startDate": startDate,
                    "location": "Earth",
                    "catalog": "SWRC_CATALOG",
                    "api_key": self.api_key,
                },
            )
            if not res.content:
                return 0
            data = res.json()
            value = int(data[-1]["allKpIndex"][-1]["kpIndex"])
            return value
        except Exception as e:
            print(f"Ошибка при получении магнитных бурь {e}")
            return None
