import sqlite3
from pokemon import Pokemon
from typing import List
from database_repository import DatabateRepository
class PokemonRepository(DatabateRepository):
    """Define a pokemon repository, with every query needed for the game
    
    Attributes:
        db_name (str): database's name.
    """

    def __init__(self, db_name: str):
        self.db_name = db_name
    
    def get_pokemons_list(self) -> List[Pokemon]:
        """Get ID and name of all the pokemons"""
        query = "SELECT id, name FROM pokemons"
        pokemon_list = super().run_query_select_fetchall(query)
        return pokemon_list

    def get_pokemon_by_id(self, id: int) -> str:
        "Get the pokemon name by its ID"
        query = "SELECT * FROM pokemons WHERE id = ?"
        pokemon = super().run_query_select_fetchone(query, id)
        return pokemon
    
    def get_pokemon_amount(self):
        """Get the amount of Pokemon in database"""
        query = "SELECT COUNT(*) FROM pokemons"
        pokemon_amount = super().run_query_select_fetchone(query)[0]
        return pokemon_amount

    def get_pokemon_attacks (self, pokemon1: Pokemon):
        query = """
            SELECT attacks.* 
            FROM attacks
            INNER JOIN pokemon_attacks on (pokemon_attacks.attack_id = attacks.id)
            WHERE pokemon_id = ?
            ;"""
        pokemon_attacks = super().run_query_select_fetchall(query, str(pokemon1.id))
        return pokemon_attacks

