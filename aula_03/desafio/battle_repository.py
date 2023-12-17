from abc import ABC
from battle import Battle
from database_repository import DatabateRepository

class BattleRepository(DatabateRepository):

    def __init__(self, db_name):
        self.db_name = db_name

    def load_battle_results(self, battle: Battle):
        
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


