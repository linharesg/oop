from abc import ABC
import sqlite3
from typing import Any

class DatabateRepository(ABC):
    """Database repository to call the main queries
    
    Attributes:
        db_name (str): name of the database.
        query (str): query to e executed in the sql.
    """

    def __init__(self, db_name: str, query: str):
        self.query = query
        self.db_name = db_name

    def run_query(self, query: str, *params: Any):
        """Run any query according its query.
        
        Args:
            query (str): query to e executed in the sql.
            *params (Any): Arguments used along the query.
        """
        connection = sqlite3.connect(self.db_name)
        cursor = connection.cursor()
        cursor.execute(query, params)
        connection.commit()
        connection.close()

    def run_query_select_fetchone(self, query: str, *params: Any):
        """Run any query, returning the first result of the select query in a single row
        
        Args:
            query (str): query to e executed in the sql.
            *params (Any): Arguments used along the query.
        """

        connection = sqlite3.connect(self.db_name)
        cursor = connection.cursor()
        cursor.execute(query, params)
        connection.commit()
        row = cursor.fetchone()
        connection.close()
        return row
    
    def run_query_select_fetchall(self, query: str, *params: Any):
        """Run any query, returning the result of the select query in amultiple rows.
        
        Args:
            query (str): query to e executed in the sql.
            *params (Any): Arguments used along the query.
        """
        connection = sqlite3.connect(self.db_name)
        cursor = connection.cursor()
        cursor.execute(query, params)
        connection.commit()
        rows = cursor.fetchall()
        connection.close()
        return rows

    def check_database(db_name: str):
        """Check if there is some data in the tables of the game's database.
        
        Args:
            db_name (str): database's name.
        """
        connection = sqlite3.connect(db_name)
        cursor = connection.cursor()
        cursor.execute("""
        SELECT MIN(id) FROM pokemons
        """)
        row = cursor.fetchone()
        connection.close
        return row[0]