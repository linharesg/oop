from db_inicializator import DataBaseInitialize
from battle import Battle
from attack import Attack
from user import User
from user_repository import UserRepository

if __name__ == "__main__":

    #Defining the database name
    database_name = "pokemon_game.sqlite"

    # Creating the database tables (if it doenst exists)
    DataBaseInitialize.create_table(database_name)

    # Inserting default data if there is no data
    pokemons_inseridos = DataBaseInitialize.check_database(database_name)
    if pokemons_inseridos == None:
        DataBaseInitialize.insert_default_data(database_name)

    # Create objects for each Attack
    Attack.attacks_definition(database_name)
    
    # Start the game by printing the initial Menu, where the user can choose the options.
    while True:
        option = input(
"""
Welcome back! Choose any option according to the list bellow: 
1) Start a new battle!
2) Statistics (Stay tuned! Available in the next update)
3) Login

Press any other key to exit the game.
""")
        match option:

            case "1":
                Battle.start_battle(database_name, current_user)
            case "2":
                input("Look out for this function in the upcoming release!")
            case "3":
                # user_input = input("Input your user: ")
                user_input = "gabriel.sl"
                user_id = UserRepository(database_name).get_user_id(user_input)
                current_user = User(user_id)
                
                User.set_user_pokemons(current_user, database_name)
            case _:
                input("See you soon! The game is now closing.")
                break