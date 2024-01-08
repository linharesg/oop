import sqlite3
from database_repository import DatabateRepository
from requests import get
from bs4 import BeautifulSoup
import re

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
                power INT DEFAULT 0,
                accuracy INT DEFAULT 0,
                cooldown INT NOT NULL
            );

            CREATE TABLE IF NOT EXISTS pokemon_attacks (
                pokemon_id INTEGER,
                attack_id INTEGER,
                level INTEGER DEFAULT 0,
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
        cursor.executescript(f"""
            
            {DataBaseInitialize.get_pokemon_from_url()}
            
            {DataBaseInitialize.get_attacks_from_url()}
            
            {DataBaseInitialize.get_pokemon_attacks_from_url()}
                             
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
        
    def get_pokemon_from_url():
        
        url = "https://pokemondb.net/pokedex/all"

        response = get(url)

        soup = BeautifulSoup(response.content, "html.parser")

        table = soup.find_all(id="pokedex")[0]

        rows = table.find_all("tr")

        dictionary = {}
        header = rows[0]
        for row in rows[1:]:
            
            row_td = row.find_all("td")
            
            # Find ID
            id = int(row_td[0].attrs["data-sort-value"])
            if id > 151:
                break
            if id not in dictionary.keys():

                # Find Name
                name = re.sub(r'\s+', ' ', row_td[1].text)

                # Find types
                # types = []
                # types_html = row_td[2].find_all("a")
                # for type in types_html:
                #     types.append(type.text)
                type = row_td[2].find_all("a")[0].text
                # print(f"pokemon: {name}")
                #Find HP
                hp = int(row_td[4].text)
                
                dictionary[id] = {"name": name, "types": type, "hp": hp}
                
        query = "INSERT INTO pokemons (id, name, type, hp) VALUES "

        for key, value in dictionary.items():
            id = key
            name = value['name'].replace("'", "''")
            types = value['types']
            hp = value['hp']
            
            query += f"({id}, '{name}', '{types}', {hp}),\n"

        query = f"{query[0:-2]};"        
        return query
    
    def get_pokemon_attacks_from_url():

        url_moves = "https://pokemondb.net/move/generation/1"
        response_moves = get(url_moves)
        soup_moves = BeautifulSoup(response_moves.content, "html.parser")

        table = soup_moves.find_all("table")[0]
        rows = table.find_all("tr")

        dict = {}

        for index_attack, row in enumerate(rows[1:]):
            cells = row.find_all("td")
            if len(cells) > 0:
                # move_name = cells[0].text.strip()
                # print(move_name)
                # dict[index_attack + 1] = []
                # move_type = cells[1].text.strip()
                # move_power = cells[3].text.strip()
                # move_pp = cells[5].text.strip()
                url_attack = "https://pokemondb.net" + cells[0].contents[0].attrs['href']

                response_pokemon = get(url_attack)
                soup_pokemon = BeautifulSoup(response_pokemon.content, "html.parser")
                
                nav_bar = soup_pokemon.find_all(class_="panel-nav")[0]

                if "Learnt by level up" not in nav_bar.text:
                    continue
                
                try:
                    pokemon_board = soup_pokemon.find_all(class_="infocard-list-pkmn-md")[0]
                except:
                    continue

                dict[index_attack + 1] = {"pokemon": [], "level": []}
                pokemons = pokemon_board.find_all(class_="infocard")
                for pokemon_html in pokemons:
                    pokemon_text = pokemon_html.find_all(class_="text-muted")
                    
                    for i in pokemon_text:
                        if "#" in i.text:
                            match = re.search(r'#(\d+)', i.text)
                            id = int(match.group(1))
                            if id in dict[index_attack + 1]["pokemon"] or id > 151:
                                break
                            
                            dict[index_attack + 1]["pokemon"].append(id)
                        if "Level" in i.text:
                            match = re.search(r'(\d+)', i.text)
                            level = int(match.group(1))
                            dict[index_attack + 1]["level"].append(level)

        query = "INSERT INTO pokemon_attacks (attack_id, pokemon_id, level) VALUES "

        for attack_id, poke_level in dict.items():
            for index, value in enumerate(poke_level['pokemon']):
                pokemon_id = poke_level['pokemon'][index]
                level = poke_level['level'][index]
                query += f"({attack_id}, {pokemon_id}, {level}), \n"

        query = f"{query[0:-3]};"
        return query
    
    def get_attacks_from_url():
        with open("move_list.html", "r", encoding="utf-8") as file:
            html_content = file.read()

        url_moves = "https://pokemondb.net/move/generation/1"
        response_moves = get(url_moves)
        # soup_moves = BeautifulSoup(html_content, "html.parser")
        soup_moves = BeautifulSoup(response_moves.content, "html.parser")

        table = soup_moves.find_all("table")[0]
        rows = table.find_all("tr")

        # moves_dict = {}
        query = "INSERT INTO attacks (id, name, type, power, accuracy, cooldown) VALUES "

        for index_attack, row in enumerate(rows[1:]):
            cells = row.find_all("td")
            if len(cells) > 0:
                try:
                    move_power = int(cells[3].text.strip())
                except:
                    move_power = 0
                move_name = re.sub(r'\s+', ' ', cells[0].text.strip().replace("\n", " "))
                try:
                    move_accuracy = int(cells[4].text.strip())
                except:
                    move_accuracy = 0
                move_type = cells[1].text.strip()

                if move_power >= 200:
                    cooldown = 8
                elif move_power >= 150:
                    cooldown = 6
                elif move_power >= 100:
                    cooldown = 5
                elif move_power >= 80:
                    cooldown = 4
                elif move_power >= 50:
                    cooldown = 3
                elif move_power >= 40:
                    cooldown = 2
                elif move_power >= 30:
                    cooldown = 1
                else:
                    cooldown = 0

            query += (f"({index_attack + 1}, '{move_name}', '{move_type}', {move_power}, {move_accuracy}, {cooldown}),\n")

        query = query[0:-2] + ";"
        return query
