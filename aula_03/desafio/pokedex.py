import requests
from bs4 import BeautifulSoup
import re

with open("move_list.html", "r", encoding="utf-8") as file:
    html_content = file.read()

# url_moves = "https://pokemondb.net/move/generation/1"
# response_moves = requests.get(url_moves)
soup_moves = BeautifulSoup(html_content, "html.parser")

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
        move_name = cells[0].text.strip()
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

    query += (f"({index_attack + 1}, '{move_name}', '{move_type}', {move_power}, {move_accuracy}, '{cooldown}),\n")

    
query = query[0:-2] + ";"
print(query)
    


