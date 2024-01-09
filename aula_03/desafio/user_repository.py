from database_repository import DatabateRepository
from pokemon_player import PokemonPlayer
from pokemon import Pokemon
# from battle import Battle

class UserRepository(DatabateRepository):

    def __init__(self, db_name: str):
        self.db_name = db_name

    def get_users_pokemon(self, user_id):

        query = "SELECT * FROM user_pokemon where user_id = ?"
        user_pokemon_list = super().run_query_select_fetchall(query, user_id)

        return user_pokemon_list   

    def get_user_id(self, user):

        query = "SELECT id FROM users WHERE user = ?" 
        user_id = super().run_query_select_fetchone(query, user)
        return user_id[0]
    
    def update_pokemon_level(self, battle):
        "Updates the level of the pokemon after a battle"
        
        bt = str(battle.pokemon1.level)
        pokemon1 = str(battle.pokemon1.id)
        user = str(battle.user.id)
        query = "UPDATE user_pokemon SET level = ? WHERE pokemon_id = ? and user_id = ?"
        super().run_query(query, bt, pokemon1, user)