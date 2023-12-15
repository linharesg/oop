from inicializador_db import DataBaseInitialize

database_name = "pokemon_game.db"
DataBaseInitialize.create_table(database_name)
DataBaseInitialize.insert_default_data(database_name)
