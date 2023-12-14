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
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS pokemons (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                type TEXT NOT NULL,
                hp INTEGER NOT NULL
            );
            """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS pokemon_atacks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                pokemon_id INTEGER NOT NULL,
                name TEXT NOT NULL,
                power INTEGER NOT NULL,
                accurace INTEGER NOT NULL
            );
        """)
        connection.commit()
        connection.close()