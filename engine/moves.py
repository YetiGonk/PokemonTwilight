import random
from data_methods import DataMethods

class Move(DataMethods):
    def __init__(self, name):
        super().__init__()
        self.name = name

        # Load move details from JSON file
        move_data = self.load_data("moves_data.json")

        if name not in move_data:
            raise ValueError(f"Move '{name}' not found in moves.json")

        move_details = move_data[name]
        self.id = move_details["id"]
        self.type = move_details["type"]
        self.power = move_details.get("power", 0)  # Some moves may not deal damage and thus have no power
        self.pp = move_details["pp"]
        self.accuracy = move_details.get("accuracy", 100)  # Default to 100 if not specified
        self.priority = move_details.get("priority", 0)
        self.damage_class = move_details["damage_class"]
        self.status_effect = move_details.get("status_effect", None)
        self.learned_by_pokemon = move_details.get("learned_by_pokemon", [])
        self.flavor_text_entries = move_details.get("flavor_text_entries", [])
        self.stat_changes = move_details.get("stat_changes", [])
        self.target = move_details["target"]

    def accuracy_check(self):
        return random.randint(0, 100) <= self.accuracy

    def execute(self, attacker, defender):
        if not self.accuracy_check():
            print(f"{attacker.name}'s {self.name} missed!")
            return

        # Apply damage if the move has power
        if self.power > 0:
            damage, message = self.calculate_damage(attacker, defender)
            defender.take_damage(damage)
            print(f"{attacker.name}'s {self.name} hits for {damage} damage. {message}")
        else:
            print(f"{attacker.name} used {self.name}!")

        # Apply status effect if the move has one
        if self.status_effect and not defender.is_knocked_out():
            defender.apply_status_effect(self.status_effect)
            print(f"{defender.name} is now {self.status_effect}!")

    def calculate_damage(self, attacker, defender):
        # This method should be expanded based on your game's damage calculation rules
        STAB = 1.5 if self.type == attacker.type else 1
        # Placeholder for type effectiveness, you need to implement this based on your game's mechanics
        effectiveness = 1
        Modifier = STAB * effectiveness

        # Critical hit consideration
        critical = 2 if random.random() < 0.1 else 1  # Assuming a 10% critical hit rate

        # Determine attack and defense based on the damage class of the move
        if self.damage_class == "physical":
            attack = attacker.attack
            defense = defender.defense
        elif self.damage_class == "special":
            attack = attacker.sp_atk
            defense = defender.sp_def
        else:  # Status moves don't deal damage
            return 0, "But it failed!"

        Damage = (((2 * attacker.level / 5 + 2) * self.power * (attack / defense) / 50) + 2) * Modifier * critical

        message = "A critical hit!" if critical > 1 else ""
        return int(Damage), message

    def __str__(self):
        return self.name
