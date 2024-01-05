from database_repository import DatabateRepository
from pokemon_player import PokemonPlayer
from pokemon import Pokemon

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