import pandas as pd
import sqlite3
import os.path

class PandasManager:
    def __init__(self):
        self.connection = None
        self.create_connection()

    def create_connection(self):
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.join(BASE_DIR, "./../../app.db")
        self.connection = sqlite3.connect(db_path)

    def get_data(self, user_id: int):
        request_string = f'select well_being, is_head_hurts, is_high_pressure, pressure from "data" where user_id = {user_id}'
        data = pd.read_sql_query(request_string, self.connection)
        return data