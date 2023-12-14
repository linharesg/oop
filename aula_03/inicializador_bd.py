import sqlite3

class InicializadorBD:
    """Classe responsável por inicializar o banco de dados."""

    @staticmethod
    def criar_tabelas(db_nome: str):
        """Cria as tabelas no banco de dados.
        
        Args:
            db_nome (str): 
        """
        connection = sqlite3.connect(db_nome)
        cursor = connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE
            );
        """)
        connection.commit()
        connection.close()