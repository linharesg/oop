import sqlite3
from database_repository import DatabateRepository

class DataBaseCreating(DatabateRepository):
    """Classe que inicia o banco de dados, criando as tabelas"""

    @staticmethod
    def create_table(db_name: str):
        """Create the database tables.
        
        Args:
            db_name (str): Name of the table being created.
        """

        connection = sqlite3.connect(db_name)
        cursor = connection.cursor()
        cursor.executescript("""
            CREATE TABLE IF NOT EXISTS pokemons (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                type TEXT NOT NULL,
                hp INTEGER NOT NULL
            );
            
            CREATE TABLE IF NOT EXISTS attacks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                type TEXT NOT NULL,
                power INT NOT NULL,
                cooldown INT NOT NULL
            );

            CREATE TABLE IF NOT EXISTS pokemon_attacks (
                pokemon_id INTEGER,
                attack_id INTEGER,
                PRIMARY KEY (pokemon_id, attack_id),
                FOREIGN KEY (pokemon_id) REFERENCES pokemons(id),
                FOREIGN KEY (attack_id) REFERENCES attacks(id)
            );
            
            CREATE TABLE IF NOT EXISTS battle_results (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                pokemon_1_id INTEGER NOT NULL,
                pokemon_2_id INTEGER NOT NULL,
                winner INTEGER NOT NULL,
                timestamp INTEGER NOT NULL,
                FOREIGN KEY (pokemon_1_id) REFERENCES pokemons(id),
                FOREIGN KEY (pokemon_2_id) REFERENCES pokemons(id)
            );
            """)

        connection.commit()
        connection.close()
    
    # 
    def insert_default_data():
        pass