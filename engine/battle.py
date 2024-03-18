from pokemon import Pokemon
from moves import Move
import random

class Battle:
    def __init__(self, pokemon1, pokemon2):
        self.pokemon1 = pokemon1
        self.pokemon2 = pokemon2

    def get_move_choice(self, pokemon):
        print(f"\n{pokemon.name}'s turn to choose a move:")
        for idx, move in enumerate(pokemon.moves, start=1):
            print(f"{idx}. {move.name} (PP: {move.pp})")
        while True:
            try:
                choice = int(input("Choose a move: ")) - 1
                if 0 <= choice < len(pokemon.moves) and pokemon.moves[choice].pp > 0:
                    return pokemon.moves[choice]
                else:
                    print("Invalid choice or move out of PP. Choose again.")
            except ValueError:
                print("Please enter a valid number.")

    def determine_turn_order(self, pokemon1_choice, pokemon2_choice):
        if pokemon1_choice.priority == pokemon2_choice.priority:
            return sorted([self.pokemon1, self.pokemon2], key=lambda p: p.speed, reverse=True)
        return [self.pokemon1, self.pokemon2] if pokemon1_choice.priority > pokemon2_choice.priority else [self.pokemon2, self.pokemon1]

    def start_battle(self):
        print(f"A wild battle begins between {self.pokemon1.name} and {self.pokemon2.name}!")

        while not self.pokemon1.is_knocked_out() and not self.pokemon2.is_knocked_out():
            pokemon1_choice = self.get_move_choice(self.pokemon1)
            pokemon2_choice = self.get_move_choice(self.pokemon2)
            order = self.determine_turn_order(pokemon1_choice, pokemon2_choice)

            for pokemon in order:
                if pokemon == self.pokemon1:
                    move_choice = pokemon1_choice
                    defender = self.pokemon2
                else:
                    move_choice = pokemon2_choice
                    defender = self.pokemon1

                self.battle_round(pokemon, defender, move_choice)
                if defender.is_knocked_out():
                    break

            if self.pokemon1.is_knocked_out():
                print(f"{self.pokemon1.name} has been knocked out! {self.pokemon2.name} wins!")
                break
            elif self.pokemon2.is_knocked_out():
                print(f"{self.pokemon2.name} has been knocked out! {self.pokemon1.name} wins!")
                break

    def battle_round(self, attacker, defender, move_choice):
        # Before attacker's turn
        attacker.resolve_status_effects_before_turn()
        if not attacker.is_able_to_attack():
            return  # Skip the turn if the attacker is incapacitated
        if attacker.is_knocked_out() or defender.is_knocked_out():
                # No action if either Pokémon is already knocked out
            return

        # PP Check
        if move_choice.pp <= 0:
            print(f"{move_choice.name} has no PP left! {attacker.name} loses the turn.")
            return
        else:
            move_choice.pp -= 1  # Deduct one PP for using the move

        # Calculate and Apply Damage
        damage, effectiveness_message = move_choice.calculate_damage(attacker, defender)
        print(f"{attacker.name} uses {move_choice.name}! {effectiveness_message}")
        defender.take_damage(damage)

        # Check for Knockout After Attack
        if defender.is_knocked_out():
            print(f"{defender.name} has been knocked out!")
        
        attacker.resolve_status_effects_after_turn()