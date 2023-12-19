from database_repository import DatabateRepository
from pokemon import Pokemon
from attack import Attack
class AttackRepository(DatabateRepository):

    def __init__(self, db_name: str):
        self.db_name = db_name

    def get_attacks(self):
        query = """
        SELECT attacks.* 
        FROM attacks"""
        return super().run_query_select_fetchall(query)
    
repository = AttackRepository("pokemon_game.db").get_attacks()
print(len(repository))
a = []
for i, attack in enumerate(repository):
     a.append(Attack(*repository[i]))

for attack in a:
    print(attack)