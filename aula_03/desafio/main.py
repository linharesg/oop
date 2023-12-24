from inicializador_db import DataBaseInitialize
from pokemon_repository import PokemonRepository
from random import randint
from pokemon import Pokemon
from battle import Battle
from battle_repository import BattleRepository
from attack import Attack

if __name__ == "__main__":

    
    database_name = "pokemon_game.sqlite"

    # Creating the database tables
    DataBaseInitialize.create_table(database_name)

    # Inserting default data if pokemon table is empty
    pokemons_inseridos = DataBaseInitialize.check_database(database_name)
    if pokemons_inseridos == None:
        DataBaseInitialize.insert_default_data(database_name)

    # Show pokemon list to choose
    pokemon_list = PokemonRepository(database_name).get_pokemons_list()
    print("Choose your Pokemon!")
    for pokemon in pokemon_list:
        print(f"{pokemon[0]}\t{pokemon[1]}")

    # Input pokemon
    input_pokemon1 = input("Your Pokemon (by ID): ")
    
    # Create objects for each Attack
    Attack.attacks_definition(database_name)

    # Defining pokemon1
    pokemon1 = Pokemon(*Pokemon.pokemon_definition(database_name, input_pokemon1))
    pokemon1.attacks = Pokemon.set_pokemon_attacks(database_name, input_pokemon1)
    print(f"Well done! Your pokemon is {pokemon1.name}.")

    # Choose a random pokemon for the opponent
    pokemon_amount = PokemonRepository(database_name).get_pokemon_amount()
    random_pokemon2 = str(randint(1, pokemon_amount))
    # Defining pokemon2 attributes
    pokemon2 = Pokemon(*Pokemon.pokemon_definition(database_name, random_pokemon2))
    pokemon2.attacks = Pokemon.set_pokemon_attacks(database_name, random_pokemon2)

    # Revealing the opponent's pokemon
    input("Press any key to randomly choose your opponent.\n")
    print(f"Be ready, your opponent is a {pokemon2.name}!")

    current_battle = Battle(pokemon1, pokemon2)
    current_battle.start_battle()

    BattleRepository(database_name).load_battle_results(current_battle)