from game_data import EFFECTIVE_DATA, NATURE_DATA
from pokemon_data import POKEMON_DATA, GENDER_RATIOS
from move_data import MOVE_DATA
from ability_data import ABILITY_DATA
import random

class Pokemon:
    def __init__(self, name, level, ability=None, held_item=None, moves=None, evs=None, nature=None, gender=None, current_hp=None, status_effect=None):
        self.name = name
        self.data = POKEMON_DATA[self.name]
        self.level = level
        self.ability = self.choose_ability() if not ability else ability
        self.held_item = held_item
        if not moves:
            moveset = self.choose_moves(self.level)
            self.moves = {
                index: {
                    'name': move_name,
                    'current_pp': MOVE_DATA[move_name]['max_pp']
                    } if move_name else None for index, move_name in enumerate(moveset)
            }
        else:
            self.moves = {
                index: {
                    'name': move_name,
                    'current_pp': MOVE_DATA[move_name]['max_pp']
                    } if move_name else None for index, move_name in enumerate(moves)
            }

        self.nature = self.choose_nature() if not nature else nature
        self.happiness = 0

        self.gender = self.choose_gender() if not gender else gender

        self.type = [t['type'] for t in self.data['types']]
        self.base_stats = {stat['stat']: stat['base_stat'] for stat in self.data['stats']}
        self.real_stats = {list(self.base_stats.keys())[i]:(list(self.base_stats.values())[i]/50)*self.level for i in range(len(self.base_stats))}
        self.stat_mods = {list(self.base_stats.keys())[i]: 0 for i in range(len(self.base_stats))}
        self.accuracy_mod = 0
        self.critical_hit_mod = 0

        self.evs = {list(self.base_stats.keys())[i]: 0 for i in range(len(self.base_stats))} if not evs else evs

        self.max_hp = int(0.01 * (2 * self.base_stats['HP'] + int(0.25 * self.evs['HP'])) * self.level) + self.level + 10
        self.current_hp = self.max_hp if not current_hp else current_hp

        self.current_xp = 0
        self.level_xp = (self.level+1)**3 - self.level**3

        self.status_effect = None if not status_effect else status_effect
        self.status_counter = 0
        self.fainted = False if self.current_hp > 0 else True
        self.can_move = True

        self.paused = False

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

    def choose_gender(self):
        ratio = GENDER_RATIOS[self.name]
        if ratio is None:
            return 'genderless'
        else:
            if random.random() < ratio:
                return 'male'
            else:
                return 'female'

    def get_effectiveness(self, atk_type, def_types):
        eff = 1
        for def_type in def_types:
            if def_type in EFFECTIVE_DATA[atk_type].keys():
                eff *= float(EFFECTIVE_DATA[atk_type][def_type])
        return eff

    def cure_all(self):
        self.current_hp = self.max_hp
        for i in range(len(self.moves)):
            self.moves[i]['current_pp'] = MOVE_DATA[self.moves[i]['name']]['max_pp']
        self.status_effect = None
        self.status_counter = 0

    def reset_stat_mods(self):
        self.stat_mods = {list(self.base_stats.keys())[i]: 0 for i in range(len(self.base_stats))}
        self.accuracy_mod = 0
        self.critical_hit_mod = 0

    def update(self, dt):
        pass