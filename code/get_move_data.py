import requests
import json
from alive_progress import alive_bar
from pokemon_data import POKEMON_DATA

MOVE_DATA = {}

def get_move_data(move_name):
    url = f"https://pokeapi.co/api/v2/move/{move_name}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None

def format_move_data(data):
    if data:
        move_data = {}
        move_name = data['name']
        move_data['name'] = move_name
        move_data['id'] = data['id']
        move_data['name'] = data['name']
        move_data['accuracy'] = data['accuracy']
        move_data['priority'] = data['priority']
        move_data['power'] = data['power']
        move_data['type'] = data['type']['name']
        move_data['damage_class'] = data['damage_class']['name']
        move_data['stat_changes'] = data['stat_changes']
        move_data['effect_chance'] = data['effect_chance']
        move_data['target'] = data['target']['name']
        move_data['meta'] = data['meta']
        for effect_entry in data['effect_entries']:
            if effect_entry['language']['name'] == 'en':
                move_data['effect_entries'] = effect_entry['short_effect']
        for flavor_text_entry in data['flavor_text_entries']:
            if flavor_text_entry['language']['name'] == 'en':
                move_data['flavor_text_entry'] = flavor_text_entry['flavor_text'].replace('\n', ' ')
                break
        MOVE_DATA[move_name] = move_data
    else:
        print("Move data not found")

def collect_moves():
    with alive_bar(len(POKEMON_DATA)) as bar:
        i = 0
        for pokemon in POKEMON_DATA.values():
            print(f'- - - - - - - - - - Adding {list(POKEMON_DATA.keys())[i]}')
            for move in pokemon["moves"]:
                if move['move'] not in MOVE_DATA.keys():
                    format_move_data(get_move_data(move['move']))
                    print(f'Added {move['move']}')
                else:
                    print(f'- - - - - - - - - - {move['move']} already exists.')
            print(f'- - - - - - - - - - - Added all of {list(POKEMON_DATA.keys())[i]}')
            i += 1
            bar()

collect_moves()

with open('move_data.py', 'w') as file:
    file.write(f'MOVE_DATA = {json.dumps(MOVE_DATA, indent=4)}\n')