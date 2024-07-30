import requests
from alive_progress import alive_bar
from unidecode import unidecode
import json

POKEMON_DATA = {}

# List of version groups in release order
VERSION_GROUPS = [
    "red-blue", "yellow", "gold-silver", "crystal", "ruby-sapphire", "emerald", 
    "firered-leafgreen", "diamond-pearl", "platinum", "heartgold-soulsilver", 
    "black-white", "black-2-white-2", "x-y", "omega-ruby-alpha-sapphire", 
    "sun-moon", "ultra-sun-ultra-moon", "lets-go-pikachu-lets-go-eevee", 
    "sword-shield", "brilliant-diamond-and-shining-pearl", "legends-arceus", 
    "scarlet-violet", "xd", "colosseum"
]

POKEDEX = "Deerling Sawsbuck Pachirisu Teddiursa Ursaring Wingull Pelipper Staryu Starmie Spheal Sealeo Walrein Slakoth Vigoroth Slaking Paras Parasect Kecleon Magnemite Magneton Magnezone Trubbish Garbodor Porygon Porygon2 Porygon-Z Miltank Combee Vespiquen Budew Roselia Roserade Bounsweet Steenee Tsareena Pineco Forretress Dratini Dragonair Dragonite Bagon Shelgon Salamence Flabebe Floette Florges Snubbull Granbull Grimer Muk Koffing Weezing Ditto Eevee Jolteon Umbreon Bonsly Sudowoodo Totodile Croconaw Feraligatr Hoothoot Noctowl Azurill Marill Azumarill Swinub Piloswine Mamoswine Tyrogue Treecko Grovyle Sceptile Mudkip Marshtomp Swampert Lotad Lombre Ludicolo Spoink Grumpig Cacnea Cacturne Corphish Crawdaunt Feebas Milotic Turtwig Grotle Torterra Bidoof Bibarel Buizel Floatzel Drifloon Drifblim Buneary Lopunny Rotom Roggenrola Boldore Gigalith Drilbur Excadrill Cottonee Whimsicott Basculin-red-striped Maractus Scraggy Scrafty Tirtouga Carracosta Cubchoo Beartic Bouffalant Rufflet Braviary Clauncher Clawitzer Hawlucha Klefki Rowlet Dartrix Decidueye Morelull Shiinotic Stufful Bewear Sandygast Palossand Togedemaru Nickit Thievul Vulpix Ninetales Torkoal Ralts Kirlia Gardevoir Munna Musharna Sandile Krokorok Krookodile Mightyena Scyther Scizor Growlithe Arcanine Joltik Galvantula Skarmory".split(' ')

def get_pokemon_data(pokemon_name):
    url = f"https://pokeapi.co/api/v2/pokemon/{unidecode(pokemon_name.lower())}"
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"Failed to fetch data for Pokémon: {pokemon_name}")
    data = response.json()
    
    # Extract and structure the data
    pokemon_info = {
        "id": data["id"],
        "name": data["name"],
        "base_experience": data["base_experience"],
        "height": data["height"],
        "weight": data["weight"],
        "abilities": [
            {
                "is_hidden": ability["is_hidden"],
                "slot": ability["slot"],
                "ability": ability["ability"]["name"]
            } for ability in data["abilities"]
        ],
        "held_items": [
            {
                "item": item["item"]["name"],
                "rarity": detail["rarity"]
            } for item in data["held_items"]
            for detail in item["version_details"]
        ],
        "moves": [],
        "species": data["species"]["name"],
        "stats": [
            {
                "stat": stat["stat"]["name"],
                "effort": stat["effort"],
                "base_stat": stat["base_stat"]
            } for stat in data["stats"]
        ],
        "types": [
            {
                "slot": poke_type["slot"],
                "type": poke_type["type"]["name"]
            } for poke_type in data["types"]
        ]
    }
    
    for move in data["moves"]:
        bw_moves = [detail for detail in move["version_group_details"] if detail["version_group"]["name"] == "black-white"]
        if bw_moves:
            earliest_move = bw_moves[0]
        else:
            earliest_move = sorted(
                move["version_group_details"],
                key=lambda x: VERSION_GROUPS.index(x["version_group"]["name"])
            )[0]
        pokemon_info["moves"].append({
            "move": move["move"]["name"],
            "details": {
                "move_learn_method": earliest_move["move_learn_method"]["name"],
                "level_learned_at": earliest_move["level_learned_at"],
                "version_group": earliest_move["version_group"]["name"]
            }
        })
    
    return pokemon_info

def update_pokemon_data():
    with alive_bar(len(POKEDEX)) as bar:
        for pokemon in POKEDEX:
            try:
                pokemon_data = get_pokemon_data(pokemon)
                POKEMON_DATA[pokemon.lower()] = pokemon_data
            except Exception as e:
                print(f"Error fetching data for {pokemon}: {e}")
            bar()

    # Write updated data back to the file
    with open('game_data.py', 'w') as file:
        file.write(f'POKEMON_DATA = {json.dumps(POKEMON_DATA, indent=4)}\n')

if __name__ == "__main__":
    update_pokemon_data()
