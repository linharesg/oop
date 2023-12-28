"""Pokemon model"""
from typing import List
from pokemon_repository import PokemonRepository
from attack import Attack

class Pokemon():
    """This class represents a Pokemon
    
    Attributes:
        id (int): Pokemon's ID.
        name (str): Pokemon's name.
        type (str): Pokemon's type.
        hp (int): Pokemon's initial health points
    """
    def __init__(self, id: int,  name: str, type: str, hp: int, atk1: Attack, atk2: Attack, atk3: Attack) -> None:
        self.id = id
        self.name = name
        self.type = type
        self.hp = hp
        # self.attacks = []
        self.atk1 = atk1
        self.atk2 = atk2
        self.atk3 = atk3
    
    def __str__(self):
        return f"ID: {self.id} | Name: {self.name} | Type: {self.type} | HP: {self.hp}, atk1: {self.atk1}, atk2: {self.atk2}, atk3: {self.atk3}"
    
    def __repr__(self) -> str:
        return f"ID: {self.id} | Name: {self.name} | Type: {self.type} | HP: {self.hp}, atk1: {self.atk1}, atk2: {self.atk2}, atk3: {self.atk3}"

    def is_pokemon_defeated(self):
        return self.hp <= 0

    def recieve_damage(self, damage):
        self.hp -= damage

    def pokemon_definition(db_name, pokemon_id):
        """Returns data of the Pokemon according to the pokemon's ID inputed"""
        pokemon_data = PokemonRepository(db_name).get_pokemon_by_id(pokemon_id)
        return pokemon_data

    # def set_pokemon_attacks(db_name, pokemon_id):
    #     avaliable_attacks = []
    #     pokemon_attacks_id = PokemonRepository(db_name).get_pokemon_attacks_id(pokemon_id)

    #     for attack in Attack.attacks_list:
    #         if attack.id in pokemon_attacks_id:
    #             avaliable_attacks.append(attack)
    #     return avaliable_attacks


    def set_pokemon_attacks(db_name, pokemon_id):
        avaliable_attacks = []
        pokemon_attacks_id = PokemonRepository(db_name).get_pokemon_attacks_id(pokemon_id)
        print(pokemon_attacks_id)
        for attack in Attack.attacks_list:
            if attack.id in pokemon_attacks_id:
                avaliable_attacks.append(attack)
        return avaliable_attacks


    def show_pokemon_list(db_name):
        pokemon_list = PokemonRepository(db_name).get_pokemons_list()
        print("Choose your Pokemon!")
        for pokemon in pokemon_list:
            print(f"{pokemon[0]}\t{pokemon[1]}")
    
    
    def increase_cooldown(attack: Attack):
        print(f"atual: {attack}")
        attack.current_cooldown = attack.cooldown + 1
        print(f"novo: {attack}")

    def decrease_cooldown(self):
        
        if self.atk1.current_cooldown > 0:
            self.atk1.current_cooldown -= 1
        if self.atk2.current_cooldown > 0:
            self.atk2.current_cooldown -= 1
        if self.atk3.current_cooldown > 0:
            self.atk3.current_cooldown -= 1
