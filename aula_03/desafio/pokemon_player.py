from pokemon import Pokemon
from pokemon_repository import PokemonRepository
from attack import Attack
from copy import deepcopy
class PokemonPlayer(Pokemon):

    def __init__(self, id: int,  name: str, type: str, hp: int):
        
        super().__init__(id,  name, type, hp)
        self.initial_hp = self.hp
        self.level = 0
        self.attacks = []

    def __str__(self):
        return f"ID: {self.id} | Name: {self.name} | Type: {self.type} | HP: {self.hp} | current hp: {self.initial_hp} | level: {self.level} \n Attacks : {self.attacks}"
    
    def __repr__(self) -> str:
        return f"ID: {self.id} | Name: {self.name} | Type: {self.type} | HP: {self.hp} | current hp: {self.initial_hp} | level: {self.level}"
    
    
    def reset_hp(self):
        "Reset the health points after finishing a battle"

        self.hp = self.initial_hp
    
    @staticmethod
    def set_pokemon_attacks(db_name: str, pokemon_id: str):
        """Set the pokemon's attacks by the available attaks in database.
        
        Args:
            db_name (str): name of the database.
            pokemon_id (str): pokemon's ID.
        """

        pokemon_attacks_id = PokemonRepository(db_name).get_pokemon_attacks_id(pokemon_id)

        attacks =[]
        
        for index, pokemon_attack in enumerate(pokemon_attacks_id):
            
            for attack in Attack.attacks_list:
                # print(attack)
                # print(index)
                # print(pokemon_attack)
                if attack.id == pokemon_attack[0] and attack.power != 0:
                    attacks.append(deepcopy(attack))
                    attacks[-1].level = pokemon_attack[1]
                    break
        return attacks