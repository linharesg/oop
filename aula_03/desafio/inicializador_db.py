import sqlite3
from database_repository import DatabateRepository

class DataBaseInitialize(DatabateRepository):
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
    def insert_default_data(db_name):
        connection = sqlite3.connect(db_name)
        cursor = connection.cursor()
        cursor.executescript("""
            INSERT INTO pokemons (name, type, hp) VALUES 
                ('Bulbasaur', 'Grass', 45),
                ('Charmander', 'Fire', 39),
                ('Squirtle', 'Water', 44),
                ('Psyduck', 'Water', 50),
                ('Magikarp', 'Water', 20),
                ('Meowth', 'Normal', 40),
                ('Pidgey', 'Normal', 40),
                ('Caterpie', 'Bug', 45),
                ('Pikachu', 'Electric', 35);
            
            INSERT INTO attacks (name, type, power, cooldown) VALUES 
                ('Tackle', 'Normal', 5, 1),
                ('Vine Whip', 'Grass', 15, 2),
                ('Poison Powder', 'Poison', 5, 1),
                ('Scratch', 'Normal', 4, 0),
                ('Ember', 'Fire', 3, 2),
                ('Dragon Rage', 'Fire', 6, 1),
                ('Water Gun', 'Water', 8, 1),
                ('Withdraw', 'Water', 5, 0),
                ('String Shot', 'Bug', 30, 3),
                ('Bug Bite', 'Bug', 12, 2),
                ('Gust', 'Flying', 4, 0),
                ('Mirror Move', 'Flying', 5, 0),
                ('Confusion', 'Psychic', 25, 4),
                ('Hydro Pump', 'Water', 20, 4),
                ('Pay Day', 'Normal', 4, 1),
                ('Bite', 'Dark', 6, 1),
                ('Splash', 'Water', 10, 2),
                ('Flail', 'Normal', 50, 1),
                ('Thunder Shock', 'Electric', 10, 1),
                ('Quick Attack', 'Normal', 5, 1),
                ('Thunderbolt', 'Electric', 9, 2);

            INSERT INTO pokemon_attacks (attack_id, pokemon_id) VALUES 
                (1, 1),
                (1, 3),
                (1, 8),
                (1, 5),
                (2, 1),
                (3, 1),
                (4, 2),
                (4, 6),
                (5, 2),
                (6, 2),
                (7, 3),
                (7, 4),
                (8, 3),
                (9, 8),
                (10, 8),
                (11, 7),
                (12, 7),
                (13, 4),
                (14, 4),
                (15, 6),
                (16, 6),
                (17, 5),
                (18, 5),
                (19, 9),
                (20, 7),
                (20, 9),
                (21, 9);
            """)
