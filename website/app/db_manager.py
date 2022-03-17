from typing import Dict
from app.weather import Weather
from app.models import User, Data
from app import db

class DBManager:
    def save_data (
        self,
        user_id: int,
        time: str,
        user_answer: Dict[str, str],
        weather: Weather
    ):
        data = Data(
            user_id=user_id,
            time=time,
            well_being=user_answer.get("radio1"),
            is_head_hurts=user_answer.get("radio2"),
            is_high_pressure=user_answer.get("radio3"),
            temperature=weather.temperature,
            pressure=weather.pressure,
        )

        db.session.add(data)
        db.session.commit()

    def get_user(self, email: str) -> User:
        return User.query.filter_by(username=email).first()

    def save_user(self, email: str, password: str):
        user = User(username=email, email=password)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()