import sqlite3
from pokemon import Pokemon

class PokemonRepository():
    """Define a pokemon repository, with every query needed for the game
    
    Attributes:
        db_name (str): database's name.
    """

    def __init__(self, db_name: str):
        self.db_name = db_name
    
    #this method will be included in inicizalizador_db
    # def insert_pokemon_data(self, pokemon: Pokemon):
    #     """Insert content tho the pokemon table"""

    #     query = "INSERT INTO pokemon (name, type, hp) VALUES (?, ?, ?)"
        
