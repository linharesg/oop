# from battle import Battle (cannot import battle cause of circular import)
from database_repository import DatabateRepository

class BattleRepository(DatabateRepository):
    """This class is used to create the connection between the battle results and the database
    
    Attributes:
        db_name: name of the database.
    """
    def __init__(self, db_name: str):
        self.db_name = db_name

    def load_battle_results(self, battle):
        """Loads the battle results to the database
        
        Args:
            battle (Battle): The battle to have the results stored
        """
        pokemon1 = str(battle.pokemon1.id)
        pokemon2 = str(battle.pokemon2.id)
        winner = battle.winner
        rounds = str(battle.your_attacks + battle.opponent_attacks)
        time = battle.start_time
        query = """INSERT INTO battle_results
        (pokemon_1_id, pokemon_2_id, winner, timestamp, rounds)
        VALUES
        (?, ?, ?, ?, ?)"""
        super().run_query(query, pokemon1, pokemon2, winner, time, rounds)


