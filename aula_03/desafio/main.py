from inicializador_db import DataBaseInitialize
from pokemon_repository import PokemonRepository
from random import randint
from pokemon import Pokemon

database_name = "pokemon_game.db"

# Creating the database tables
DataBaseInitialize.create_table(database_name)

# Inserting default data if pokemon table is empty
pokemons_inseridos = DataBaseInitialize.check_database(database_name)
if pokemons_inseridos == None:
    DataBaseInitialize.insert_default_data(database_name)

# Choose your pokemon
lista_pokemons = PokemonRepository(database_name).get_pokemons_list()
print("Choose your Pokémon!")
for pokemon in lista_pokemons:
    print(f"{pokemon[0]}\t{pokemon[1]}")
input_pokemon1 = input("Your Pókemon (by ID): ")
pokemon1_data = PokemonRepository(database_name).get_pokemon_by_id(input_pokemon1)
pokemon1 = Pokemon(*pokemon1_data)

print(f"Well done! Your pokemon is {pokemon1.name}.")

# Choose a random pokemon for the opponent
pokemon_amount = PokemonRepository(database_name).get_pokemon_amount()
random_pokemon2 = str(randint(1, pokemon_amount))
pokemon2_data = PokemonRepository(database_name).get_pokemon_by_id(random_pokemon2)
pokemon2 = Pokemon(*pokemon2_data)
input("Press any key to randomly choose your opponent.")
print(f"Be ready, your opponent is a {pokemon2.name}!")

