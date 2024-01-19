from database_repository import DatabateRepository

class AttackRepository(DatabateRepository):
    """This class is used to access the attacks in the database

    Attributes:
        db_name (str): name of the database to get the data.
    """

    def __init__(self, db_name: str):
        self.db_name = db_name

    def get_attacks(self):
        "Returns all the attacks of the database"
        
        query = """
        SELECT  id, name, type, power, cooldown
        FROM attacks"""
        return super().run_query_select_fetchall(query)
    