from requests import get
from bs4 import BeautifulSoup
from abc import ABC

class DamageRepository(ABC):
    "This class is used to get data for damages"

    def get_type_effectiveness():
        "Get the damage effectiveness between attack type and pokemon type"
        
        # Get data from a url
        try:
            url = "https://pokemondb.net/type"
            response = get(url)

            # Get the HTML
            soup = BeautifulSoup(response.content, "html.parser")

            # Get data from the frist table in the HTML
            table = soup.find_all("table")[0]

            # Get each row of the table
            rows = table.find_all("tr")

            # Set the pokemon types as the column title, except the first column
            pokemon_type = [col.next.attrs['title'] for col in rows[0].find_all("th")[1:]]

            # Create a dictionary to relate each pokemon type and attack type
            dictionary = {}

            # Loop into each row of the table, except the first line
            for row in rows[1:]:

                # For each row get the attack type (th) and its respective value for the pokemon type (td) 
                row_th = row.find_all("th")
                row_td = row.find_all("td")
                for index_attack, attack_html in enumerate(row_th):
                    if index_attack == 0:
                        attack_type = attack_html.text
                        dictionary[attack_type] = {}
                    for index_value, value_html in enumerate(row_td):
                        value = value_html.text
                        if value != '':
                            if value == '½':
                                dictionary[attack_type][pokemon_type[index_value]] = 0.5
                                continue
                            dictionary[attack_type][pokemon_type[index_value]] = float(value)
        
        # Backup dictionary, if there is no connection
        except:
            dictionary = {
                'Normal': {'Rock': 0.5, 'Ghost': 0.0, 'Steel': 0.5},
                'Fire': {'Fire': 0.5, 'Water': 0.5, 'Grass': 2.0, 'Ice': 2.0, 'Bug': 2.0, 'Rock': 0.5, 'Dragon': 0.5, 'Steel': 2.0},
                'Water': {'Fire': 2.0, 'Water': 0.5, 'Grass': 0.5, 'Ground': 2.0, 'Rock': 2.0, 'Dragon': 0.5},
                'Electric': {'Water': 2.0, 'Electric': 0.5, 'Grass': 0.5, 'Ground': 0.0, 'Flying': 2.0, 'Dragon': 0.5},
                'Grass': {'Fire': 0.5, 'Water': 2.0, 'Grass': 0.5, 'Poison': 0.5, 'Ground': 2.0, 'Flying': 0.5, 'Bug': 0.5, 'Rock': 2.0, 'Dragon': 0.5, 'Steel': 0.5},
                'Ice': {'Fire': 0.5, 'Water': 0.5, 'Grass': 2.0, 'Ice': 0.5, 'Ground': 2.0, 'Flying': 2.0, 'Dragon': 2.0, 'Steel': 0.5},
                'Fighting': {'Normal': 2.0, 'Ice': 2.0, 'Poison': 0.5, 'Flying': 0.5, 'Psychic': 0.5, 'Bug': 0.5, 'Rock': 2.0, 'Ghost': 0.0, 'Dark': 2.0, 'Steel': 2.0, 'Fairy': 0.5},
                'Poison': {'Grass': 2.0, 'Poison': 0.5, 'Ground': 0.5, 'Rock': 0.5, 'Ghost': 0.5, 'Steel': 0.0, 'Fairy': 2.0},
                'Ground': {'Fire': 2.0, 'Electric': 2.0, 'Grass': 0.5, 'Poison': 2.0, 'Flying': 0.0, 'Bug': 0.5, 'Rock': 2.0, 'Steel': 2.0},
                'Flying': {'Electric': 0.5, 'Grass': 2.0, 'Fighting': 2.0, 'Bug': 2.0, 'Rock': 0.5, 'Steel': 0.5},
                'Psychic': {'Fighting': 2.0, 'Poison': 2.0, 'Psychic': 0.5, 'Dark': 0.0, 'Steel': 0.5},
                'Bug': {'Fire': 0.5, 'Grass': 2.0, 'Fighting': 0.5, 'Poison': 0.5, 'Flying': 0.5, 'Psychic': 2.0, 'Ghost': 0.5, 'Dark': 2.0, 'Steel': 0.5, 'Fairy': 0.5},
                'Rock': {'Fire': 2.0, 'Ice': 2.0, 'Fighting': 0.5, 'Ground': 0.5, 'Flying': 2.0, 'Bug': 2.0, 'Steel': 0.5},
                'Ghost': {'Normal': 0.0, 'Psychic': 2.0, 'Ghost': 2.0, 'Dark': 0.5},
                'Dragon': {'Dragon': 2.0, 'Steel': 0.5, 'Fairy': 0.0},
                'Dark': {'Fighting': 0.5, 'Psychic': 2.0, 'Ghost': 2.0, 'Dark': 0.5, 'Fairy': 0.5},
                'Steel': {'Fire': 0.5, 'Water': 0.5, 'Electric': 0.5, 'Ice': 2.0, 'Rock': 2.0, 'Steel': 0.5, 'Fairy': 2.0},
                'Fairy': {'Fire': 0.5, 'Fighting': 2.0, 'Poison': 0.5, 'Dragon': 2.0, 'Dark': 2.0, 'Steel': 0.5}
                }

        return dictionary