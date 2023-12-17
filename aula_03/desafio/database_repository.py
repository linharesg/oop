from abc import ABC
import sqlite3
from typing import Any

class DatabateRepository(ABC):
    """Databse repository to call the main queries"""

    def __init__(self, db_name, query):
        self.query = query
        self.db_name = db_name

    def run_query(self, query: str, *params: Any):
        connection = sqlite3.connect(self.db_name)
        cursor = connection.cursor()
        cursor.execute(query, params)
        connection.commit()
        connection.close()

    def run_script(self, query: str):
        connection = sqlite3.connect(self.db_name)
        cursor = connection.cursor()
        cursor.executescript(query)
        connection.commit()
        connection.close()

    def run_query_select_fetchone(self, query: str, *params: Any):
        connection = sqlite3.connect(self.db_name)
        cursor = connection.cursor()
        cursor.execute(query, params)
        connection.commit()
        rows = cursor.fetchone()
        connection.close()
        return rows
    
    def run_query_select_fetchall(self, query: str, *params: Any):
        connection = sqlite3.connect(self.db_name)
        cursor = connection.cursor()
        cursor.execute(query, params)
        connection.commit()
        rows = cursor.fetchall()
        connection.close()
        return rows