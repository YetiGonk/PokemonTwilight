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
        self.power = move_details.get("power", 0)  # Some moves may not deal damage
        self.pp = move_details["pp"]
        self.accuracy = move_details.get("accuracy", 100)
        self.priority = move_details.get("priority", 0)
        self.damage_class = move_details["damage_class"]
        self.critical_rate = move_details.get("critical_rate", 1)  # Adjusted for moves with different crit rates
        self.status_effect = move_details.get("status_effect", None)
        self.learned_by_pokemon = move_details.get("learned_by_pokemon", [])
        self.flavor_text_entries = move_details.get("flavor_text_entries", [])
        self.stat_changes = move_details.get("stat_changes", [])
        self.target = move_details["target"]
        self.min_hits = move_details.get("min_hits", 1)
        self.max_hits = move_details.get("max_hits", 1)

        # Load type effectiveness data
        self.type_effectiveness = self.load_data("effective_data.json")

    def accuracy_check(self):
        return random.random() <= self.accuracy / 100

    def is_critical_hit(self):
        # Adjust for moves with a high critical hit ratio
        return random.random() < (0.1 * self.critical_rate)

    def execute(self, attacker, defender):
        if not self.accuracy_check():
            print(f"{attacker.name}'s {self.name} missed!")
            return

        hits = random.randint(self.min_hits, self.max_hits)
        total_damage = 0
        for _ in range(hits):
            is_critical = self.is_critical_hit()
            damage, msg = self.calculate_damage(attacker, defender, is_critical)
            defender.take_damage(damage)
            total_damage += damage
            print(f"{attacker.name} used {self.name}! {msg}")

        print(f"{self.name} hit {hits} time(s), dealing a total of {total_damage} damage.")

        # Check for status effect application
        if self.status_effect:
            self.apply_status_effect(defender)

    def calculate_damage(self, attacker, defender, is_critical):
        STAB = 1.5 if self.type in attacker.type else 1
        critical_modifier = 2 if is_critical else 1
        effectiveness = self.get_effectiveness_modifier(self.type, defender.type)
        Modifier = STAB * critical_modifier * effectiveness

        attack_stat = attacker.attack if self.damage_class == "physical" else attacker.sp_atk
        defense_stat = defender.defense if self.damage_class == "physical" else defender.sp_def

        Damage = (((((2 * attacker.level / 5 + 2) * self.power * (attack_stat / defense_stat)) / 50) + 2) * Modifier)
        msg = "A critical hit!" if is_critical else ""
        return int(Damage), msg

    def get_effectiveness_modifier(self, attacker_type, defender_types):
        modifier = 1
        for defender_type in defender_types:
            effectiveness = next((type_info for type_info in self.type_effectiveness if type_info["name"] == defender_type), None)
            if attacker_type in effectiveness["immunes"]:
                modifier *= 0
            elif attacker_type in effectiveness["weaknesses"]:
                modifier *= 0.5
            elif attacker_type in effectiveness["strengths"]:
                modifier *= 2
        return modifier

    def apply_status_effect(self, defender):
        if random.random() <= self.status_effect.get("chance", 0):  # Ensure there's a chance defined
            defender.apply_status_effect(self.status_effect["type"])
            print(f"{defender.name} was affected by {self.status_effect['type']}!")

    def __str__(self):
        return self.name