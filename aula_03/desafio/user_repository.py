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

 
    def create_new_user(self):

        user = input("Informe your username: ")
        email = input("Informe your email: ")
        password = input("inform your password: ")

        new_id = self.get_last_user_id()[0] + 1

        query = "INSERT INTO users (id, user, email, password) VALUES (?, ?, ?, ?)"

        super().run_query(query, new_id, user, email, password)

        UserRepository.crete_initial_pokemons(self, new_id)

        return new_id


    def get_last_user_id(self):
        
        query = "SELECT MAX(id) from users"
        
        return super().run_query_select_fetchone(query)


    def crete_initial_pokemons(self, user_id):
        
        query = """INSERT INTO user_pokemon (user_id, pokemon_id, level) VALUES
        (?, 1, 1),
        (?, 4, 1),
        (?, 7, 1),
        (?, 25, 1);
        """
        args_query = []
        TOTAL_POKEMONS = 4
        for i in range(0, TOTAL_POKEMONS):
            args_query.append(user_id)

        super().run_query(query, *args_query)

    def get_user_data(self, user):

        query = "SELECT id, user, email FROM users WHERE id = ?" 
        user_data = super().run_query_select_fetchone(query, user)
        return user_data