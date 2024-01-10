from pokemon import Pokemon
from user_repository import UserRepository
from typing import List
from pokemon_repository import PokemonRepository
from pokemon_player import PokemonPlayer

class User():

    def __init__(self, id: str):
        self.id = id
        self.pokemons = []

    def __str__(self) -> str:
        return f"id: {self.id} | pokemons: {self.pokemons}"
    
    def __repr__(self) -> str:
        return f"id: {self.id} | pokemons: {self.pokemons}"

    def set_user_pokemons(self, db_name):
        user_pokemon_data = UserRepository(db_name).get_users_pokemon(self.id)
        for index, pokemon_data in enumerate(user_pokemon_data):
            self.pokemons.append(PokemonPlayer(*Pokemon.pokemon_definition(db_name, pokemon_data[1])))
            self.pokemons[index].level = pokemon_data[2]
            self.pokemons[index].attacks = PokemonPlayer.set_pokemon_attacks(db_name, pokemon_data[1])
        
    @staticmethod
    def validate_pokemon_input(self):
        """Verify if the pokemon's ID is valid"""
        
        while True:
            try:
                input_id = int(input("Choose you pokemon (by ID): "))
                for pokemon in self.pokemons:
                    if input_id == pokemon.id:
                        return pokemon
            except:
                continue



        