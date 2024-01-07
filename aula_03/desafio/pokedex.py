import requests
from bs4 import BeautifulSoup
import re

url_moves = "https://pokemondb.net/move/generation/1"
response_moves = requests.get(url_moves)
soup_moves = BeautifulSoup(response_moves.content, "html.parser")

table = soup_moves.find_all("table")[0]
rows = table.find_all("tr")

dict = {}

for index_attack, row in enumerate(rows[1:]):
    cells = row.find_all("td")
    if len(cells) > 0:
        move_name = cells[0].text.strip()
        print(move_name)
        # dict[index_attack + 1] = []
        # move_type = cells[1].text.strip()
        # move_power = cells[3].text.strip()
        # move_pp = cells[5].text.strip()
        url_attack = "https://pokemondb.net" + cells[0].contents[0].attrs['href']


        
        response_pokemon = requests.get(url_attack)
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
