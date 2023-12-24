from inicializador_db import DataBaseInitialize
from battle import Battle
from attack import Attack

if __name__ == "__main__":

    #Defining the database name
    database_name = "pokemon_game.sqlite"

    # Creating the database tables (if it doenst exists)
    DataBaseInitialize.create_table(database_name)

    # Inserting default data if pokemon table is empty
    pokemons_inseridos = DataBaseInitialize.check_database(database_name)
    if pokemons_inseridos == None:
        DataBaseInitialize.insert_default_data(database_name)
        # Create objects for each Attack
    Attack.attacks_definition(database_name)
    
    while True:
        option = input(
"""
Welcome back! Choose any option according to the list bellow: 
1) Start a new battle!
2) Statistics
""")
        match option:

            case "1":
                Battle.start_battle(database_name)
            case _:
                input("Invalid input! The game is now closing")
                break