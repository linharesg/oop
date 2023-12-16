import sqlite3
from pokemon import Pokemon
from typing import List

class PokemonRepository():
    """Define a pokemon repository, with every query needed for the game
    
    Attributes:
        db_name (str): database's name.
    """

    def __init__(self, db_name: str):
        self.db_name = db_name
    
    def get_pokemons_list(self) -> List[Pokemon]:
        """Obtém a ID e o nome de todos os Pokemons"""
        query = "SELECT id, name FROM pokemons"
        connection = sqlite3.connect(self.db_name)
        cursor = connection.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        connection.close()
        return rows
        
