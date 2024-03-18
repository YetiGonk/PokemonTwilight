import requests
import json

def fetch_move_data(move_id):
    url = f"https://pokeapi.co/api/v2/move/{move_id}"
    response = requests.get(url)
    move_data = response.json()
    
    return {
        "id": str(move_data["id"]).zfill(4),
        "name": move_data["name"].capitalize().replace("-", " "),
        "type": move_data["type"]["name"].capitalize(),
        "power": move_data["power"],
        "pp": move_data["pp"],
        "accuracy": move_data["accuracy"],
        "priority": move_data["priority"],
        "damage_class": move_data["damage_class"]["name"].capitalize(),
        "learned_by_pokemon": [pokemon["name"] for pokemon in move_data["learned_by_pokemon"]],
        "flavor_text_entries": [entry["flavor_text"] for entry in move_data["flavor_text_entries"] if entry["language"]["name"] == "en"],
        "stat_changes": move_data["stat_changes"],
        "target": move_data["target"]["name"]
    }

# The number of moves in Gen 1 is 165, but let's fetch a bit more in case the IDs are not completely sequential
moves_data = {}
i = 1
for move_id in range(1, 801):  # Adjust based on the actual number of moves available
    try:
        move_data = fetch_move_data(move_id)
        moves_data[move_data["name"]] = move_data
        print(move_data["name"].capitalize().replace("-", " "), " - ", i)
        i+=1
    except Exception as e:
        print(f"Failed to fetch move with ID {move_id}: {str(e)}")

# Saving the data to a JSON file
with open("moves.json", "w") as file:
    json.dump(moves_data, file, indent=4)