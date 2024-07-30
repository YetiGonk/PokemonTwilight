from pokemon_data import POKEMON_DATA
import requests
from alive_progress import alive_bar
from unidecode import unidecode
import json

pokemon_data = POKEMON_DATA

def get_genus_data(pokemon_name):
    url = f"https://pokeapi.co/api/v2/pokemon-species/{str(POKEMON_DATA[pokemon_name.lower()]['species'])}"
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"Failed to fetch data for Pokémon: {pokemon_name}")
    data = response.json()
    for genus in data['genera']:
        if genus['language']['name'] == 'en':
            return str(genus['genus'])
    return None

def update_pokemon_data():
    with alive_bar(len(pokemon_data.keys())) as bar:
        for pokemon in list(pokemon_data.keys()):
            try:
                pokemon_data[pokemon]['genus'] = get_genus_data(pokemon)
            except Exception as e:
                print(f"Error fetching data for {pokemon}: {e}")
            bar()

    with open('pokemon_data.py', 'w') as file:
        file.write(f'POKEMON_DATA = {json.dumps(pokemon_data, indent=4)}\n')

if __name__ == "__main__":
    update_pokemon_data()