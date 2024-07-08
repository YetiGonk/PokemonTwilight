import sys
import os
import time
import random

current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir+"/poke-battle-sim")

from poke_battle_sim.poke_sim import PokeSim
from poke_battle_sim.core.pokemon import Pokemon
from poke_battle_sim.core.trainer import Trainer
from poke_battle_sim.core.battle import Battle
from poke_battle_sim.core.battlefield import Battlefield
from poke_battle_sim.core.move import Move
import poke_battle_sim.util.process_move as pm
import poke_battle_sim.util.process_ability as pa
import poke_battle_sim.util.process_item as pi
import poke_battle_sim.conf.global_settings as gs
import poke_battle_sim.conf.global_data as gd

PLAYER_NAME = None

def main():

    PokeSim.start()

    #intro_script()
    starters = initialize_starters()
    first_class(starters)
    player_pokemon = choose_starter(starters)

    cafeteria_scene()

def intro_script():
    
    _print("The car's tires hum softly against the wet road as you drive through the dense fog that clings to the landscape of Forks, Washington.\nThe overcast sky, towering evergreens on either side of the road… It's a fresh start in a new town, far away from the bustling life you once knew.")
    time.sleep(2)

    _print("\nAs you pull up to your new home, a sense of apprehension stirs within you. It looks old and damp.\nYou can clearly see the peeling paint-job and rotting wood on its walls.\nThere's no excitement, no fear within you. Moving here was never part of the plan, but plans change, especially when you're the new kid in town, again.")
    time.sleep(2)

    _print("\nForks, with its endless rain and shadows, feels like a scene ripped from a book you wouldn't read, yet here you are, about to start one of its many chapters.\nTomorrow, you'll walk the halls of Forks High School, a nobody in a sea of somebodies.\n\n")
    time.sleep(5)
    
def first_class(starters):

    _print("First Day at School\n\n")
    time.sleep(2)
    _print("The school bell echoes through the halls of Forks High, a clear signal that the show must go on, with you playing the starring role of The New Kid.\nThe corridors buzz with the energy of students, their laughter and chatter forming a backdrop to your own silent contemplations as you navigate your way to class.\n")
    time.sleep(2)
    _print("The moment you step into the classroom, it's as if an invisible spotlight has settled on you, the air thick with anticipation.\nYou find a seat just as the door opens to reveal Professor Pine, a man whose presence seems to command immediate attention, though his demeanour suggests he's walked through these motions far more times than he cares to count.\n")
    time.sleep(2)
    _print('\"Settle down, settle down,\" he announces. \'First, let me express my gratitude for you choosing this experimental module.\"\n\"I practically had to beg the administrative staff to allow it, but here we are.\"\n\"Let\'s go through the register,\" he announces, and a sudden hush falls over the class.\nAs names are called, each one ticks by, leading closer to yours.\n"And what might your name be?" he finally turns to me, the question hanging in the air, spotlight squarely on the new oddity in town — me. I mumble my name, feeling the weight of gazes sizing me up, slotting me into their social hierarchies.\n\n')

    get_player_name()
    
    _print("With the formalities out of the way, Pine leans against his desk, surveying the class with a look that\'s hard to read.\n\"Alright, let\'s cut to the chase. Pokémon.\" He says it like it\'s a world unto itself, a shared secret.\n\"Here, Pokémon aren\'t just companions; they\'re as much a part of Forks as the trees and the mist.\"\n")
    time.sleep(2)
    _print("The class chuckles a little at his serious demeanour. \"It's true!\"\n\"In this town, Pokémon roam freely, intertwining with our lives in ways you might not expect.\"\n\"They can be life-long friends, allies, challengers, and sometimes, a bridge to the unknown,\" he continues\n")
    time.sleep(2)
    _print("Mid-sentence, Pine reaches into his bag and pulls out a Poké Ball.\nWith a flick of his wrist, he releases his Pokémon — a vibrant Eevee jumps out onto his desk. It immediately captures the room's attention. \n\"This is Fluff,\" he introduces.\nThe Eevee greets the class with a cheerful yip. \"I been Fluff\'s trainer for going on 3 years now.\"\n")
    time.sleep(2)
    _print("\"As you embark on this module, you'll be encountering, befriending and training Pokémon just like Eevee.\"\n\"And today,\" Pine pauses, looking around the class as a smile spreads across his face, \"today, you'll begin forging your own path with a Pokémon companion.\"\n\"Yes, you'll be receiving your starter Pokémon.\"\n")
    time.sleep(2)
    _print("Pine moves to the front of the class, a table now mysteriously laden with three distinct Poké Balls.\n\"When it's your turn,\" he instructs, \"come up and choose the one that feels right.\"\n\"Trust your instincts.\"\n")
    time.sleep(2)
    _print("As Professor Pine calls the class's attention for the moment of choosing your first Pokémon, your heart races.\nThe decision feels bigger than it probably should, like whatever choice you make will ripple through the rest of your time in Forks.\nYou're standing there, trying to decide, when you notice someone else at the edge of your vision.\nA mysterious figure. He stands apart, his presence unmistakable even in the crowded classroom.\nFor a moment, the world seems to pause as you take in his almost otherworldly appearance: his skin is pale, almost translucent, under the fluorescent lights.\nThere's something unmistakably different about him, something that speaks of both elegance and an unnerving stillness.\nHis eyes, a deep, unfathomable shade. Just as quickly, the moment passes, and the buzz of the classroom resumes, pulling your attention back to the task at hand.\n")
    _print(f"\"{PLAYER_NAME}! You're up!\" Professor Pine announces.")
    
    player_pokemon = choose_starter(starters)

