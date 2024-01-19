from db_inicializator import DataBaseInitialize
from battle import Battle
from attack import Attack
from user import User
from user_repository import UserRepository
from pokemon import Pokemon

def main_menu(user):
        
        while True:
            
            option = input("""
Welcome back! Choose any option according to the list bellow: 
1) Start a new battle!
2) Statistics (Stay tuned! Available in the next update
3) Logout\n""")

            match option:
                case "1":
                    Battle.start_battle(database_name, user)
                
                case "2":
                    input("Look out for this function in the upcoming release!")

                case "3":
                    break

                case _:
                    input("Invalid input! Press any key to return to the menu")


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
    Pokemon.all_pokemon_definition(database_name)
    Pokemon.set_pokemons_attacks(database_name)
    
    # Prints the login menu
    while True:
        option = input(
"""
Welcome back! Choose any option according to the list bellow: 
1) Login
2) Create new account
3) Exit game\n""")
        match option:

            case "1":

                user_input = input("Your user: ")
                user_id = UserRepository(database_name).get_user_id(user_input)
                current_user = User.set_user(database_name, user_id)
                
                input(f"\nWelcome back, {current_user.user}! Press any key to go to the main menu.")

                main_menu(current_user)

            case "2":

                new_user_id = UserRepository(database_name).create_new_user()
                current_user = User.set_user(database_name, new_user_id)

                input(f" Welcome, {current_user.user}! Press any key to go to the main menu")
                main_menu(current_user)

            case "3":
                input("See you soon! The game is now closing.")
                break

            case _:
                input("Invalid input! Press any key to return to the login menu.")
                continue