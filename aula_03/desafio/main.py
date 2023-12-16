from inicializador_db import DataBaseInitialize
from pokemon_repository import PokemonRepository

database_name = "pokemon_game.db"

# Criando as tabelas do banco de dados
DataBaseInitialize.create_table(database_name)
pokemons_inseridos = DataBaseInitialize.check_database(database_name)

# Inserindo dados caso a tabela pokemons esteja vazia
if pokemons_inseridos == None:
    DataBaseInitialize.insert_default_data(database_name)

#Exibir lista de pokemons para escolher
lista_pokemons = PokemonRepository(database_name).get_pokemons_list()
print("Escolha o seu Pokémon!")
for pokemon in lista_pokemons:
    print(f"{pokemon[0]}\t{pokemon[1]}")