def cafeteria_scene():
    _print("Later, in the cafeteria, you're sitting with some people who might be your friends.\nYou're not sure yet. You're not even sure how you ended up here, but they're talking about everyone and everything, including the mysterious figure from before.\n")
    time.sleep(2)
    _print('"Did you see that guy earlier?" you find yourself asking, trying not to sound too interested.\n')
    time.sleep(2)
    _print('"Yeah, that\'s Edward Cullen. He\'s... different," one of them whispers, leaning in.\nThe name doesn\'t mean much to you, but the way they say it, like it\'s a secret everyone\'s in on but you, makes you curious.\n')
    time.sleep(2)
    _print("You nod, acting like you understand, like you're not completely out of your depth. Edward Cullen. The name sticks in your mind, another piece of Forks to figure out.\nBut that's a problem for another day. Right now, you're just trying to get through lunch without revealing too much about how overwhelmed you feel.\n")
    time.sleep(2)
    _print("The bell rings, and you're grateful for the escape. As you head to your next class, the thought of Edward and the brief, almost encounter lingers.\n")

def initialize_starters():
    starters = {
        'sproutide': Pokemon('sproutide', level=5, moves=['tackle','leer'], gender=random.choice(["male", "female"]), ability=random.choice(['overgrow','chlorophyll','sand-veil'])),
        'glinti': Pokemon('glinti', level=5, moves=['scratch','tail-whip'], gender=random.choice(("male", "female")), ability=random.choice(['storm-drain','intimidate','moxie'])),
        'lunapup': Pokemon('lunapup', level=5, moves=['pound','growl'], gender=random.choice(("male", "female")), ability=random.choice(['flame-body','blaze','serene-grace']))
    }
    return starters

def choose_starter(starters):
    _print("Professor Pine presents you with three Poké Balls: \"It's time to choose your companion.\"")
    time.sleep(2)
    starters_info = {
        '1': "001: Sproutide\nType: Grass/Ground\nAbilities: Overgrow, Chlorophyll, Sand Force\nBase Stats: HP: 50, Attack: 55, Defense: 45, Special Attack: 35, Special Defense: 45, Speed: 40, Total: 270\nHeight: 0.3m, Weight: 5kg\nCategory: Bud Pokémon\nDescription: A small, sprightly Pokémon that resembles a budding beach flower. Its body is covered in a mix of soft green foliage and grainy textures, making it adept at blending into both forested areas and sandy terrains.",
        '2': "004: Lunapup\nType: Water/Dark\nAbilities: Storm Drain, Intimidate, Moxie\nBase Stats: HP: 45, Attack: 65, Defense: 40, Special Attack: 50, Special Defense: 40, Speed: 60, Total: 300\nHeight: 0.6m, Weight: 15kg\nCategory: Moonlight Pup Pokemon\nDescription: A small, wolf-like Pokémon with dark blue fur and a moon-shaped patch over one eye. It's known for its loyalty and playful bites that can surprisingly turn fierce in battle.",
        '3': "007: Glinti\nType: Fire/Fairy\nAbilities: Flame Body, Prankster, Serene Grace\nBase Stats: HP: 40, Attack: 50, Defense: 45, Special Attack: 70, Special Defense: 45, Speed: 70, Total: 320\nHeight: 0.4m, Weight: 8.5kg\nCategory: Sparkle Pokémon\nDescription: A small, impish Pokémon with a bright, warm glow. Its playful leaps leave behind a trail of sparkles, captivating all who see it."
    }
    for key, value in starters_info.items():
        _print(value + "\n")
        time.sleep(5)  # Gives the player time to read each entry
    
    while True:
        choice = input("Which one will you choose? (Enter 1, 2, or 3): ").strip()

        if choice not in ['1', '2', '3']:
            _print("That's not a valid choice. Please choose 1, 2, or 3.")
            continue

        # Confirm the choice
        _print(f"\nYou chose:\n{starters_info[choice]}\n")
        confirm = input("Are you sure? (y/n): ").strip().lower()
        if confirm in ["y", "yes", ""]:
            if choice == '1':
                return starters['Sproutide']
            elif choice == '2':
                return starters['Glinti']
            elif choice == '3':
                return starters['Lunapup']
        else:
            _print("Let's choose again.\n")

def get_player_name():
    global PLAYER_NAME
    while True: 
        print("What is your name?")
        player_name = input("Name: > ").strip()

        if not player_name:
            print("The name cannot be empty. Please enter a valid name.")
            continue
        
        if len(player_name) > 10:
            print("The name cannot be longer than 10 characters. Please enter a valid name.")
            continue

        print(f"Are you sure your name is {player_name}? (y/n)")
        confirm = input("> ").strip().lower()

        if confirm in ["y", "yes", "Y", ""]:
            PLAYER_NAME = player_name
            return 
        else:
            print("Name not confirmed. Let's try again.")

def _print(text, delay=0.02):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

if __name__ == "__main__":
    main()