import requests
import json
import os
from alive_progress import alive_bar
from item_data import ITEM_DATA

ITEM_DATA = {}

PATH = '../graphics/items'

ALL_ITEM_PATHS = []
for root, dirs, files in os.walk(PATH):
    for file in files:
        if file.endswith('.png'):
            if 'tms' not in root:
                ALL_ITEM_PATHS.append(os.path.join(root, file))

def get_item_data(item_path):
    item_path = item_path.replace('.png', '')
    if 'berries' in item_path:
        item_path += '-berry'
    if 'balls' in item_path:
        item_path += '-ball'
    item_name = item_path.split('/')[-1]
    url = f"https://pokeapi.co/api/v2/item/{item_name}"
    print(url)
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None

def format_item_data(data, item_path):
    if data:
        item_data = {}
        item_data['name'] = data['name']
        item_data['id'] = data['id']
        item_data['cost'] = data['cost']
        item_data['fling_power'] = data['fling_power']
        item_data['fling_effect'] = data['fling_effect']['name'] if data['fling_effect'] else None
        item_data['attributes'] = [attr['name'] for attr in data['attributes']]
        item_data['category'] = data['category']['name']
        
        # Handle effect entries
        for effect_entry in data['effect_entries']:
            if effect_entry['language']['name'] == 'en':
                item_data['effect'] = effect_entry['effect'].replace('\n', ' ')
                item_data['short_effect'] = effect_entry['short_effect']
                break

        # Handle flavor text entries
        for flavor_text_entry in data['flavor_text_entries']:
            if flavor_text_entry['language']['name'] == 'en':
                item_data['flavor_text'] = flavor_text_entry['text'].replace('\n', ' ')
                break

        ITEM_DATA[item_data['name']] = item_data
    else:
        print("Item data not found")

def collect_items():
    with alive_bar(len(ALL_ITEM_PATHS)) as bar:
        for item_path in ALL_ITEM_PATHS:
            print(item_path)
            format_item_data(get_item_data(item_path), item_path)
            bar()

collect_items()

with open('item_data.py', 'w') as file:
    file.write(f'ITEM_DATA = {json.dumps(ITEM_DATA, indent=4)}\n')