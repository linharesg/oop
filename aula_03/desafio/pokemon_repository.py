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
        """Get ID and name of all the pokemons"""
        query = "SELECT id, name FROM pokemons"
        connection = sqlite3.connect(self.db_name)
        cursor = connection.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        connection.close()
        return rows

    def get_pokemon_by_id(self, id: int) -> str:
        "Get the pokemon name by its ID"
        query = "SELECT * FROM pokemons WHERE id = ?"
        connection = sqlite3.connect(self.db_name)
        cursor = connection.cursor()
        cursor.execute(query, id)
        pokemon = cursor.fetchone()
        connection.close()
        return pokemon

    def get_pokemon_amount(self):
        """Get the amount of Pokemon in database"""
        query = "SELECT COUNT(*) FROM pokemons"
        connection = sqlite3.connect(self.db_name)
        cursor = connection.cursor()
        cursor.execute(query)
        pokemon_amount = cursor.fetchone()[0]
        connection.close()
        return pokemon_amount

    def get_pokemon_attacks (self, pokemon: Pokemon):
        query = """
            SELECT attacks.* 
            FROM attacks
            INNER JOIN pokemon_attacks on (pokemon_attacks.attack_id = attacks.id)
            WHERE pokemon_id = ?
            ;"""
        connection = sqlite3.connect(self.db_name)
        cursor = connection.cursor()
        cursor.execute(query, str(pokemon.id))
        rows = cursor.fetchall()
        connection.close
        return rows

