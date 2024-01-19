"""Pokemon model"""
from pokemon_repository import PokemonRepository
from attack import Attack
from copy import deepcopy
# from user import User

class Pokemon():
    """This class represents a Pokemon
    
    Attributes:
        id (int): Pokemon's ID.
        name (str): Pokemon's name.
        type (str): Pokemon's type.
        hp (int): Pokemon's initial health points
        attacks (List[Attack]): Available attacks of the pokemon.
    """

    pokemon_list = []

    def __init__(self, id: int,  name: str, type: str, hp: int) -> None:
        self.id = id
        self.name = name
        self.type = type
        self.hp = hp
        self.attacks = []
        self.level = 0
        self.initial_hp = 0
    
    def __str__(self):
        return f"ID: {self.id} | Name: {self.name} | Type: {self.type} | HP: {self.hp} | level: {self.level}\n"
    
    def __repr__(self) -> str:
        return f"ID: {self.id} | Name: {self.name} | Type: {self.type} | HP: {self.hp} | level: {self.level}\n"


    # @staticmethod
    # def pokemon_definition(db_name: str, pokemon_id: str):
    #     """Returns data of the Pokemon according to the pokemon's ID inputed
        
    #     Args:
    #         db_name (str): name of the database.
    #         pokemon_id (str): pokemon's ID.
    #     """
    #     pokemon_data = PokemonRepository(db_name).get_pokemon_by_id(pokemon_id)
    #     return pokemon_data

    # @staticmethod
    # def show_pokemon_list(db_name: str):
    #     """Prints a list of the pokemon available in database.
        
    #     Args:
    #         db_name (str): name of the database.
    #     """
    #     pokemon_list = PokemonRepository(db_name).get_pokemons_list()
    #     print("Choose your Pokemon!")
    #     for pokemon in pokemon_list:
    #         print(f"{pokemon[0]}\t{pokemon[1]}")
    
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
    def all_pokemon_definition(db_name: str) -> None:
        """Stores all the attacks of the database in a list
        
        Args: 
            db_name (str): name of the database.
        """
        pokemons = PokemonRepository(db_name).get_pokemons()
        for pokemon in pokemons:
            Pokemon.pokemon_list.append(Pokemon(*pokemon))


    @staticmethod
    def set_pokemons_attacks(db_name: str):
        """Set the pokemon's attacks by the available attaks in database.
        
        Args:
            db_name (str): name of the database.
            pokemon_id (str): pokemon's ID.
        """

        pokemons = Pokemon.pokemon_list

        attack_list = Attack.attacks_list
        
        
        for pokemon in pokemons:

            pokemon_attacks_id = PokemonRepository(db_name).get_pokemon_attacks_by_id(pokemon.id)


            attacks =[]
            
            
            for pokemon_attack in pokemon_attacks_id:
                for attack in attack_list:

                    if attack.id == pokemon_attack[0] and attack.power != 0:
                        pokemon.attacks.append(deepcopy(attack))

                        pokemon.attacks[-1].level = pokemon_attack[1]
                        # print(pokemon.attacks[-1])

                        break
        # return attacks
                    
    def reset_hp(self):
        self.hp = self.initial_hp

    # @staticmethod
    # def set_pokemon_attacks(db_name: str, pokemon_id: str):
    #     """Set the pokemon's attacks by the available attaks in database.
        
    #     Args:
    #         db_name (str): name of the database.
    #         pokemon_id (str): pokemon's ID.
    #     """

    #     pokemon_attacks_id = PokemonRepository(db_name).get_pokemon_attacks_id(pokemon_id)

    #     attacks =[]
        
    #     for pokemon_attack in pokemon_attacks_id:
            
    #         for attack in Attack.attacks_list:

    #             if attack.id == pokemon_attack[0] and attack.power != 0:
    #                 attacks.append(deepcopy(attack))
    #                 attacks[-1].level = pokemon_attack[1]
    #                 break
    #     return attacks