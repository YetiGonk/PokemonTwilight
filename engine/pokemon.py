from engine.moves import Move   
from data_methods import DataMethods
import random

class Pokemon(DataMethods):
    def __init__(self, name, level, max_hp, current_hp, moves, status=None):
        super().__init__()
        pokemon_data = self.load_data("pokemon_data.json")
        
        # Ensure the Pokémon exists in the data
        if name not in pokemon_data:
            raise ValueError(f"Pokemon '{name}' not found in pokemon_data.json")
        
        self.pokemon = pokemon_data[name]
        self.name = name
        self.level = level
        self.max_hp = max_hp
        self.current_hp = current_hp
        self.moves = [Move(move) for move in moves]  # Assuming moves is a list of move names
        self.type = self.pokemon["type"]
        self.bst = self.pokemon["total"]
        self.hp_stat = self.pokemon["hp"]
        self.attack = self.pokemon["attack"]
        self.defense = self.pokemon["defense"]
        self.sp_atk = self.pokemon["sp_atk"]
        self.sp_def = self.pokemon["sp_def"]
        self.speed = self.pokemon["speed"]
        self.status = status

    def is_knocked_out(self):
        return self.current_hp <= 0

    def take_damage(self, damage):
        self.current_hp -= damage
        if self.current_hp < 0:
            self.current_hp = 0
        print(f"{self.name} took {damage} damage and is now at {self.current_hp} HP.")

    def attack(self, move_name, opponent):
        if self.is_knocked_out():
            print(f"{self.name} can't battle because it's knocked out!")
            return

        # Find the move object based on move_name
        move = next((move for move in self.moves if move.name == move_name), None)
        if not move:
            print(f"{self.name} doesn't know the move {move_name}.")
            return

        # Check if the move has enough PP
        if move.pp <= 0:
            print(f"{move_name} has no PP left!")
            return

        # Calculate damage and apply to the opponent
        damage, effectiveness_message = move.calculate_damage(self, opponent)
        print(f"{self.name} used {move_name}! {effectiveness_message}")
        opponent.take_damage(damage)
        
    def apply_status_effect(self, effect):
        # Apply a new status effect if one is not already present
        if not self.status:
            self.status = effect
            print(f"{self.name} is now {effect}!")
        else:
            print(f"{self.name} is already affected by {self.status}.")

    def resolve_status_effects_before_turn(self):
        # Resolve effects like Burn or Poison at the start of a turn
        if self.status in ['burn', 'poison']:
            damage = self.max_hp * 0.1  # Example damage calculation
            self.take_damage(damage)
            print(f"{self.name} is hurt by {self.status}!")

    def resolve_status_effects_after_turn(self):
        # Check for thawing or waking up
        if self.status == 'freeze' and random.randint(1, 5) == 1:
            self.status = None
            print(f"{self.name} has thawed out!")
        elif self.status == 'sleep':
            # Assuming sleep lasts for 1 to 3 turns
            if self.sleep_turns > 0:
                self.sleep_turns -= 1
            if self.sleep_turns == 0:
                self.status = None
                print(f"{self.name} woke up!")
    
    def is_able_to_attack(self):
        # Check if the Pokémon can attack based on its status
        if self.status in ['freeze', 'sleep']:
            print(f"{self.name} is fully paralyzed and cannot move!")
            return False
        elif self.status == 'paralysis' and random.randint(1, 4) == 1:
            print(f"{self.name} is fully paralyzed and cannot move!")
            return False
        return True