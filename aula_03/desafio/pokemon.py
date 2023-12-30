"""Pokemon model"""
from typing import List
from pokemon_repository import PokemonRepository
from attack import Attack
import copy

class Pokemon():
    """This class represents a Pokemon
    
    Attributes:
        id (int): Pokemon's ID.
        name (str): Pokemon's name.
        type (str): Pokemon's type.
        hp (int): Pokemon's initial health points
        attacks (List[Attack]): Available attacks of the pokemon.
    """
    def __init__(self, id: int,  name: str, type: str, hp: int) -> None:
        self.id = id
        self.name = name
        self.type = type
        self.hp = hp
        self.attacks = []
    
    def __str__(self):
        return f"ID: {self.id} | Name: {self.name} | Type: {self.type} | HP: {self.hp}"
    
    def __repr__(self) -> str:
        return f"ID: {self.id} | Name: {self.name} | Type: {self.type} | HP: {self.hp}"

    def is_pokemon_defeated(self):
        "Check if the pokemon is defeated during a battle."
        return self.hp <= 0

    def recieve_damage(self, damage: int):
        """Decrese the pokemon's hp during a battle, according the damage received.
        
        Args:
            damage (int): Power of the damage, corresponding the hp to be decreased.
        """
        self.hp -= damage

    @staticmethod
    def pokemon_definition(db_name: str, pokemon_id: int):
        """Returns data of the Pokemon according to the pokemon's ID inputed
        
        Args:
            db_name (str): name of the database.
            pokemon_id (int): pokemon's ID.
        """
        pokemon_data = PokemonRepository(db_name).get_pokemon_by_id(pokemon_id)
        return pokemon_data

    @staticmethod
    def set_pokemon_attacks(db_name: str, pokemon_id: str):
        """Set the pokemon's attacks by the available attaks in database.
        
        Args:
            db_name (str): name of the database.
            pokemon_id (int): pokemon's ID.
        """

        avaliable_attacks = []
        pokemon_attacks_id = PokemonRepository(db_name).get_pokemon_attacks_id(pokemon_id)

        for attack in Attack.attacks_list:
            if attack.id in pokemon_attacks_id:
                avaliable_attacks.append(copy.deepcopy(attack))
        return avaliable_attacks

    @staticmethod
    def show_pokemon_list(db_name: str):
        """Prints a list of the pokemon available in database.
        
        Args:
            db_name (str): name of the database.
        """
        pokemon_list = PokemonRepository(db_name).get_pokemons_list()
        print("Choose your Pokemon!")
        for pokemon in pokemon_list:
            print(f"{pokemon[0]}\t{pokemon[1]}")
    