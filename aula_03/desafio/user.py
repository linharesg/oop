from pokemon import Pokemon
from user_repository import UserRepository
from copy import deepcopy

class User():

    def __init__(self, id: str = "", user: str = "", email: str = ""):
        self.id = id
        self.user = user
        self.email = email
        self.pokemons = []

    def __str__(self) -> str:
        return f"id: {self.id} | pokemons: {self.pokemons}"
    
    def __repr__(self) -> str:
        return f"id: {self.id} | pokemons: {self.pokemons}"


    def set_user_pokemons(self, db_name):

        user_pokemon_data = UserRepository(db_name).get_users_pokemon(self.id)
        pokemon_list = Pokemon.pokemon_list
        for pokemon_data in user_pokemon_data:
            for pokemon in pokemon_list:
                if pokemon.id == pokemon_data[1]:
                    self.pokemons.append(deepcopy(pokemon))
                    self.pokemons[-1].level = pokemon_data[2]
                    self.pokemons[-1].initial_hp = pokemon.hp
        
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

    def set_user(db_name, user_id):
        
        user_data = UserRepository(db_name).get_user_data(user_id)
        current_user = User(*user_data)
        User.set_user_pokemons(current_user, db_name)
        
        return current_user