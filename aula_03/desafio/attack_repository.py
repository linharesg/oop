from database_repository import DatabateRepository

# from attack import Attack
class AttackRepository(DatabateRepository):

    def __init__(self, db_name: str):
        self.db_name = db_name

    def get_attacks(self):
        query = """
        SELECT attacks.* 
        FROM attacks"""
        return super().run_query_select_fetchall(query)
    
    def get_attacks_amount(self):
        """Get the amount of attacks in database"""
        query = "SELECT COUNT(*) FROM attacks"
        pokemon_amount = super().run_query_select_fetchone(query)[0]
        return pokemon_amount
    
