import sqlite3


class DataBaseCreating:
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
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                pokemon_id INTEGER NOT NULL,
                attack_id INTEGER NOT NULL,
                UNIQUE (pokemon_id, attack_id)
            );
            
            CREATE TABLE IF NOT EXISTS battle_results (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                pokemon_1_id INTEGER NOT NULL,
                pokemon_2_id INTEGER NOT NULL,
                winner INTEGER NOT NULL,
                timestamp INTEGER NOT NULL
            );
            """)

        connection.commit()
        connection.close()