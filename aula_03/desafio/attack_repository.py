from pokemon import Pokemon
import sqlite3


class AttackRepository():

    def __init__(self, db_name):
        self.db_name = db_name

    #This method was transfered to PokemonRepository
    # def get_pokemon_attacks (self, pokemon: Pokemon):
    #     query = """
    #         SELECT attacks.* 
    #         FROM attacks
    #         INNER JOIN pokemon_attacks on (pokemon_attacks.attack_id = attacks.id)
    #         WHERE pokemon_id = ?
    #         ;"""
    #     connection = sqlite3.connect(self.db_name)
    #     cursor = connection.cursor()
    #     cursor.execute(query, str(pokemon.id))
    #     rows = cursor.fetchall()
    #     connection.close
    #     return rows
    
