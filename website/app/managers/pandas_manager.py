from pandas import read_sql_query
import sqlite3
import os.path
from  sqlite3.dbapi2 import Connection

from pandas.core.frame import DataFrame

class PandasManager:
    def __init__(self):
        self.connection: Connection = self.create_connection()

    def create_connection(self) -> Connection:
        BASE_DIR: str = os.path.dirname(os.path.abspath(__file__))
        db_path: bytes = os.path.join(BASE_DIR, "./../../app.db")
        connection: Connection = sqlite3.connect(db_path)
        return connection

    def get_data(self, user_id: int) -> DataFrame:
        query: str = f"""
        select well_being, is_head_hurts, is_high_pressure, pressure, magnetic_storms
        from "data" 
        where user_id={user_id}
        """
        data: DataFrame = read_sql_query(query, self.connection)
        return data
