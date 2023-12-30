from database_repository import DatabateRepository

class PokemonRepository(DatabateRepository):
    """Define a pokemon repository, with every query needed for the game
    
    Attributes:
        db_name (str): database's name.
    """

    def __init__(self, db_name: str):
        self.db_name = db_name
    
    def get_pokemons_list(self):
        "Get the list of pokemons in the database"
        
        """Get ID and name of all the pokemons"""
        query = "SELECT id, name FROM pokemons ORDER BY id"
        pokemon_list = super().run_query_select_fetchall(query)
        return pokemon_list

    def get_pokemons_id_list(self):
        "Get the list of pokemons ID in the database"
        
        """Get ID and name of all the pokemons"""
        query = "SELECT id FROM pokemons ORDER BY id"
        pokemon_id_list = super().run_query_select_fetchall(query)
        return [row[0] for row in pokemon_id_list]

    def get_pokemon_by_id(self, id: int) -> str:
        """Get the data of a pokemon by its ID
        
        Args:
            id (int): Pokemon's ID.
        """

        query = "SELECT * FROM pokemons WHERE id = ?"
        pokemon = super().run_query_select_fetchone(query, id)
        return pokemon
    
    def get_pokemon_amount(self):
        "Get the number of pokemons availables inthe database."
        
        """Get the amount of Pokemon in database"""
        query = "SELECT COUNT(*) FROM pokemons"
        pokemon_amount = super().run_query_select_fetchone(query)[0]
        return pokemon_amount

    def get_pokemon_attacks_id(self, pokemon_id: int):
        """Get the attacks ID avaliable to a pokemon.
        
        Args:
            pokemon_id (int): ID of the pokemon.
        """

        query = "SELECT attack_id from pokemon_attacks where pokemon_id = ?"
        avaliable_attacks = super().run_query_select_fetchall(query, str(pokemon_id))
        attack_list = []

        for attack in avaliable_attacks:
            attack_list.append(attack[0])
        return attack_list