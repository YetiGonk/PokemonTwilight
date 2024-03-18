from engine.pokemon import Pokemon
from engine.moves import Move
from engine.battle import Battle

# Creating Moves
thunderbolt = Move("Thunderbolt")
ember = Move("Ember")

# Creating Pokemon objects
pikachu = Pokemon(name="Pikachu", level=5, type="Electric", max_hp=35, current_hp=35, moves=[thunderbolt])
charmander = Pokemon(name="Charmander", level=5, type="Fire", max_hp=39, current_hp=39, moves=[ember])
