import sqlite3
from database_repository import DatabateRepository

class DataBaseInitialize(DatabateRepository):
    """Class that starts the database, creating the tables."""

    @staticmethod
    def create_table(db_name: str):
        """Create the database tables.
        
        Args:
            db_name (str): Name of the database.
        """

        connection = sqlite3.connect(db_name)
        cursor = connection.cursor()
        cursor.executescript("""
            CREATE TABLE IF NOT EXISTS pokemons (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT UNIQUE NOT NULL,
                type TEXT NOT NULL,
                hp INTEGER NOT NULL
            );

            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user TEXT UNIQE NOT NULL,
                email TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL
            );
            
            CREATE TABLE IF NOT EXISTS attacks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT UNIQUE NOT NULL,
                type TEXT NOT NULL,
                power INT NOT NULL,
                cooldown INT NOT NULL,
                level INT
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
                timestamp TEXT NOT NULL,
                rounds INTEGER NOT NULL,
                FOREIGN KEY (pokemon_1_id) REFERENCES pokemons(id),
                FOREIGN KEY (pokemon_2_id) REFERENCES pokemons(id)
            );
                             
            CREATE TABLE IF NOT EXISTS user_pokemon (
                user_id INTEGER,
                pokemon_id INTEGER,
                level INTEGER DEFAULT 0,
                PRIMARY KEY (user_id, pokemon_id),
                FOREIGN KEY (pokemon_id) REFERENCES pokemons(id),        
                FOREIGN KEY (user_id) REFERENCES users(id)        
            )
            """)

        connection.commit()
        connection.close()
    
    @staticmethod
    def insert_default_data(db_name: str):
        """Insert default data into the tables created to the game's database.
        
        Args:
            db_name (str): Name of the database.
        """

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
            
            INSERT INTO attacks (name, type, power, cooldown, level) VALUES 
                ('Tackle', 'Normal', 5, 1, 1),
                ('Vine Whip', 'Grass', 15, 3, 0),
                ('Poison Powder', 'Poison', 5, 1, 2),
                ('Scratch', 'Normal', 4, 0, 3),
                ('Ember', 'Fire', 3, 2, 1),
                ('Dragon Rage', 'Fire', 6, 1, 0),
                ('Water Gun', 'Water', 8, 1, 0),
                ('Withdraw', 'Water', 5, 0, 1),
                ('String Shot', 'Bug', 13, 2, 1),
                ('Bug Bite', 'Bug', 12, 3, 0),
                ('Gust', 'Flying', 4, 0, 2),
                ('Mirror Move', 'Flying', 5, 0, 1),
                ('Confusion', 'Psychic', 12, 3, 1),
                ('Hydro Pump', 'Water', 7, 2, 0),
                ('Pay Day', 'Normal', 4, 1, 1),
                ('Bite', 'Dark', 6, 1, 0),
                ('Splash', 'Water', 10, 3, 1),
                ('Flail', 'Normal', 7, 1, 1),
                ('Thunder Shock', 'Electric', 10, 2, 1),
                ('Quick Attack', 'Normal', 5, 1, 0),
                ('Thunderbolt', 'Electric', 9, 2, 0);

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
                             
            INSERT INTO users (user, email, password) VALUES
                ('gabriel.sl', 'gabriel@email.com', '1234'),
                ('amanda.bv', 'amanda@email.com', '1234');
            
            INSERT INTO user_pokemon (user_id, pokemon_id, level) VALUES
                (1, 1, 0),
                (1, 3, 1),
                (1, 4, 0),
                (1, 9, 0),
                (2, 2, 1),
                (2, 5, 2),
                (2, 6, 0),
                (2, 8, 0);
            
            """)
        


