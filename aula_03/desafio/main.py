from inicializador_db import DataBaseInitialize

database_name = "pokemon_game.db"
DataBaseInitialize.create_table(database_name)
pokemons_inseridos = DataBaseInitialize.check_database(database_name)
if pokemons_inseridos == None:
    DataBaseInitialize.insert_default_data(database_name)

while True:
    #Escolher o pokemon
    pass