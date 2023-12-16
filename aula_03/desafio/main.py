from inicializador_db import DataBaseInitialize
from pokemon_repository import PokemonRepository
from random import randint

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
pokemon1 = input("Your Pókemon (by ID): ")
name_pokemon1 = PokemonRepository(database_name).get_pokemon_by_id(pokemon1)
print(f"Well done! Your pokemon is {name_pokemon1}.")

# Choose a random pokemon for the opponent
pokemon_amount = PokemonRepository(database_name).get_pokemon_amount()
pokemon2 = str(randint(1, pokemon_amount))
name_pokemon2 = PokemonRepository(database_name).get_pokemon_by_id(pokemon2)
input("Press any key to randomly choose your opponent.")
print(f"Be ready! Your opponent is a {name_pokemon2}!")