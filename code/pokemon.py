from game_data import EFFECTIVE_DATA, NATURE_DATA
from pokemon_data import POKEMON_DATA
from move_data import MOVE_DATA
from ability_data import ABILITY_DATA
import random

class Pokemon:
    def __init__(self, name, level, ability=None, items=None, moves=None, evs=None, nature=None):
        self.name = name
        self.data = POKEMON_DATA[self.name]
        self.level = level
        self.ability = self.choose_ability() if not ability else ability
        self.items = items
        self.moves = self.choose_moves(self.level) if not moves else moves
        self.evs = evs
        self.nature = self.choose_nature() if not nature else nature

        self.type = [t['type'] for t in self.data['types']]
        self.base_stats = {stat['stat']: stat['base_stat'] for stat in self.data['stats']}

    def choose_ability(self):
        abilities = self.data["abilities"]
        hidden_abilities = [ability["ability"] for ability in abilities if ability["is_hidden"]]
        regular_abilities = [ability["ability"] for ability in abilities if not ability["is_hidden"]]
        if len(hidden_abilities) > 1:
            raise ValueError(f"Multiple hidden abilities for {self.name}... {hidden_abilities}")
        if random.randint(0,100) > 5:
            return random.choice(regular_abilities)
        else:
            return random.choice(hidden_abilities)

    def choose_moves(self, level):
        moves = self.data["moves"]
        level_up_moves = [
            move for move in moves 
            if move["details"]["move_learn_method"] == "level-up"
        ]
        valid_moves = [
            move["move"] for move in level_up_moves 
            if move["details"]["level_learned_at"] <= level
        ]
        moveset = random.sample(valid_moves, min(4, len(valid_moves)))
        return moveset

    def choose_nature(self):
        nature_name = random.choice(list(NATURE_DATA.keys()))
        return nature_name

    def get_effectiveness(self, atk_type, def_types):
        eff = 1
        for def_type in def_types:
            if def_type in EFFECTIVE_DATA[atk_type].keys():
                eff *= float(EFFECTIVE_DATA[atk_type][def_type])
        return eff
