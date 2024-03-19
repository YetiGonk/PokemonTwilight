from engine.moves import Move
from data_methods import DataMethods
import random

class Pokemon(DataMethods):
    def __init__(self, name, level, max_hp, moves, status=None):
        super().__init__()
        self.load_pokemon_data(name)
        self.level = level
        self.max_hp = max_hp
        self.current_hp = max_hp  # Starting with full health
        self.moves = [Move(move) for move in moves]  # Load moves
        self.status = status
        self.status_duration = 0
        # Initial stat modifiers for battle effects
        self.stat_modifiers = {"atk": 1, "def": 1, "sp_atk": 1, "sp_def": 1, "speed": 1}

    def load_pokemon_data(self, name):
        pokemon_data = self.load_data("pokemon_data.json")
        if name not in pokemon_data:
            raise ValueError(f"{name} not found in pokemon_data.json")
        
        pokemon = pokemon_data[name]
        self.name = name
        self.type = pokemon["type"]
        self.attack = pokemon["attack"]
        self.defense = pokemon["defense"]
        self.sp_atk = pokemon["sp_atk"]
        self.sp_def = pokemon["sp_def"]
        self.speed = pokemon["speed"]

    def is_knocked_out(self):
        if self.current_hp <= 0:
            print(f"{self.name} is knocked out!")
            return True
        return False

    def take_damage(self, damage):
        self.current_hp = max(0, self.current_hp - damage)
        print(f"{self.name} took {damage} damage and is now at {self.current_hp} HP.")

    def perform_move(self, move_name, target):
        if self.is_knocked_out():
            return
        
        if not self.is_able_to_attack():
            return

        move = next((m for m in self.moves if m.name == move_name), None)
        if move:
            move.execute(self, target)

    def apply_status_effect(self, effect):
        if self.status and effect != "sleep":
            print(f"{self.name} is already affected by {self.status} and cannot be {effect}.")
            return

        self.status = effect
        print(f"{self.name} is now {effect}.")
        if effect == "paralysis":
            self.speed *= 0.75  # Adjust for game balance as needed
        elif effect == "sleep":
            self.status_duration = random.randint(1, 3)  # Sleep for 1-3 turns

    def resolve_status_effects_before_turn(self):
        if self.status == 'burn' or self.status == 'poison':
            damage = max(1, int(self.max_hp * 0.125))  # Example damage calculation for burn/poison
            self.take_damage(damage)

    def end_of_turn_effects(self):
        if self.status == 'burn' or self.status == 'poison':
            self.take_damage(self.max_hp * 0.1)  # Damage from burn/poison
        self.reduce_status_duration()

    def reduce_status_duration(self):
        if self.status_duration > 0:
            self.status_duration -= 1
            if self.status_duration == 0 and self.status == 'sleep':
                self.status = None
                print(f"{self.name} woke up!")

    def is_able_to_attack(self):
        if self.status == 'freeze':
            # 20% chance to thaw out each turn
            if random.randint(1, 5) == 1:
                self.status = None
                print(f"{self.name} has thawed out!")
            else:
                print(f"{self.name} is frozen solid and can't move!")
                return False
        elif self.status == 'sleep':
            if self.status_duration > 0:
                print(f"{self.name} is fast asleep.")
                return False
        elif self.status == 'paralysis' and random.randint(1, 4) == 1:
            print(f"{self.name} is fully paralyzed and can't move!")
            return False
        return True
