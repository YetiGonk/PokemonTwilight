from settings import *
import textwrap
import random
import math
import player_data
from game_data import *
from move_data import MOVE_DATA
from item_data import ITEM_DATA
import pokemon_data
import ability_data
from groups import BattleSprites
from support import *
from dialog import DialogTree, DialogSprite
from sprites import PokemonSprite, PokemonStatsSprite
from timer import Timer

class Battle:
    def __init__(self, player_pokemon, opponent_pokemon, current_area, fonts, all_sprites, pokemon_graphics, item_graphics, battle_bgs, other_graphics, is_trainer=False):
        # general
        self.display_surface = pygame.display.get_surface()
        bg_surf = battle_bgs[current_area]
        self.bg_surf = pygame.transform.scale(
            bg_surf,
            (bg_surf.get_width()*(self.display_surface.get_width()/bg_surf.get_width()),
            bg_surf.get_height()*(self.display_surface.get_width()/bg_surf.get_width()))
        )
        self.bg_surf_pos = -(self.bg_surf.get_height()-self.display_surface.get_height())
        self.fonts = fonts
        self.current_area = current_area

        self.is_trainer = is_trainer
        self.was_fished = False
        self.caught_with_heal_ball = False
        self.caught_with_friend_ball = False
        self.shake_number = 3
        self.round_number = 1

        self.ui = import_folder_dict(join('..','graphics','ui'))
        self.dialog_tree = None
        self.dialog_input_overlap = False
        self.all_sprites = all_sprites

        self.tint_surf = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.tint_surf.set_alpha(200)   

        self.timers = {
            'start_effects': Timer(150),
            'resolve_action': Timer(150),
            'apply_effects': Timer(150),
            'end_effects': Timer(150)
        }

        # pokemon data
        self.player_pokemon = player_pokemon
        self.opponent_pokemon = opponent_pokemon
        self.current_player_pokemon = self.player_pokemon[0]
        self.current_opponent_pokemon = self.opponent_pokemon[0]
        self.pokemon_graphics = pokemon_graphics

        # item graphics
        self.item_graphics = item_graphics

        # other graphics
        self.move_type_icon = {
            'physical': other_graphics['physical'],
            'special': other_graphics['special'],
            'status': other_graphics['status']
        }

        self.bag_icons = other_graphics['bag_icons']
        self.bag_sprites = other_graphics['bag_sprites']
        self.gender_icons = other_graphics['gender']
        self.status_icons = other_graphics['status_conditions']

        # dimensions
        self.player_pokemon_position = vector(self.display_surface.get_width()*57/225, self.display_surface.get_height()*138/143)
        self.opponent_pokemon_position = vector(self.display_surface.get_width()*170/225,self.display_surface.get_height()*85/143)
        box_to_wall = self.display_surface.get_width()*15/225
        self.stats_size = (self.display_surface.get_width()*97/225, self.display_surface.get_height()*23/143)
        self.player_stats_position = vector(self.display_surface.get_width() - self.stats_size[0] - box_to_wall, self.display_surface.get_height()*131/143 - self.stats_size[1])
        self.opponent_stats_position = vector(box_to_wall, self.display_surface.get_height()*41/143 - self.stats_size[1])

        # groups
        self.battle_sprites = pygame.sprite.Group()
        self.player_sprites = pygame.sprite.Group()
        self.opponent_sprites = pygame.sprite.Group()

        # index
        self.indexes = {
            'workflow': 0,
            'move_order': 0,
            'menu': 0,
            'fight': 0,
            'bag': 0,
            'bag_category': 0,
            'bag_option': 0,
            'bag_pokemon_option': 0,
            'party': (0,0),
            'pokemon_option': 0,
            'pokemon_stats_move': 0
        }

        self.workflow = [
            'select',
            'start_effects', 'start_effects_text', 'pre_move_text', 'resolve_action', 'apply_effects', 'post_move_text', 'post_effect_text', 'end_effects', 'end_effects_text',
            'start_effects', 'start_effects_text', 'pre_move_text', 'resolve_action', 'apply_effects', 'post_move_text', 'post_effect_text', 'end_effects', 'end_effects_text'
        ]
        self.workflow_active = False
        self.move_order = None

        self.selection_mode = 'menu'
        self.party_option_select = False
        self.party_open = False
        self.bag_option_select = False
        self.bag_option_pokemon_select = False
        self.bag_open = False

        # battle flow
        self.player_chosen_action = None
        self.opponent_chosen_action = None
        self.action_chosen = False
        self.switch_token = False
        self.switch_party_selection_mode = False
        self.stat_change_dialog_stack = []
        self.start_effects_dialog_stack = []
        self.post_move_text_dialog_stack = []
        self.post_effect_text_dialog_stack = []
        self.end_effects_dialog_stack = []

        self.run_attempt_counter = 0
        self.attack_missed = False
        self.multi_hit_number = None
        self.reflect_up = {
            'player': False,
            'opponent': False
        }
        self.light_screen_up = {
            'player': False,
            'opponent': False
        }
        self.weather = None
        self.flash_fire_active = {
            'player': False,
            'opponent': False
        }
        self.metronome_counter = {
            'player': 0,
            'opponent': 0
        }
        self.me_first_active = True


        self.battle_state = None
        self.waiting_for_input = False
        self.final_dialog = False
        self.battle_finished = False
        self.finish_token = False

        self.setup()

    def setup(self):
        self.create_pokemon(self.current_player_pokemon, 'player')
        self.create_pokemon(self.current_opponent_pokemon, 'opponent')

# support methods

    def end_dialog(self):
        self.dialog_tree = None
        self.dialog_input_overlap = True
        if self.workflow[self.indexes['workflow']] == 'start_effects_text':
            self.workflow_active = False
            self.indexes['workflow'] += 1
        if self.workflow[self.indexes['workflow']] == 'pre_move_text':
            self.workflow_active = False
            self.indexes['workflow'] += 1
        elif self.workflow[self.indexes['workflow']] == 'post_move_text':
            self.workflow_active = False
            self.indexes['workflow'] += 1
        elif self.workflow[self.indexes['workflow']] == 'post_effect_text':
            self.workflow_active = False
            self.indexes['workflow'] += 1
        elif self.workflow[self.indexes['workflow']] == 'end_effects_text':
            self.workflow_active = False
            if self.finish_token:
                self.final_dialog = True
            else:
                if self.indexes['workflow'] + 1 == len(self.workflow):
                    self.next_round_reset()
                else:
                    self.indexes['workflow'] += 1
                    self.indexes['move_order'] += 1
                    self.indexes['move_order'] = self.indexes['move_order'] % 2

    def create_pokemon(self, pokemon, entity):
        graphic = self.pokemon_graphics['battle_sprites'][f"{pokemon.name}_back-normal" if entity == 'player' else f"{pokemon.name}_normal"]
        if entity == 'player':
            self.player_pokemon_graphic_scaled = pygame.transform.scale(graphic, (graphic.get_width()*5, graphic.get_height()*5))
        else:
            self.opponent_pokemon_graphic_scaled = pygame.transform.scale(graphic, (graphic.get_width()*5, graphic.get_height()*5))
        pokemon_sprite = PokemonSprite(
            pos = self.player_pokemon_position if entity == 'player' else self.opponent_pokemon_position,
            image = self.player_pokemon_graphic_scaled if entity == 'player' else self.opponent_pokemon_graphic_scaled,
            groups = (self.battle_sprites, self.player_sprites if entity == 'player' else self.opponent_sprites),
            pokemon = pokemon,
            entity = entity
        )
        if entity == 'player':
            self.player_pokemon_midbottom = pokemon_sprite.rect.midbottom
        stats_sprite = PokemonStatsSprite(
            pos = self.player_stats_position if entity == 'player' else self.opponent_stats_position,
            size = self.stats_size,
            pokemon = pokemon,
            entity = entity,
            groups = (self.battle_sprites, self.player_sprites if entity == 'player' else self.opponent_sprites),
            fonts = self.fonts,
            status_icons = self.status_icons
        )

    def fill_non_transparent(self, surface, colour):
        surface.lock()
        px_array = pygame.PixelArray(surface)
        
        fill_color = surface.map_rgb(colour)
        
        for y in range(surface.get_height()):
            for x in range(surface.get_width()):
                pixel_colour = surface.unmap_rgb(px_array[x, y])
                if pixel_colour[3] != 0:
                    px_array[x, y] = fill_colour
        
        surface.unlock()
        del px_array

    def get_move_effectiveness(self, atk_type, def_types):
        eff = 1
        for def_type in def_types:
            if def_type in EFFECTIVE_DATA[atk_type].keys():
                eff *= float(EFFECTIVE_DATA[atk_type][def_type])
        return eff

    def get_matchup_effectiveness(self, atk_types, def_types):
        eff = 1
        for atk_type in atk_types:
            for def_type in def_types:
                if def_type in EFFECTIVE_DATA[atk_type].keys():
                    eff *= float(EFFECTIVE_DATA[atk_type][def_type])
        return eff

    def get_critical(self, moving_pokemon, affected_pokemon, move_used):
        threshold = 0
        effective_crit_mod = moving_pokemon.critical_hit_mod + \
            MOVE_DATA[move_used]['meta']['crit_rate'] + \
            1 if moving_pokemon.held_item == 'razor-claw' or moving_pokemon.held_item == 'scope-lens' else 0 + \
            1 if moving_pokemon.ability == 'super-luck' else 0
        if effective_crit_mod == 0:
            threshold = 1/16
        elif effective_crit_mod == 1:
            threshold = 1/8
        elif effective_crit_mod == 2:
            threshold = 1/2
        elif effective_crit_mod >= 3:
            threshold = 1
        
        if random.random() < threshold:
            return True
        else:
            return False

    def stage_to_factor(self, stat):
        if stat >= 0:
            return (stat + 2)/2
        if stat < 0:
            return 2/(2 + abs(stat))

    def stage_to_factor_acc(self, stat):
        if stat >= 0:
            return (100 + stat * (100/3))/100
        if stat < 0:
            return ((100/9) * stat + 100)/100

    def calculate_experience(self):
        """
        Calculate and distribute experience points to the player's Pokémon.
        """
        fainted_opponent = self.current_opponent_pokemon
        base_xp = pokemon_data.POKEMON_DATA[fainted_opponent.name]['base_experience']
        
        for pokemon in list(self.player_pokemon.values()):
            if pokemon.current_hp > 0:  # Only non-fainted Pokémon earn experience
                xp_gain = math.floor((base_xp * fainted_opponent.level) / 7)
                pokemon.current_xp += xp_gain
                self.end_effects_dialog_stack.append(f"{pokemon.name.capitalize()} gained {xp_gain} EXP points!")
                
                # Check for level up
                if pokemon.current_xp >= pokemon.level_xp:
                    extra_xp = pokemon.current_xp - pokemon.level_xp
                    self.level_up(pokemon, extra_xp)

    def decide_order(self):
        player_speed = self.current_player_pokemon.real_stats['Speed'] * self.stage_to_factor(self.current_player_pokemon.stat_mods['Speed'])
        opponent_speed = self.current_opponent_pokemon.real_stats['Speed'] * self.stage_to_factor(self.current_opponent_pokemon.stat_mods['Speed'])
        player_move_priority = MOVE_DATA[self.player_chosen_action['move']]['priority']
        opponent_move_priority = MOVE_DATA[self.opponent_chosen_action['move']]['priority']

        if player_move_priority == opponent_move_priority:
            if player_speed > opponent_speed:
                return ['player', 'opponent']
            else:
                return ['opponent', 'player']
        elif player_move_priority > opponent_move_priority:
            return ['player', 'opponent']
        else:
            return ['opponent', 'player']

    def decide_opponent_action(self):
        return {'option': 'fight', 'move': random.choice([self.current_opponent_pokemon.moves[index]['name'] for index in range(len(self.current_opponent_pokemon.moves)) if self.current_opponent_pokemon.moves[index] is not None])}

    def update_all_pokemon(self, option):
        for pokemon_sprite in self.player_sprites.sprites() + self.opponent_sprites.sprites():
            pokemon_sprite.pokemon.paused = True if option == 'pause' else False

    def next_round_reset(self):
        self.indexes['workflow'] = 0
        self.indexes['move_order'] = 0
        self.round_number += 1
        self.selection_mode = 'menu'
        self.player_chosen_action = None
        self.opponent_chosen_action = None
        self.action_chosen = None
        self.attack_missed = None
        self.indexes['menu'] = 0
        self.indexes['fight'] = 0
        self.indexes['bag'] = 0
        self.indexes['bag_category'] = 0
        self.indexes['bag_option'] = 0
        self.indexes['bag_pokemon_option'] = 0
        self.indexes['party'] = (0,0)
        self.indexes['pokemon_option'] = 0
        self.indexes['pokemon_stats_move'] = 0
        self.party_option_select = False
        self.party_open = False
        self.bag_option_select = False
        self.bag_option_pokemon_select = False
        self.bag_open = False
        self.multi_hit_number = None
        
        # Resetting Pokémon action capabilities
        self.current_player_pokemon.can_move = True
        self.current_opponent_pokemon.can_move = True

# battle flow methods

    def evaluate_chosen_action(self):
        if self.player_chosen_action['option'] == 'run':
            self.run_attempt_counter += 1
            odds_escape = (math.floor((self.current_player_pokemon.real_stats['Speed']*32)/(self.current_opponent_pokemon.real_stats['Speed']/4))+(30*self.run_attempt_counter))
            random_run = random.randint(0, 256)
            if odds_escape > random_run:
                self.dialog_tree = DialogTree(self.all_sprites, self.fonts['dialog'], self.display_surface, self.end_dialog, narration=BATTLE_TEXT['fail run'])
            else:
                self.dialog_tree = DialogTree(self.all_sprites, self.fonts['dialog'], self.display_surface, self.end_dialog, narration=BATTLE_TEXT['success run'])
                self.final_dialog = True

        if self.player_chosen_action['option'] == 'use':
            item_name = self.player_chosen_action['item']
            if 'balls' in ITEM_DATA[item_name]['category']:
                self.catch_result = self.calculate_catch(item_name)
                self.start_catch_anim = True
                if self.catch_result:
                    box_or_party = self.resolve_caught_pokemon()
                    if box_or_party == 'box':
                        self.dialog_tree = DialogTree(self.all_sprites, self.fonts['dialog'],self.display_surface, self.end_dialog, narration=[f"Gotcha! {self.current_opponent_pokemon.name.capitalize()} was caught!", f"Oops! You've got no space for {self.current_opponent_pokemon.name.capitalize()} in your party!",f"Sending {self.current_opponent_pokemon.name.capitalize()} to your box..."])
                        self.final_dialog = True
                    if box_or_party == 'party':
                        self.dialog_tree = DialogTree(self.all_sprites, self.fonts['dialog'],self.display_surface, self.end_dialog, narration=[f"Gotcha! {self.current_opponent_pokemon.name.capitalize()} was caught!", f"Adding {self.current_opponent_pokemon.name.capitalize()} to your party!"])
                        self.final_dialog = True
                else:
                    self.dialog_tree = DialogTree(self.all_sprites, self.fonts['dialog'],self.display_surface, self.end_dialog, narration=BATTLE_TEXT[f'shake {self.shake_number}'])
            self.move_order = ['player', 'opponent']

        if self.player_chosen_action['option'] == 'switch':
            self.move_order = ['player', 'opponent']

        if self.player_chosen_action['option'] == 'fight':
            self.move_order = self.decide_order()

    def calculate_catch(self, ball_name):
        ball_bonus = 1

        if ball_name == 'lure' and self.was_fished:
            ball_bonus = 3
        if ball_name == 'master':
            return True
        if ball_name == 'heal':
            self.caught_with_heal_ball = True
        if ball_name == 'repeat':
            if self.current_opponent_pokemon.name in player_data.CAUGHT_POKEMON:
                ball_bonus = 3
        if ball_name == 'friend':
            self.caught_with_friend_ball = True
        if ball_name == 'moon':
            if self.current_opponent_pokemon.name in ['nidorina', 'nidorino', 'clefairy', 'jigglypuff', 'skitty', 'munna']:
                ball_bonus = 3
        if ball_name == 'timer':
            ball_bonus += self.round_number*0.1
        if ball_name == 'dive':
            if self.current_area == 'water':
                ball_bonus = 3.5
        if ball_name == 'level':
            p_level = self.current_player_pokemon.level
            o_level = self.current_opponent_pokemon.level
            if o_level < p_level < o_level*2:
                ball_bonus = 2
            if o_level*2 < p_level < o_level*4:
                ball_bonus = 4
            if o_level*4 < p_level:
                ball_bonus = 8
        if ball_name == 'quick':
            if self.round_number == 1:
                ball_bonus = 4
        if ball_name == 'net':
            if 'water' in self.current_opponent_pokemon.type or 'bug' in self.current_opponent_pokemon.type:
                ball_bonus = 3
        if ball_name == 'dusk':
            if self.current_area == 'cave' or self.current_area == 'deep_cave':
                ball_bonus = 3.5
        if ball_name == 'ultra':
            ball_bonus = 2
        if ball_name == 'nest':
            if self.current_opponent_pokemon.level < 30:
                ball_bonus = (40 - self.current_opponent_pokemon.level)/10
        if ball_name == 'love':
            if ((self.current_opponent_pokemon.gender == 'male' and self.current_player_pokemon.gender == 'female') or (self.current_opponent_pokemon.gender == 'female' and self.current_player_pokemon.gender == 'male')) and pokemon_data.POKEMON_DATA[self.current_player_pokemon.name]['species'] == pokemon_data.POKEMON_DATA[self.current_opponent_pokemon.name]['species']:
                ball_bonus = 8
        if ball_name == 'fast':
            if self.current_opponent_pokemon.base_stats['Speed'] >= 100:
                ball_bonus = 4
        if ball_name == 'heavy':
            for i in range(5):
                if i*100 < self.current_opponent_pokemon.weight <= (i+1)*100-0.1:
                    ball_bonus = i if i != 0 else 0.5
        if ball_name == 'great':
            ball_bonus = 1.5

        status_bonus = 1

        if self.current_opponent_pokemon.status in ['freeze', 'sleep']:
            status_bonus = 2
        if self.current_opponent_pokemon.status in ['paralysis', 'burn', 'poison']:
            status_bonus = 1.5

        random_num = random.randint(0, 256)
        a = (3*self.current_opponent_pokemon.max_hp - 2*self.current_opponent_pokemon.current_hp)/(3*self.current_opponent_pokemon.max_hp)* pokemon_data.CATCH_RATES[self.current_opponent_pokemon.name] * ball_bonus * status_bonus
        if random_num <= a:
            return True
        return False

    def resolve_caught_pokemon(self):
        if self.caught_with_heal_ball:
            self.current_opponent_pokemon.cure_all()
        if self.caught_with_friend_ball:
            self.current_opponent_pokemon.happiness += 200
        free_party_slot_index = 0
        for i in range(len(player_data.POKEMON)):
            if player_data.POKEMON[i] is None:
                free_party_slot_index = i
                break
        if free_party_slot_index == 0:
            player_data.BOX[len(player_data.BOX) - 1] = self.current_opponent_pokemon
            return 'box'
        else:
            player_data.POKEMON[free_party_slot_index] = self.current_opponent_pokemon
            return 'party'

    def update_status_effects(self, pokemon):
        """
        Applies status effects at the end of each turn.
        """
        if pokemon.status_effect == 'paralysis':
            # 25% chance to be unable to move due to paralysis
            if random.random() <= 0.25:
                self.dialog_tree = DialogTree(self.all_sprites, self.fonts['dialog'], self.display_surface, self.end_dialog, narration=[f"{pokemon.name.title()} is paralysed and can't move!"])
                pokemon.can_move = False
            else:
                pokemon.can_move = True

        elif pokemon.status_effect == 'sleep':
            # Sleep counter, Pokémon wakes up after a few turns
            if pokemon.sleep_turns > 0:
                pokemon.sleep_turns -= 1
                self.dialog_tree = DialogTree(self.all_sprites, self.fonts['dialog'], self.display_surface, self.end_dialog, narration=[f"{pokemon.name.title()} is fast asleep."])
                pokemon.can_move = False
            else:
                pokemon.status_effect = None
                self.dialog_tree = DialogTree(self.all_sprites, self.fonts['dialog'], self.display_surface, self.end_dialog, narration=[f"{pokemon.name.title()} woke up!"])
                pokemon.can_move = True

        elif pokemon.status_effect == 'poison':
            # Poison damage each turn
            damage = max(1, pokemon.max_hp // 8)  # 1/8th of max HP
            pokemon.current_hp -= damage
            self.end_effects_dialog_stack.append(f"{pokemon.name.title()} was hurt by poison!")

        elif pokemon.status_effect == 'toxic':
            # Toxic poison, increasing damage over time
            pokemon.toxic_turns += 1
            damage = max(1, (pokemon.max_hp // 16) * pokemon.toxic_turns)  # Increasing damage each turn
            pokemon.current_hp -= damage
            self.end_effects_dialog_stack.append(f"{pokemon.name.title()} was badly poisoned!")

        elif pokemon.status_effect == 'burn':
            # Burn damage each turn, halved attack
            damage = max(1, pokemon.max_hp // 16)  # 1/16th of max HP
            pokemon.current_hp -= damage
            self.end_effects_dialog_stack.append(f"{pokemon.name.title()} was hurt by its burn!")
            # Attack is halved if burned
            pokemon.attack_multiplier = 0.5

        elif pokemon.status_effect == 'freeze':
            # Pokémon remains frozen with a small chance to thaw each turn
            if random.random() <= 0.2:
                pokemon.status_effect = None
                self.dialog_tree = DialogTree(self.all_sprites, self.fonts['dialog'], self.display_surface, self.end_dialog, narration=[f"{pokemon.name.title()} thawed out!"])
            else:
                self.dialog_tree = DialogTree(self.all_sprites, self.fonts['dialog'], self.display_surface, self.end_dialog, narration=[f"{pokemon.name.title()} is frozen solid!"])
                pokemon.can_move = False

        elif pokemon.status_effect == 'confusion':
            # Pokémon has a 50% chance to hurt itself while confused
            if random.random() <= 0.5:
                # Confusion self-damage uses physical attack stats
                damage = max(1, pokemon.level * 0.2 * (pokemon.real_stats['Atk'] / pokemon.real_stats['Def']))
                pokemon.current_hp -= int(damage)
                self.dialog_tree = DialogTree(self.all_sprites, self.fonts['dialog'], self.display_surface, self.end_dialog, narration=[f"{pokemon.name.title()} hurt itself in confusion!"])
            else:
                self.dialog_tree = DialogTree(self.all_sprites, self.fonts['dialog'], self.display_surface, self.end_dialog, narration=[f"{pokemon.name.title()} snapped out of confusion!"])
                pokemon.status_effect = None

        elif pokemon.status_effect == 'infatuation':
            # 50% chance to be immobilized by love
            if random.random() <= 0.5:
                self.dialog_tree = DialogTree(self.all_sprites, self.fonts['dialog'], self.display_surface, self.end_dialog, narration=[f"{pokemon.name.title()} is in love and can't move!"])
                pokemon.can_move = False

        elif pokemon.status_effect == 'curse':
            # Pokémon loses 1/4th HP each turn from a Ghost's curse
            damage = max(1, pokemon.max_hp // 4)
            pokemon.current_hp -= damage
            self.end_effects_dialog_stack.append(f"{pokemon.name.title()} is afflicted by the curse!")

        elif pokemon.status_effect == 'trap':
            # Pokémon is trapped and can't switch or escape
            self.end_effects_dialog_stack.append(f"{pokemon.name.title()} is trapped and can't escape!")

    def start_effects(self):
        """
        Handles the beginning of the turn and applies status effects that affect move order or action availability.
        """
        moving_pokemon = self.current_player_pokemon if self.move_order[self.indexes['move_order']] == 'player' else self.current_opponent_pokemon
        affected_pokemon = self.current_opponent_pokemon if self.move_order[self.indexes['move_order']] == 'player' else self.current_player_pokemon

        for pokemon in [self.current_player_pokemon, self.current_opponent_pokemon]:
            if pokemon.status_effect in ['freeze', 'sleep', 'paralysis']:
                self.update_status_effects(pokemon)

    def apply_end_turn_effects(self):
        """
        Applies status effects like poison, burn, and toxic at the end of each turn.
        """
        for pokemon in [self.current_player_pokemon, self.current_opponent_pokemon]:
            if pokemon.status_effect in ['poison', 'toxic', 'burn']:
                self.update_status_effects(pokemon)

    def start_effects_text(self):
        if len(self.start_effects_dialog_stack) > 0:
            self.dialog_tree = DialogTree(self.all_sprites, self.fonts['dialog'], self.display_surface, self.end_dialog, narration=[self.start_effects_dialog_stack[0]])
            if len(self.start_effects_dialog_stack) == 1:
                self.start_effects_dialog_stack = []
            else:
                self.start_effects_dialog_stack = self.start_effects_dialog_stack[1:]

    def pre_move_text(self):
        if self.player_chosen_action['option'] == 'switch' and self.move_order[self.indexes['move_order']] == 'player':
            text = random.choice([f'Go! {self.order[self.indexes['party'][1]][self.indexes['party'][0]].name.title()}!', f"Let's see what {self.order[self.indexes['party'][1]][self.indexes['party'][0]].name.title()} can do!", f"Go get em', {self.order[self.indexes['party'][1]][self.indexes['party'][0]].name.title()}"])
            self.dialog_tree = DialogTree(self.all_sprites, self.fonts['dialog'], self.display_surface, self.end_dialog, narration=[text])
        else:
            self.dialog_tree = DialogTree(self.all_sprites, self.fonts['dialog'], self.display_surface, self.end_dialog, narration=[f"{self.current_player_pokemon.name.capitalize() if self.move_order[self.indexes['move_order']] == 'player' else self.current_opponent_pokemon.name.capitalize()} used {self.player_chosen_action['move'].title() if self.move_order[self.indexes['move_order']] == 'player' else self.opponent_chosen_action['move'].title()}!"])

    def resolve_move_damage(self):
        """
        Handles the damage calculation when a move is executed and takes status conditions into account.
        """
        moving_pokemon = self.current_player_pokemon if self.move_order[self.indexes['move_order']] == 'player' else self.current_opponent_pokemon
        affected_pokemon = self.current_opponent_pokemon if self.move_order[self.indexes['move_order']] == 'player' else self.current_player_pokemon
        move_used = self.player_chosen_action['move'] if self.move_order[self.indexes['move_order']] == 'player' else self.opponent_chosen_action['move']

        # If the Pokémon is frozen, paralyzed, or asleep, it may not attack
        if not moving_pokemon.can_move:
            return

        # accuracy
        move_accuracy = MOVE_DATA[move_used]['accuracy']
        if move_accuracy is not None: # if not guaranteed hit
            accuracy_modified = move_accuracy * self.stage_to_factor_acc(moving_pokemon.accuracy_mod)
            rand_val = random.randint(0, 100)
            if accuracy_modified < rand_val: # if miss
                self.post_move_text_dialog_stack.append(f"{self.current_player_pokemon.name.capitalize() if self.move_order[self.indexes['move_order']] == 'player' else ("The foe's" + self.current_opponent_pokemon.name.capitalize())} missed!")
                self.attack_missed = True
                return

        # damage
        damage_class = MOVE_DATA[move_used]['damage_class']
        if damage_class != 'status':

            level = moving_pokemon.level
            power = MOVE_DATA[move_used]['power']
            eff_atk = moving_pokemon.real_stats['Atk'] * self.stage_to_factor(moving_pokemon.stat_mods['Atk']) if damage_class == 'physical' else moving_pokemon.real_stats['SpAtk'] * self.stage_to_factor(moving_pokemon.stat_mods['SpAtk'])
            eff_def = affected_pokemon.real_stats['Def'] * self.stage_to_factor(affected_pokemon.stat_mods['Def']) if damage_class == 'physical' else affected_pokemon.real_stats['SpDef'] * self.stage_to_factor(affected_pokemon.stat_mods['SpDef'])
            burn = 1 if moving_pokemon.status_effect != 'burn' else 0.5
            screen = 1 if (damage_class != 'physical' and not self.reflect_up[self.move_order[self.indexes['move_order']]]) or (damage_class != 'special' and not self.light_screen_up[self.move_order[self.indexes['move_order']]]) else 0.5

            weather_mod = 1
            if self.weather == 'rain' and MOVE_DATA[move_used]['type'] == 'water':
                weather_mod = 1.5
            elif self.weather == 'harsh-sunlight' and MOVE_DATA[move_used]['type'] == 'fire':
                weather_mod = 1.5
            elif self.weather == 'rain' and MOVE_DATA[move_used]['type'] == 'fire':
                weather_mod = 0.5
            elif self.weather == 'harsh-sunlight' and MOVE_DATA[move_used]['type'] == 'water':
                weather_mod = 0.5

            ff = 1 if not self.flash_fire_active[self.move_order[self.indexes['move_order']]] else 1.5
            critical = 1
            if self.get_critical(moving_pokemon, affected_pokemon, move_used):
                critical = 2
                self.post_move_text_dialog_stack.append('A critical hit!')

            item = 1 
            if moving_pokemon.held_item == 'life-orb':
                item = 1.3
            if moving_pokemon.held_item == 'metronome':
                item = 1 + (min(self.metronome_counter[self.move_order[self.indexes['move_order']]], 10) / 10)
            
            first = 1 if not self.me_first_active else 1.5
            random_mod = random.randint(85, 100)/100 if move_used != 'spit-up' else 1
            
            STAB = 1
            if MOVE_DATA[move_used]['type'] in moving_pokemon.type:
                STAB = 1.5
            if moving_pokemon.ability == 'adaptability':
                STAB = 2
            
            eff = self.get_move_effectiveness(MOVE_DATA[move_used]['type'], affected_pokemon.type)
            if eff == 0:
                self.post_move_text_dialog_stack.append(f"{self.current_player_pokemon.name.capitalize() if self.move_order[self.indexes['move_order']] == 'opponent' else ("The foe's" + self.current_opponent_pokemon.name.capitalize())} is immune!")
            if eff == 0.25:
                self.post_move_text_dialog_stack.append(f"It wasn't effective at all...")
            if eff == 0.5:
                self.post_move_text_dialog_stack.append(f"It wasn't very effective...")
            if eff == 2:
                self.post_move_text_dialog_stack.append(f"It was super effective!")
            if eff == 4:
                self.post_move_text_dialog_stack.append(f"It was super DUPER effective!!")
            
            SRF = 0.75 if (eff != 1) and (affected_pokemon.ability == 'solid-rock' or affected_pokemon.ability == 'filter') and (moving_pokemon.ability != 'mold-breaker') else 1
            EB = 1 if moving_pokemon.held_item != 'expert-belt' else 1.2
            TL = 1 if moving_pokemon.ability != 'tinted-lens' and eff >= 1 else 2
            berry = 1

            damage = ((((2 * level / 5) * power * (eff_atk / eff_def)) / 50) * burn * screen * weather_mod * ff + 2) * critical * item * first * random_mod * STAB * eff * SRF * EB * TL * berry

            max_hits = MOVE_DATA[move_used]['meta']['max_hits']
            min_hits = MOVE_DATA[move_used]['meta']['min_hits']
            if max_hits is not None and min_hits is not None:
                damage = damage * random.randint(min_hits, max_hits)

            affected_pokemon.current_hp -= int(damage) if affected_pokemon.current_hp >= int(damage) else affected_pokemon.current_hp

            if MOVE_DATA[move_used]['meta']['drain'] != 0:
                drain = ((((2 * level / 5) * MOVE_DATA[move_used]['meta']['drain'] * (eff_atk / eff_def)) / 50) * burn * screen * weather_mod * ff + 2) * critical * item * first * random_mod * STAB * eff * SRF * EB * TL * berry
                moving_pokemon.current_hp += int(drain) if (moving_pokemon.max_hp - moving_pokemon.current_hp >= int(drain)) else (moving_pokemon.max_hp - moving_pokemon.current_hp)
                self.post_move_text_dialog_stack.append(f"{moving_pokemon.name.capitalize()} drained {affected_pokemon.name.capitalize()}'s health!")

    def apply_effects(self):
        moving_pokemon = self.current_player_pokemon if self.move_order[self.indexes['move_order']] == 'player' else self.current_opponent_pokemon
        affected_pokemon = self.current_opponent_pokemon if self.move_order[self.indexes['move_order']] == 'player' else self.current_player_pokemon
        chosen_action = self.player_chosen_action if self.move_order[self.indexes['move_order']] == 'player' else self.opponent_chosen_action

        move_used = chosen_action['move']

        if not self.attack_missed or chosen_action['option'] not in ['switch', 'run', 'use']:

            stat_changes = MOVE_DATA[move_used]['stat_changes']
            effect_chance = MOVE_DATA[move_used]['effect_chance']
            affected = False
            if effect_chance != 100 and effect_chance is not None and effect_chance != 0:
                if random.random() <= effect_chance/100:
                    affected = True
            if len(stat_changes) != 0 and affected:
                for stat_change in stat_changes:
                    stat = stat_change['stat']['name']
                    stat_text = None
                    if stat == 'Atk':
                        stat_text = 'Attack'
                    if stat == 'Def':
                        stat_text = 'Defense'
                    if stat == 'SpAtk':
                        stat_text = 'Special Attack'
                    if stat == 'SpDef':
                        stat_text = 'Special Defense'
                    if stat == 'Speed':
                        stat_text = 'Speed'
                    change = stat_change['change']
                    change_mem = change
                    targeted_pokemon_entity_stat_change = None
                    targeted_pokemon_entity_status_change = None

                    if MOVE_DATA[move_used]['target'] in ['selected-pokemon', 'all-other-pokemon', 'all-opponents']:
                        if change + affected_pokemon.stat_mods[stat] > 6:
                            change = change + affected_pokemon.stat_mods[stat] - 6
                        if change + affected_pokemon.stat_mods[stat] < -6:
                            change = change + affected_pokemon.stat_mods[stat] + 6
                        affected_pokemon.stat_mods[stat] += change
                        targeted_pokemon_entity_stat_change = 'affected'

                        if abs(change_mem) > abs(change):
                            if change_mem < 0:
                                self.post_effect_text_dialog_stack.append(f"{affected_pokemon.name.capitalize()}'s {stat_text} can't go any lower!")
                            elif change_mem > 0:
                                self.post_effect_text_dialog_stack.append(f"{affected_pokemon.name.capitalize()}'s {stat_text} can't go any higher!")
                        else:
                            if change_mem == 3:
                                self.post_effect_text_dialog_stack.append(f"{affected_pokemon.name.capitalize()}'s {stat_text} drastically rose!")
                            if change_mem == 2:
                                self.post_effect_text_dialog_stack.append(f"{affected_pokemon.name.capitalize()}'s {stat_text} sharply rose!")
                            if change_mem == 1:
                                self.post_effect_text_dialog_stack.append(f"{affected_pokemon.name.capitalize()}'s {stat_text} rose!")
                            if change_mem == -1:
                                self.post_effect_text_dialog_stack.append(f"{affected_pokemon.name.capitalize()}'s {stat_text} fell!")
                            if change_mem == -2:
                                self.post_effect_text_dialog_stack.append(f"{affected_pokemon.name.capitalize()}'s {stat_text} sharply fell!")
                            if change_mem == -3:
                                self.post_effect_text_dialog_stack.append(f"{affected_pokemon.name.capitalize()}'s {stat_text} drastically fell!")
                        
                    if MOVE_DATA[move_used]['target'] == 'user':
                        if change + moving_pokemon.stat_mods[stat] > 6:
                            change = change + moving_pokemon.stat_mods[stat] - 6
                        if change + moving_pokemon.stat_mods[stat] < -6:
                            change = change + moving_pokemon.stat_mods[stat] + 6
                        moving_pokemon.stat_mods[stat] += change
                        
                        if abs(change_mem) > abs(change):
                            if change_mem < 0:
                                self.post_effect_text_dialog_stack.append(f"{moving_pokemon.name.capitalize()}'s {stat_text} can't go any lower!")
                            elif change_mem > 0:
                                self.post_effect_text_dialog_stack.append(f"{moving_pokemon.name.capitalize()}'s {stat_text} can't go any higher!")
                        else:
                            if change_mem == 3:
                                self.post_effect_text_dialog_stack.append(f"{moving_pokemon.name.capitalize()}'s {stat_text} drastically rose!")
                            if change_mem == 2:
                                self.post_effect_text_dialog_stack.append(f"{moving_pokemon.name.capitalize()}'s {stat_text} sharply rose!")
                            if change_mem == 1:
                                self.post_effect_text_dialog_stack.append(f"{moving_pokemon.name.capitalize()}'s {stat_text} rose!")
                            if change_mem == -1:
                                self.post_effect_text_dialog_stack.append(f"{moving_pokemon.name.capitalize()}'s {stat_text} fell!")
                            if change_mem == -2:
                                self.post_effect_text_dialog_stack.append(f"{moving_pokemon.name.capitalize()}'s {stat_text} sharply fell!")
                            if change_mem == -3:
                                self.post_effect_text_dialog_stack.append(f"{moving_pokemon.name.capitalize()}'s {stat_text} drastically fell!")
            
            if MOVE_DATA[move_used]['meta']['ailment']['name'] != 'none':
                
                ailment = MOVE_DATA[move_used]['meta']['ailment']['name']
                if MOVE_DATA[move_used]['target'] in ['selected-pokemon', 'all-other-pokemon', 'all-opponents']:
                    if affected_pokemon.status_effect == ailment:
                        self.already_affected = True
                    else:
                        affected_pokemon.status_effect = ailment
                        self.already_affected = False

                    if ailment == 'paralysis':
                        self.post_effect_text_dialog_stack.append(f"{affected_pokemon.name.capitalize()} {'was' if not self.already_affected else 'is already'} paralysed!")
                    elif ailment == 'burn':
                        self.post_effect_text_dialog_stack.append(f"{affected_pokemon.name.capitalize()} {'was' if not self.already_affected else 'is already'} burned!")
                    elif ailment == 'poison':
                        self.post_effect_text_dialog_stack.append(f"{affected_pokemon.name.capitalize()} {'was' if not self.already_affected else 'is already'} poisoned!")
                    elif ailment == 'toxic':
                        self.post_effect_text_dialog_stack.append(f"{affected_pokemon.name.capitalize()} {'was' if not self.already_affected else 'is already'} badly poisoned!")
                    elif ailment == 'freeze':
                        self.post_effect_text_dialog_stack.append(f"{affected_pokemon.name.capitalize()} {'was' if not self.already_affected else 'is already'} frozen!")
                    elif ailment == 'sleep':
                        self.post_effect_text_dialog_stack.append(f"{affected_pokemon.name.capitalize()} {'fell' if not self.already_affected else 'is already'} asleep!")
                    elif ailment == 'confusion':
                        self.post_effect_text_dialog_stack.append(f"{affected_pokemon.name.capitalize()} {'became' if not self.already_affected else 'is already'} confused!")
                    elif ailment == 'infatuation':
                        self.post_effect_text_dialog_stack.append(f"{affected_pokemon.name.capitalize()} {'became' if not self.already_affected else 'is already'} infatuated!")
                    elif ailment == 'trap':
                        self.post_effect_text_dialog_stack.append(f"{affected_pokemon.name.capitalize()} can't escape!")
                    elif ailment == 'curse':
                        self.post_effect_text_dialog_stack.append(f"{affected_pokemon.name.capitalize()} {'was' if not self.already_affected else 'is already'} cursed!")
                    elif ailment == 'flinch':
                        self.post_effect_text_dialog_stack.append(f"{affected_pokemon.name.capitalize()} flinched and couldn’t move!")

                elif MOVE_DATA[move_used]['target'] == 'user':
                    if moving_pokemon.status_effect == ailment:
                        self.already_affected = True
                    else:
                        moving_pokemon.status_effect = ailment
                        self.already_affected = False

                    if ailment == 'paralysis':
                        self.post_effect_text_dialog_stack.append(f"{moving_pokemon.name.capitalize()} {'was' if not self.already_affected else 'is already'} paralysed!")
                    elif ailment == 'burn':
                        self.post_effect_text_dialog_stack.append(f"{moving_pokemon.name.capitalize()} {'was' if not self.already_affected else 'is already'} burned!")
                    elif ailment == 'poison':
                        self.post_effect_text_dialog_stack.append(f"{moving_pokemon.name.capitalize()} {'was' if not self.already_affected else 'is already'} poisoned!")
                    elif ailment == 'toxic':
                        self.post_effect_text_dialog_stack.append(f"{moving_pokemon.name.capitalize()} {'was' if not self.already_affected else 'is already'} badly poisoned!")
                    elif ailment == 'freeze':
                        self.post_effect_text_dialog_stack.append(f"{moving_pokemon.name.capitalize()} {'was' if not self.already_affected else 'is already'} frozen!")
                    elif ailment == 'sleep':
                        self.post_effect_text_dialog_stack.append(f"{moving_pokemon.name.capitalize()} {'fell' if not self.already_affected else 'is already'} asleep!")
                    elif ailment == 'confusion':
                        self.post_effect_text_dialog_stack.append(f"{moving_pokemon.name.capitalize()} {'became' if not self.already_affected else 'is already'} confused!")
                    elif ailment == 'infatuation':
                        self.post_effect_text_dialog_stack.append(f"{moving_pokemon.name.capitalize()} {'became' if not self.already_affected else 'is already'} infatuated!")
                    elif ailment == 'trap':
                        self.post_effect_text_dialog_stack.append(f"{moving_pokemon.name.capitalize()} can't escape!")
                    elif ailment == 'curse':
                        self.post_effect_text_dialog_stack.append(f"{moving_pokemon.name.capitalize()} {'was' if not self.already_affected else 'is already'} cursed!")
                    elif ailment == 'flinch':
                        self.post_effect_text_dialog_stack.append(f"{moving_pokemon.name.capitalize()} flinched and couldn’t move!")

    def post_move_text(self):
        if len(self.post_move_text_dialog_stack) != 0:
            self.dialog_tree = DialogTree(self.all_sprites, self.fonts['dialog'], self.display_surface, self.end_dialog, narration=[self.post_move_text_dialog_stack[0]])
            if len(self.post_move_text_dialog_stack) == 1:
                self.post_move_text_dialog_stack = []
            else:
                self.post_move_text_dialog_stack = self.post_move_text_dialog_stack[1:]

    def post_effect_text(self):
        if len(self.post_effect_text_dialog_stack) != 0:
            self.dialog_tree = DialogTree(self.all_sprites, self.fonts['dialog'], self.display_surface, self.end_dialog, narration=[self.post_effect_text_dialog_stack[0]])
            if len(self.post_effect_text_dialog_stack) == 1:
                self.post_effect_text_dialog_stack = []
            else:
                self.post_effect_text_dialog_stack = self.post_effect_text_dialog_stack[1:]

    def end_effects(self):
        moving_pokemon = self.current_player_pokemon if self.move_order[self.indexes['move_order']] == 'player' else self.current_opponent_pokemon
        affected_pokemon = self.current_opponent_pokemon if self.move_order[self.indexes['move_order']] == 'player' else self.current_player_pokemon
        chosen_action = self.player_chosen_action if self.move_order[self.indexes['move_order']] == 'player' else self.opponent_chosen_action
        
        if self.indexes['move_order'] == 1:
            self.apply_end_turn_effects()

    def end_effects_text(self):
        if len(self.end_effects_dialog_stack) != 0:
            self.dialog_tree = DialogTree(self.all_sprites, self.fonts['dialog'], self.display_surface, self.end_dialog, narration=[self.end_effects_dialog_stack[0]])
            if len(self.end_effects_dialog_stack) == 1:
                self.end_effects_dialog_stack = []
            else:
                self.end_effects_dialog_stack = self.end_effects_dialog_stack[1:]

    def switch_pokemon(self, entity, pokemon_to_swap_into):
        if entity == 'player':
            self.battle_sprites.remove(*self.player_sprites)
            self.player_sprites.empty()
            self.current_player_pokemon.reset_stat_mods()
            self.current_player_pokemon = pokemon_to_swap_into
            self.create_pokemon(pokemon_to_swap_into, 'player')
        else:
            self.battle_sprites.remove(*self.opponent_sprites)
            self.opponent_sprites.empty()
            self.current_opponent_pokemon.reset_stat_mods()
            self.current_opponent_pokemon = pokemon_to_swap_into
            self.create_pokemon(pokemon_to_swap_into, 'opponent')

    def update_fainting_and_experience(self):
        """
        Handles fainting mechanics and experience distribution after an opponent Pokémon is fainted.
        """
        # Check if any Pokémon fainted
        for pokemon in [self.current_player_pokemon, self.current_opponent_pokemon]:
            if pokemon.current_hp <= 0:
                self.battle_state = 'fainting'
                self.waiting_for_input = True
                if pokemon == self.current_player_pokemon:
                    self.fainting_sequence(pokemon, 'player')
                else:
                    self.fainting_sequence(pokemon, 'opponent')

    def fainting_sequence(self, pokemon, entity):
        """
        Handles the fainting of a Pokémon, sets up the dialog and next steps.
        """        
        if entity == 'opponent':
            self.end_effects_dialog_stack.append(f"{pokemon.name.capitalize()} fainted!")

            self.calculate_experience()  # Add the experience calculation here

        elif entity == 'player':
            self.end_effects_dialog_stack.append(f"{pokemon.name.capitalize()} fainted!")

            if not all(pokemon.current_hp <= 0 for pokemon in list(self.player_pokemon.values())):
                self.indexes['workflow'] = 0
                self.selection_mode = 'party'
                self.party_open = False
                self.party_option_select = False
                self.switch_party_selection_mode = True
            else:
                self.end_effects_dialog_stack.append(f"You have no more Pokémon!")
                self.finish_token = True  # End the battle when all player Pokémon faint

                self.end_effects_dialog_stack.append(f"{pokemon.name.capitalize()} fainted!")
                
                if not all(pokemon.current_hp <= 0 for pokemon in list(self.player_pokemon.values())):
                    self.indexes['workflow'] = 0
                    self.selection_mode = 'party'
                    self.party_open = False
                    self.party_option_select = False
                    self.switch_party_selection_mode = True
                else:
                    self.end_effects_dialog_stack.append(f"You have no more pokemon!")
                    self.finish_token = True

    def calculate_experience(self):
        """
        Calculate and distribute experience points to the player's Pokémon.
        """
        fainted_opponent = self.current_opponent_pokemon
        base_xp = pokemon_data.POKEMON_DATA[fainted_opponent.name]['base_experience']
        
        for pokemon in list(self.player_pokemon.values()):
            if pokemon.current_hp > 0:  # Only non-fainted Pokémon earn experience
                xp_gain = math.floor((base_xp * fainted_opponent.level) / 7)
                pokemon.current_xp += xp_gain

                # Check for level up
                if pokemon.current_xp >= pokemon.level_xp:
                    extra_xp = pokemon.current_xp - pokemon.level_xp
                    self.level_up(pokemon, extra_xp)

    def level_up(self, pokemon, extra_xp):
        """
        Handles the levelling up of a Pokémon.
        """
        pokemon.level += 1
        pokemon.current_xp = extra_xp
        pokemon.level_xp = (pokemon.level+1)**3-pokemon.level**3  # Increase exp requirement for next level
        self.end_effects_dialog_stack.append(f"{pokemon.name.capitalize()} reached level {pokemon.level}!")

    def select_next_opponent_pokemon(self, player_pokemon, opponent_party):
        """
        Selects the best next Pokémon from the opponent's party based on type match-ups and health status.
        :param player_pokemon: The player's current Pokémon object.
        :param opponent_party: A list of Pokémon objects representing the opponent's party.
        :return: The selected Pokémon object from the opponent's party.
        """

        # Initialize variables to track the best match-up
        best_pokemon = None
        best_effectiveness = -1.0  # Default to a negative value to ensure we select at least one Pokémon

        # Iterate through the opponent's party to evaluate match-ups
        for opponent_pokemon in opponent_party:
            # Skip fainted Pokémon or those with status effects that prevent movement
            if opponent_pokemon.fainted or opponent_pokemon.status_effect in ['sleep', 'freeze', 'paralysis']:
                continue

            # Get the type effectiveness of the opponent's Pokémon against the player's Pokémon
            effectiveness = self.get_matchup_effectiveness(opponent_pokemon.type, player_pokemon.type)

            # Choose the Pokémon with the highest effectiveness (i.e., most favourable match-up)
            if effectiveness > best_effectiveness:
                best_effectiveness = effectiveness
                best_pokemon = opponent_pokemon

        # If all Pokémon are fainted or unusable, return None (battle should be won)
        return best_pokemon if best_pokemon else None

    def player_pressed_continue(self):
        # Handle input for continuing to the next part of the battle
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN] or keys[pygame.K_SPACE] or pygame.mouse.get_pressed()[0]:
            return True
        return False

# draw methods

    def draw_menu(self):
        for index, (option, data_dict) in enumerate(BATTLE_CHOICES.items()):
            surf = self.ui[data_dict['icon']+"_hl" if index == self.indexes['menu'] else data_dict['icon']]
            surf = pygame.transform.scale(surf, (surf.get_width()*2, surf.get_height()*2))
            rect = surf.get_frect(center = self.player_pokemon_midbottom + data_dict['pos'])
            self.display_surface.blit(surf, rect)

    def draw_fight(self):
        moves = self.current_player_pokemon.moves
        move_gap = 5
        bar_buffer = 12
        move_box_height = 66.25
        move_box_width = 246.0

        for i in range(4):
            move = moves[i]
            box_topleft_pos = self.player_pokemon_position + vector(40, -300 + (move_box_height+move_gap)*i)

            if move:
                move_data = MOVE_DATA[move['name']]

                # box
                move_box_rect = pygame.FRect(box_topleft_pos, (move_box_width, move_box_height))
                pygame.draw.rect(self.display_surface, COLOURS[move_data['type']], move_box_rect, 0, 8, 8, 8, 8)

                # name
                move_name_surf = self.fonts['regular'].render(f'{move['name'].replace('-', ' ').title()}', False, COLOURS['white'])
                move_name_rect = move_name_surf.get_frect(topleft = box_topleft_pos + vector(10,10))
                self.display_surface.blit(move_name_surf, move_name_rect)

                # move_icon
                icon_surf = self.move_type_icon[move_data['damage_class']]
                icon_surf = pygame.transform.scale(icon_surf, (icon_surf.get_width()*0.6, icon_surf.get_height()*0.6))
                icon_width = icon_surf.get_width()
                icon_height = icon_surf.get_height()
                icon_rect = icon_surf.get_frect(topleft = box_topleft_pos + vector(move_box_width - icon_width - 10, 10))
                self.display_surface.blit(icon_surf, icon_rect)
                
                # pp
                pp_surf = self.fonts['small'].render(f'PP:{move['current_pp']}/{move_data['max_pp']}', False, COLOURS['white'])
                pp_rect = pp_surf.get_frect(topleft = box_topleft_pos + vector(10, move_box_height - pp_surf.get_height() - 10))
                self.display_surface.blit(pp_surf, pp_rect)

                # power
                power_surf = self.fonts['small'].render(f'Power: {move_data['power']}' if move_data['power'] else 'Power: --', False, COLOURS['white'])
                power_rect = power_surf.get_frect(bottomleft = pp_rect.bottomright + vector(10,0))
                self.display_surface.blit(power_surf, power_rect)

                # accuracy
                acc_surf = self.fonts['small'].render(f'Acc: {move_data['accuracy']}' if move_data['accuracy'] else 'Acc: --', False, COLOURS['white'])
                acc_rect = acc_surf.get_frect(bottomleft = power_rect.bottomright + vector(10,0))
                self.display_surface.blit(acc_surf, acc_rect)

            else:
                # box
                move_box_rect = pygame.FRect(box_topleft_pos, (move_box_width, move_box_height))
                pygame.draw.rect(self.display_surface, COLOURS['grey'], move_box_rect, 0, 8, 8, 8, 8)

                # name
                move_name_surf = self.fonts['bold'].render('--', False, COLOURS['white'])
                move_name_rect = move_name_surf.get_frect(center = move_box_rect.center)
                self.display_surface.blit(move_name_surf, move_name_rect)

            if i == self.indexes['fight']:
                    # box
                    padding = 10
                    move_box_rect = pygame.FRect(box_topleft_pos - vector(padding/2, padding/2), (move_box_width + padding, move_box_height + padding))
                    pygame.draw.rect(self.display_surface, COLOURS['white'], move_box_rect, 8, 8, 8, 8, 8)

    def draw_bag(self):
        self.main_rect = pygame.FRect(0, 0, WINDOW_WIDTH*0.5, WINDOW_HEIGHT*0.6).move_to(center = (WINDOW_WIDTH/2, WINDOW_HEIGHT/2))

        self.visible_items = 7
        self.list_width = self.main_rect.width * 0.4
        self.item_height = self.main_rect.height / self.visible_items

        self.current_bag = player_data.BAG
        self.bag_open = True
        
        list_bg_rect = pygame.FRect(self.main_rect.topleft, (self.list_width, self.main_rect.height))
        pygame.draw.rect(self.display_surface, COLOURS['dark-grey'], list_bg_rect, 0, 0, 12, 0, 12, 0)

        # bag title
        title_text_surf = self.fonts['bold'].render("BAG", True, COLOURS['white'], COLOURS['dark-grey'])
        title_text_rect = title_text_surf.get_frect(bottomleft = self.main_rect.topleft + vector(15, -5))
        border_add = 6
        title_box_rect = pygame.FRect(title_text_rect.topleft + vector(-border_add * 1.75, -border_add * 1.75), (title_text_rect.width + border_add * 3.5, (title_text_rect.height + border_add * 4.5)))
        pygame.draw.rect(self.display_surface, COLOURS['water'], title_box_rect, 6, 6, 6, 6, 6)
        self.display_surface.blit(title_text_surf, title_text_rect)

        # bag category icons
        bag_icon_botright_pos = self.main_rect.topright + vector(-20, -5)
        icon_gap = 6
        padding = 4
        for i, category in enumerate(list(player_data.BAG.keys())):
            bag_icon_surf = self.bag_icons[category]
            bag_icon_surf = pygame.transform.scale(bag_icon_surf, (bag_icon_surf.get_width()*1.5, bag_icon_surf.get_width()*1.5))

            bag_icon_bg_rect = pygame.FRect(
                bag_icon_botright_pos - vector(padding*2, padding*2) - vector(bag_icon_surf.get_width(), bag_icon_surf.get_height()) - vector((bag_icon_surf.get_width()+padding*2+icon_gap)*i, 0),
                (bag_icon_surf.get_width() + padding*2, bag_icon_surf.get_height() + padding*2)
            )
            pygame.draw.rect(self.display_surface, COLOURS['white' if i == self.indexes['bag_category'] else 'grey'], bag_icon_bg_rect, 6, 6, 6, 6, 6)

            bag_icon_rect = bag_icon_surf.get_frect(center = bag_icon_bg_rect.center)
            self.display_surface.blit(bag_icon_surf, bag_icon_rect)

        data_bg_rect = pygame.FRect(self.main_rect.topleft + vector(self.list_width, 0), (self.main_rect.width - self.list_width, self.main_rect.height))
        pygame.draw.rect(self.display_surface, COLOURS['dark-grey'], data_bg_rect, 0, 12, 0, 12, 0, 0)

        category = list(player_data.BAG.keys())[self.indexes['bag_category']]
        bag_sprite_surf = self.bag_sprites[category]
        bag_sprite_surf = pygame.transform.scale(bag_sprite_surf, (bag_sprite_surf.get_width()*3, bag_sprite_surf.get_height()*3))
        bag_sprite_rect = bag_sprite_surf.get_frect(center = data_bg_rect.midtop + vector(0,data_bg_rect.height*0.333))
        self.display_surface.blit(bag_sprite_surf, bag_sprite_rect)

        category_text = None
        if category == 'balls':
            category_text = 'Poke Balls'
        if category == 'berries':
            category_text = 'Berries'
        if category == 'tms':
            category_text = 'TMs'
        if category == 'key-items':
            category_text = 'Key Items'
        if category == 'medicine':
            category_text = 'Medicine'
        if category == 'battle-items':
            category_text = 'Battle Items'
        if category == 'items':
            category_text = 'Items'
        category_surf = self.fonts['large'].render(category_text, False, COLOURS['white'])
        category_rect = category_surf.get_frect(midtop = data_bg_rect.midtop + vector(0, 15))
        self.display_surface.blit(category_surf, category_rect)

        # list entries
        v_offset = 0 if self.indexes['bag'] < self.visible_items else -(self.indexes['bag'] - self.visible_items + 1) * self.item_height
        for index, data in enumerate(player_data.BAG[category]):
            name, count = data['name'], data['count']
            bg_colour = COLOURS['grey'] if self.indexes['bag'] != index else COLOURS['light']
            top = self.main_rect.top + index * self.item_height + v_offset
            item_rect = pygame.FRect(self.main_rect.left, top, self.list_width, self.item_height)

            list_name = name.replace('-', ' ').title()
            if category == 'balls':
                list_name += ' Ball'
            if category == 'berries':
                list_name += ' Berry'
            text_surf = self.fonts['regular'].render(list_name, False, COLOURS['white'])
            text_rect = text_surf.get_frect(midleft = item_rect.midleft + vector(90, 0))

            # list item sprites
            if category == 'tms':
                icon_surf = self.item_graphics[category][MOVE_DATA[name]['type']]
            else:
                icon_surf = self.item_graphics[category][name]
            icon_surf = pygame.transform.scale(icon_surf, (icon_surf.get_width()*2, icon_surf.get_height()*2))
            icon_rect = icon_surf.get_frect(center = item_rect.midleft + vector(45, 0))

            quantity_surf = self.fonts['small'].render(str(count), False, COLOURS['white'])
            quantity_rect = quantity_surf.get_frect(midbottom = icon_rect.bottomright + vector(-5, -5))

            if item_rect.colliderect(self.main_rect):
                if item_rect.collidepoint(self.main_rect.topleft):
                    pygame.draw.rect(self.display_surface, bg_colour, item_rect, 0, 0, 12)
                elif item_rect.collidepoint(self.main_rect.bottomleft + vector(1,-1)):
                    pygame.draw.rect(self.display_surface, bg_colour, item_rect, 0, 0, 0, 0, 12, 0)
                else:
                    pygame.draw.rect(self.display_surface, bg_colour, item_rect)
                self.display_surface.blit(text_surf, text_rect)
                self.display_surface.blit(icon_surf, icon_rect)
                if category != 'tms':
                    if 'countable' in ITEM_DATA[name]['attributes']:
                        self.display_surface.blit(quantity_surf, quantity_rect)

        text_buffer = 10
        top_gap = 30
        text_bg_rect = pygame.FRect(
            vector(data_bg_rect.left + text_buffer, bag_sprite_rect.bottom + top_gap),
            (
                self.main_rect.width - self.list_width - text_buffer*2,
                data_bg_rect.bottom - (bag_sprite_rect.bottom + top_gap) - text_buffer
            )
        )
        pygame.draw.rect(self.display_surface, COLOURS['grey'], text_bg_rect, 0, 12, 12, 12, 12)

        text = None
        if category == 'tms':
            text = '\n'.join(textwrap.wrap(f"{MOVE_DATA[player_data.BAG[category][self.indexes['bag']]['name']]['flavor_text_entry']}", width=32))
        else:
            text = '\n'.join(textwrap.wrap(f"{ITEM_DATA[player_data.BAG[category][self.indexes['bag']]['name']]['flavor_text']} {ITEM_DATA[player_data.BAG[category][self.indexes['bag']]['name']]['short_effect']}", width=32))
        item_text_surf = self.fonts['regular'].render(text, False, COLOURS['white'])
        item_text_rect = item_text_surf.get_frect(topleft = text_bg_rect.topleft + vector(text_buffer, text_buffer))
        self.display_surface.blit(item_text_surf, item_text_rect)
        
        if category == 'tms':
            move_data = MOVE_DATA[player_data.BAG[category][self.indexes['bag']]['name']]

            # power
            power_surf = self.fonts['regular'].render(f'Power: {move_data['power']}' if move_data['power'] else 'Power: --', False, COLOURS['white'])
            power_rect = power_surf.get_frect(bottomleft = text_bg_rect.topleft + vector(0, -text_buffer))
            self.display_surface.blit(power_surf, power_rect)
            
            # move_icon
            icon_surf = self.move_type_icon[move_data['damage_class']]
            icon_surf = pygame.transform.scale(icon_surf, (icon_surf.get_width()*0.6, icon_surf.get_height()*0.6))
            icon_width = icon_surf.get_width()
            icon_height = icon_surf.get_height()
            icon_rect = icon_surf.get_frect(bottomleft = power_rect.topleft + vector(0, -text_buffer))
            self.display_surface.blit(icon_surf, icon_rect)
            
            # pp
            pp_surf = self.fonts['regular'].render(f'PP:{move_data['max_pp']}', False, COLOURS['white'])
            pp_rect = pp_surf.get_frect(bottomright = text_bg_rect.topright + vector(0, -text_buffer))
            self.display_surface.blit(pp_surf, pp_rect)

            # accuracy
            acc_surf = self.fonts['regular'].render(f'Acc: {move_data['accuracy']}' if move_data['accuracy'] else 'Acc: --', False, COLOURS['white'])
            acc_rect = acc_surf.get_frect(bottomright = pp_rect.topright + vector(0, -text_buffer))
            self.display_surface.blit(acc_surf, acc_rect)

        #lines
        for i in range(min(self.visible_items, len(player_data.BAG[category]))):
            y = self.main_rect.top + self.item_height * i
            left = self.main_rect.left
            right = self.main_rect.left + self.list_width
            pygame.draw.line(self.display_surface, COLOURS['light-grey'], (left, y), (right, y))
        
        #shadow
        shadow_surf = pygame.Surface((4, self.main_rect.height))
        shadow_surf.set_alpha(100)
        self.display_surface.blit(shadow_surf, (self.main_rect.left + self.list_width - 4, self.main_rect.top))

    def draw_bag_option_select(self):
        options = ['use', 'give', 'trash']
        option_gap = 8
        bar_buffer = 12
        option_box_height = 40
        option_box_width = 150

        for i, option in enumerate(options):
            box_topleft_pos = self.main_rect.bottomright + vector(-option_box_width/2, -option_box_height*5/2 + (option_box_height+option_gap)*i)

            # outline box  
            padding = 8
            option_outline_box_rect = pygame.FRect(box_topleft_pos - vector(padding/2, padding/2), (option_box_width + padding, option_box_height + padding))
            pygame.draw.rect(self.display_surface, COLOURS['grey'], option_outline_box_rect, 8, 8, 8, 8, 8)

            # box
            option_box_rect = pygame.FRect(box_topleft_pos, (option_box_width, option_box_height))
            pygame.draw.rect(self.display_surface, COLOURS['dark-grey'], option_box_rect, 0, 8, 8, 8, 8)

            # name
            option_name_surf = self.fonts['regular'].render(f'{option.upper()}', False, COLOURS['white'])
            option_name_rect = option_name_surf.get_frect(center = option_box_rect.center)
            self.display_surface.blit(option_name_surf, option_name_rect)

            if i == self.indexes['bag_option']:
                option_box_rect = pygame.FRect(box_topleft_pos - vector(padding/2, padding/2), (option_box_width + padding, option_box_height + padding))
                pygame.draw.rect(self.display_surface, COLOURS['white'], option_box_rect, 8, 8, 8, 8, 8)

    def draw_bag_option_pokemon_select(self):
        option_gap = 8
        bar_buffer = 12
        option_box_height = 40
        option_box_width = 150

        for i, option in list(self.player_pokemon.items()):
            box_topleft_pos = self.main_rect.bottomright + vector(option_box_width/2 + bar_buffer, -option_box_height*5/2 + (option_box_height+option_gap)*i)

            # outline box  
            padding = 8
            option_outline_box_rect = pygame.FRect(box_topleft_pos - vector(padding/2, padding/2), (option_box_width + padding, option_box_height + padding))
            pygame.draw.rect(self.display_surface, COLOURS['grey'], option_outline_box_rect, 8, 8, 8, 8, 8)

            # box
            option_box_rect = pygame.FRect(box_topleft_pos, (option_box_width, option_box_height))
            pygame.draw.rect(self.display_surface, COLOURS['dark-grey'], option_box_rect, 0, 8, 8, 8, 8)

            # name
            option_name_surf = self.fonts['regular'].render(f'{option.name.upper()}', False, COLOURS['white'])
            option_name_rect = option_name_surf.get_frect(center = option_box_rect.center)
            self.display_surface.blit(option_name_surf, option_name_rect)

            if i == self.indexes['bag_pokemon_option']:
                option_box_rect = pygame.FRect(box_topleft_pos - vector(padding/2, padding/2), (option_box_width + padding, option_box_height + padding))
                pygame.draw.rect(self.display_surface, COLOURS['white'], option_box_rect, 8, 8, 8, 8, 8)

    def draw_party(self):
        self.column_n = 3
        self.row_n = 2
        
        self.order = [[],[]]
        self.party_open = True

        self.pokemon = player_data.POKEMON

        for i in range(self.row_n):
            for j in range(self.column_n):
                self.order[i].append(player_data.POKEMON[i*3 + j] if player_data.POKEMON[i*3 + j] else None)

        self.main_rect = pygame.FRect(0, 0, WINDOW_WIDTH*0.6, WINDOW_HEIGHT*0.45).move_to(center = (WINDOW_WIDTH/2, WINDOW_HEIGHT/2))

        #pokedex title
        title_text_surf = self.fonts['bold'].render("POKEMON", True, COLOURS['white'], COLOURS['dark-grey'])
        title_text_rect = title_text_surf.get_frect(bottomleft = self.main_rect.topleft + vector(15, -5))
        border_add = 6
        title_box_rect = pygame.FRect(title_text_rect.topleft + vector(-border_add * 1.75, -border_add * 1.75), (title_text_rect.width + border_add * 3.5, (title_text_rect.height + border_add * 4.5)))
        pygame.draw.rect(self.display_surface, COLOURS['amber'], title_box_rect, 6, 6, 6, 6, 6)
        self.display_surface.blit(title_text_surf, title_text_rect)

        # background
        pygame.draw.rect(self.display_surface, COLOURS['dark-grey'], self.main_rect, 0, 12, 12, 12, 12)

        # boxes (3x2 layout)
        top_gap = 30
        between_gap = 10
        box_width = self.main_rect.width*0.3
        box_height = self.main_rect.height/2 - top_gap - between_gap
        for i in range(self.row_n):
            for j in range(self.column_n):        
                pokemon_box_rect = pygame.FRect(
                    (
                        self.main_rect.midtop + \
                        vector(- between_gap - box_width*3/2, top_gap) + \
                        vector((box_width + between_gap)*j,(box_height + between_gap)*i)
                    ),
                    (box_width, box_height)
                )
                pygame.draw.rect(self.display_surface, COLOURS['grey'], pokemon_box_rect, 0, 8, 8, 8, 8)

        # selecting lighter shaded box (index)
        select_box_rect = pygame.FRect(
            (
                self.main_rect.midtop + \
                vector(- between_gap - box_width*3/2, top_gap) + \
                vector((box_width + between_gap)*self.indexes['party'][0],(box_height + between_gap)*self.indexes['party'][1])
            ),
            (box_width, box_height)
        )
        pygame.draw.rect(self.display_surface, COLOURS['light'], select_box_rect, 0, 8, 8, 8, 8)

        # pokemon data
        for i in range(self.row_n):
            for j in range(self.column_n):
                pos = self.main_rect.midtop + \
                    vector(- between_gap - box_width*3/2, top_gap) + \
                    vector((box_width + between_gap)*j,(box_height + between_gap)*i)
                if self.order[i][j] is None:
                    # empty box
                    empty_text_surf = self.fonts['regular'].render("[EMPTY]", False, COLOURS['white'])
                    empty_text_rect = pygame.FRect((pos + vector(box_width/2-empty_text_surf.get_width()/2,box_height/2-empty_text_surf.get_height()/2)), (empty_text_surf.get_width(), empty_text_surf.get_height()))
                    self.display_surface.blit(empty_text_surf, empty_text_rect)
                else:
                    pokemon = self.pokemon[3*i + j]
                    
                    # pokemon box sprite
                    icon_surf = self.pokemon_graphics['box_sprites'][pokemon.name]
                    icon_surf = pygame.transform.scale(icon_surf, (icon_surf.get_width()*2, icon_surf.get_height()*2))
                    icon_rect = icon_surf.get_frect(topright = pos + vector(box_width + 25, -5))
                    self.display_surface.blit(icon_surf, icon_rect)

                    # pokemon name
                    name_surf = self.fonts['large'].render(pokemon.name.capitalize(), False, COLOURS['white'])
                    name_rect = name_surf.get_frect(topleft = pos + vector(12, 10))
                    self.display_surface.blit(name_surf, name_rect)

                    # pokemon level
                    level_surf = self.fonts['regular'].render(f'Lv.{pokemon.level}', False, COLOURS['white'])
                    level_rect = level_surf.get_frect(bottomleft = (icon_rect.right - level_surf.get_width(), name_rect.bottom) + vector(-32, -1))
                    self.display_surface.blit(level_surf, level_rect)

                    # health bar
                    health_bar_height = 15
                    health_bar_width = 130
                    health_bar_rect = pygame.FRect(((name_rect.left, icon_rect.bottom) + vector(0, - health_bar_height - 10)),(health_bar_width, health_bar_height))
                    health_bar_colour = None
                    ratio = pokemon.current_hp/pokemon.max_hp
                    if ratio < 0.2:
                        health_bar_colour = COLOURS['red']
                    elif ratio >= 0.2 and ratio < 0.5:
                        health_bar_colour = COLOURS['amber']
                    else:
                        health_bar_colour = COLOURS['green']
                    draw_bar(self.display_surface, health_bar_rect, pokemon.current_hp, pokemon.max_hp, health_bar_colour, COLOURS['light'])

                    # health text
                    health_text_surf = self.fonts['bold'].render(f'{pokemon.current_hp}/{pokemon.max_hp}', False, COLOURS['white'])
                    health_text_rect = health_text_surf.get_frect(bottomleft = health_bar_rect.topleft + vector(0, -5))
                    self.display_surface.blit(health_text_surf, health_text_rect)                    

                    # xp bar
                    xp_bar_height = 10
                    xp_bar_rect = pygame.FRect((health_bar_rect.bottomleft),(health_bar_width, xp_bar_height))
                    xp_bar_colour = COLOURS['blue']
                    draw_bar(self.display_surface, xp_bar_rect, pokemon.current_xp, pokemon.level_xp, xp_bar_colour, COLOURS['light-grey'])

                    # pokemon held item if held item
                    # any status effect

    def draw_party_option_select(self):
        options = ['switch', 'summary', 'check moves']
        option_gap = 8
        bar_buffer = 12
        option_box_height = 40
        option_box_width = 150

        for i, option in enumerate(options):
            box_topleft_pos = self.main_rect.bottomright + vector(-option_box_width/2, -option_box_height*5/2 + (option_box_height+option_gap)*i)

            # outline box  
            padding = 8
            option_outline_box_rect = pygame.FRect(box_topleft_pos - vector(padding/2, padding/2), (option_box_width + padding, option_box_height + padding))
            pygame.draw.rect(self.display_surface, COLOURS['grey'], option_outline_box_rect, 8, 8, 8, 8, 8)

            # box
            option_box_rect = pygame.FRect(box_topleft_pos, (option_box_width, option_box_height))
            pygame.draw.rect(self.display_surface, COLOURS['dark-grey'], option_box_rect, 0, 8, 8, 8, 8)

            # name
            option_name_surf = self.fonts['regular'].render(f'{option.upper()}', False, COLOURS['white'])
            option_name_rect = option_name_surf.get_frect(center = option_box_rect.center)
            self.display_surface.blit(option_name_surf, option_name_rect)

            if i == self.indexes['pokemon_option']:
                option_box_rect = pygame.FRect(box_topleft_pos - vector(padding/2, padding/2), (option_box_width + padding, option_box_height + padding))
                pygame.draw.rect(self.display_surface, COLOURS['white'], option_box_rect, 8, 8, 8, 8, 8)

    def draw_pokemon_stats(self):
        pokemon = self.player_pokemon[3*self.selected_party_index[1] + self.selected_party_index[0]]
        
        main_rect = pygame.FRect(0, 0, WINDOW_WIDTH*0.6, WINDOW_HEIGHT*0.6).move_to(center = (WINDOW_WIDTH/2, WINDOW_HEIGHT/2))

        divide_y = 527

        rect = pygame.FRect(
            main_rect.left, main_rect.top, main_rect.width, main_rect.height
        )
        pygame.draw.rect(self.display_surface, COLOURS['dark-grey'], rect, 0, 12, 12, 12, 12)

        profile_rect = pygame.FRect(rect.topright + vector(-rect.height * 0.4, 0), (rect.height * 0.4, rect.height * 0.4))
        pygame.draw.rect(self.display_surface, COLOURS[pokemon.type[0]], profile_rect, 0, 0, 0, 12, 12)

        scale_factor = 2
        pokemon_surf = self.pokemon_graphics['battle_sprites'][f"{pokemon.name}_normal"]
        pokemon_surf = pygame.transform.scale(pokemon_surf, (pokemon_surf.get_width()*scale_factor, pokemon_surf.get_height()*scale_factor))
        pokemon_rect = pokemon_surf.get_frect(midbottom = profile_rect.midbottom + vector(0,-10))
        self.display_surface.blit(pokemon_surf, pokemon_rect)
        
        # name
        name_surf = self.fonts['bold'].render(pokemon.name.capitalize(), False, COLOURS['white'])
        name_rect = name_surf.get_frect(topleft = rect.topleft + vector(25, 25))
        self.display_surface.blit(name_surf, name_rect)

        # gender
        gender_surf = self.gender_icons[pokemon.gender if pokemon.gender is not None else 'genderless']
        gender_surf = pygame.transform.scale(gender_surf, (name_rect.height,name_rect.height))
        gender_rect = gender_surf.get_frect(bottomleft = name_rect.bottomright + vector(5, 0))
        self.display_surface.blit(gender_surf, gender_rect)

        # ID
        id_surf = self.fonts['small'].render(f"No. {pokemon.data['id']}", False, COLOURS['white'])
        id_rect = id_surf.get_frect(bottomleft = gender_rect.bottomright + vector(5, 0))
        self.display_surface.blit(id_surf, id_rect)

        # types
        last_type_length = 0
        text_box_height = 20
        border_add = 6
        bar_buffer = 12
        bar_width_mod = 70
        for _type in pokemon.type:
            type_surf = self.fonts['bold'].render(f"{_type}", False, COLOURS['white'])
            type_surf = pygame.transform.scale(type_surf, (type_surf.get_width()*0.85, type_surf.get_height()*0.85))
            type_rect = type_surf.get_frect(topleft = name_rect.bottomleft + vector((last_type_length + border_add * 3) * (int(pokemon.type.index(_type))), 20))
            type_box_rect = pygame.FRect(type_rect.topleft - vector(border_add, border_add), (type_rect.width + border_add * 2, (text_box_height + border_add * 2)))
            pygame.draw.rect(self.display_surface, COLOURS[_type.lower()], type_box_rect, 0, 6, 6, 6, 6)
            last_type_length = type_surf.get_width()
            self.display_surface.blit(type_surf, type_rect)

        # genus
        genus_surf = self.fonts['regular'].render(pokemon.data['genus'], False, COLOURS['white'])
        genus_rect = genus_surf.get_frect(topleft = vector(name_rect.left, type_rect.bottom + 20))
        self.display_surface.blit(genus_surf, genus_rect)

        # base stats
        for index, stat in enumerate(['HP', 'Atk', 'Def', 'SpAtk', 'SpDef', 'Speed']):
            text_surf = self.fonts['regular'].render(f"{stat}:", False, COLOURS['white'])
            text_rect = text_surf.get_frect(topleft = (divide_y + bar_buffer, profile_rect.bottom + (text_surf.get_height() + bar_buffer) * index + 33))
            self.display_surface.blit(text_surf, text_rect)

            bar_rect = pygame.FRect(vector(divide_y + bar_buffer + bar_width_mod, text_rect.top), (rect.width - bar_width_mod - bar_buffer * 3 - 40 - (divide_y - rect.left), text_rect.height))
            base_stat = int(pokemon.base_stats[stat])
            bar_colour = None
            if base_stat <= 85:
                bar_colour = COLOURS['red']
            elif base_stat > 85 and base_stat <= 170:
                bar_colour = COLOURS['amber']
            else:
                bar_colour = COLOURS['green']
            draw_bar(self.display_surface, bar_rect, base_stat, 255, bar_colour, COLOURS['light'])
            
            value_text_surf = self.fonts['regular'].render(f"{base_stat}", False, COLOURS['white'])
            value_text_rect = value_text_surf.get_frect(topleft = bar_rect.topright + vector(bar_buffer, 0))
            self.display_surface.blit(value_text_surf, value_text_rect)

        health_bar_height = 15
        xp_bar_height = 10

        # health bar
        health_bar_rect = pygame.FRect((divide_y + bar_buffer, profile_rect.bottom - health_bar_height - xp_bar_height),(profile_rect.left - (divide_y + bar_buffer) - bar_buffer*2, health_bar_height))
        health_bar_colour = None
        ratio = pokemon.current_hp/pokemon.max_hp
        if ratio < 0.2:
            health_bar_colour = COLOURS['red']
        elif ratio >= 0.2 and ratio < 0.5:
            health_bar_colour = COLOURS['amber']
        else:
            health_bar_colour = COLOURS['green']
        draw_bar(self.display_surface, health_bar_rect, pokemon.current_hp, pokemon.max_hp, health_bar_colour, COLOURS['light'])

        # health text
        health_text_surf = self.fonts['regular'].render(f'{pokemon.current_hp}/{pokemon.max_hp}', False, COLOURS['white'])
        health_text_rect = health_text_surf.get_frect(bottomright = health_bar_rect.topright + vector(0, -5))
        self.display_surface.blit(health_text_surf, health_text_rect)                    

        # xp bar
        xp_bar_rect = pygame.FRect((health_bar_rect.bottomleft),(health_bar_rect.width, xp_bar_height))
        xp_bar_colour = COLOURS['blue']
        draw_bar(self.display_surface, xp_bar_rect, pokemon.current_xp, pokemon.level_xp, xp_bar_colour, COLOURS['light-grey'])

        # level
        level_surf = self.fonts['bold'].render(f'Lv.{pokemon.level}', False, COLOURS['white'])
        level_rect = level_surf.get_frect(bottomleft = health_bar_rect.topleft + vector(0,-10))
        self.display_surface.blit(level_surf, level_rect)

        # ability
        ability_surf = self.fonts['regular'].render(f'Ability: {pokemon.ability.replace('-', ' ').title()}', False, COLOURS['white'])
        ability_rect = ability_surf.get_frect(topright = (health_bar_rect.right, name_rect.top))
        self.display_surface.blit(ability_surf, ability_rect)

        # nature
        nature_right_bracket_surf = self.fonts['regular'].render(')', False, COLOURS['white'])
        nature_right_bracket_rect = nature_right_bracket_surf.get_frect(topright = (ability_rect.bottomright))
        self.display_surface.blit(nature_right_bracket_surf, nature_right_bracket_rect)
        
        if NATURE_DATA[pokemon.nature]['decreased'] and NATURE_DATA[pokemon.nature]['increased']:
            nature_right_bonus_surf = self.fonts['regular'].render(f'-{NATURE_DATA[pokemon.nature]['decreased']}', False, COLOURS['red'])
            nature_right_bonus_rect = nature_right_bonus_surf.get_frect(bottomright = nature_right_bracket_rect.bottomleft)
            self.display_surface.blit(nature_right_bonus_surf, nature_right_bonus_rect)

            nature_slash_surf = self.fonts['regular'].render('/', False, COLOURS['white'])
            nature_slash_rect = nature_slash_surf.get_frect(bottomright = nature_right_bonus_rect.bottomleft)
            self.display_surface.blit(nature_slash_surf, nature_slash_rect)

            nature_left_bonus_surf = self.fonts['regular'].render(f'+{NATURE_DATA[pokemon.nature]['increased']}', False, COLOURS['blue'])
            nature_left_bonus_rect = nature_left_bonus_surf.get_frect(bottomright = nature_slash_rect.bottomleft)
            self.display_surface.blit(nature_left_bonus_surf, nature_left_bonus_rect)

            nature_surf = self.fonts['regular'].render(f'Nature: {pokemon.nature.capitalize()} (', False, COLOURS['white'])
            nature_rect = nature_surf.get_frect(bottomright = nature_left_bonus_rect.bottomleft)
            self.display_surface.blit(nature_surf, nature_rect)
        else:
            nature_surf = self.fonts['regular'].render(f'Nature: {pokemon.nature.capitalize()} (no effect', False, COLOURS['white'])
            nature_rect = nature_surf.get_frect(bottomright = nature_right_bracket_rect.bottomleft)
            self.display_surface.blit(nature_surf, nature_rect)

        # moves
        move_gap = 5
        move_box_height = (main_rect.bottom - genus_rect.bottom - bar_buffer*2) / 4 - move_gap
        move_box_width = health_bar_rect.left - genus_rect.left - bar_buffer
        for i in range(4):
            move = pokemon.moves[i]
            box_topleft_pos = (genus_rect.left, genus_rect.bottom + bar_buffer + (move_box_height+move_gap)*i)
            move_box_rect = pygame.FRect(box_topleft_pos, (move_box_width, move_box_height))

            if i == self.indexes['pokemon_stats_move']:
                box_wrap = 6
                pygame.draw.rect(self.display_surface, COLOURS['white'], pygame.FRect(box_topleft_pos + vector(-box_wrap/2, -box_wrap/2), (move_box_width + box_wrap, move_box_height + box_wrap)), 0, 8, 8, 8, 8)

            if move:
                move_data = MOVE_DATA[move['name']]

                # box
                pygame.draw.rect(self.display_surface, COLOURS[move_data['type']], move_box_rect, 0, 8, 8, 8, 8)

                # name
                move_name_surf = self.fonts['regular'].render(f'{move['name'].replace('-', ' ').title()}', False, COLOURS['white'])
                move_name_rect = move_name_surf.get_frect(topleft = box_topleft_pos + vector(10,10))
                self.display_surface.blit(move_name_surf, move_name_rect)

                # move_icon
                icon_surf = self.move_type_icon[move_data['damage_class']]
                icon_surf = pygame.transform.scale(icon_surf, (icon_surf.get_width()*0.6, icon_surf.get_height()*0.6))
                icon_width = icon_surf.get_width()
                icon_height = icon_surf.get_height()
                icon_rect = icon_surf.get_frect(topleft = box_topleft_pos + vector(move_box_width - icon_width - 10, 10))
                self.display_surface.blit(icon_surf, icon_rect)
                
                # pp
                pp_surf = self.fonts['small'].render(f'PP:{move['current_pp']}/{move_data['max_pp']}', False, COLOURS['white'])
                pp_rect = pp_surf.get_frect(topleft = box_topleft_pos + vector(10, move_box_height - pp_surf.get_height() - 10))
                self.display_surface.blit(pp_surf, pp_rect)

                # power
                power_surf = self.fonts['small'].render(f'Power: {move_data['power']}' if move_data['power'] else 'Power: --', False, COLOURS['white'])
                power_rect = power_surf.get_frect(bottomleft = pp_rect.bottomright + vector(10,0))
                self.display_surface.blit(power_surf, power_rect)

                # accuracy
                acc_surf = self.fonts['small'].render(f'Acc: {move_data['accuracy']}' if move_data['accuracy'] else 'Acc: --', False, COLOURS['white'])
                acc_rect = acc_surf.get_frect(bottomleft = power_rect.bottomright + vector(10,0))
                self.display_surface.blit(acc_surf, acc_rect)
                
                # selected box
                if i == self.indexes['pokemon_stats_move']:
                    text = '\n'.join(textwrap.wrap(f"{move_data['flavor_text_entry']} {move_data['effect_entries']}", width=76))
                    item_text_surf = self.fonts['regular'].render(text, False, COLOURS['white'])

                    text_bg_rect = pygame.FRect(vector(main_rect.bottomleft + vector(0, bar_buffer)), (main_rect.width, item_text_surf.get_height() + bar_buffer*2))
                    pygame.draw.rect(self.display_surface, COLOURS['grey'], text_bg_rect, 0, 12, 12, 12, 12)

                    item_text_rect = item_text_surf.get_frect(topleft = text_bg_rect.topleft + vector(bar_buffer, bar_buffer))
                    self.display_surface.blit(item_text_surf, item_text_rect)

            else:
                # box
                move_box_rect = pygame.FRect(box_topleft_pos, (move_box_width, move_box_height))
                pygame.draw.rect(self.display_surface, COLOURS['grey'], move_box_rect, 0, 8, 8, 8, 8)

                # name
                move_name_surf = self.fonts['bold'].render('--', False, COLOURS['white'])
                move_name_rect = move_name_surf.get_frect(center = move_box_rect.center)
                self.display_surface.blit(move_name_surf, move_name_rect)

# real-time methods

    def input(self):
        if self.selection_mode and not self.dialog_tree:
            keys = pygame.key.get_just_pressed()

            if self.selection_mode == 'fight':  
                if keys[pygame.K_UP]:
                    self.indexes[self.selection_mode] = (self.indexes['fight'] - 1) % 4
                if keys[pygame.K_DOWN]:
                    self.indexes[self.selection_mode] = (self.indexes['fight'] + 1) % 4
                if keys[pygame.K_SPACE]:
                    if self.current_player_pokemon.moves[self.indexes[self.selection_mode]] is not None:
                        if self.current_player_pokemon.moves[self.indexes[self.selection_mode]]['current_pp'] == 0:
                            self.dialog_tree = DialogTree(self.all_sprites, self.fonts['dialog'], self.display_surface, self.end_dialog, narration=[f"No PP left on that move!"])
                        else:
                            self.player_chosen_action = {'option': 'fight', 'move': str(self.current_player_pokemon.moves[self.indexes[self.selection_mode]]['name'])}
                            self.opponent_chosen_action = self.decide_opponent_action()
                            self.selection_mode == None
                            self.evaluate_chosen_action()
                            self.indexes['workflow'] += 1
                if keys[pygame.K_z]:
                    self.selection_mode = 'menu'

            elif self.selection_mode == 'bag':
                if self.bag_option_select:
                    if self.bag_option_pokemon_select:
                        if keys[pygame.K_UP]:
                            self.indexes['bag_pokemon_option'] -= 1
                        if keys[pygame.K_DOWN]:
                            self.indexes['bag_pokemon_option'] += 1
                        self.indexes['bag_pokemon_option'] = self.indexes['bag_pokemon_option'] % len(self.player_pokemon)
                        if keys[pygame.K_SPACE]:
                            self.player_chosen_action = {'option': 'use', 'item': player_data.BAG[list(player_data.BAG.keys())[self.indexes['bag_category']]][self.indexes['bag']]['name'], 'affected_pokemon': self.player_pokemon[self.indexes['bag_pokemon_option']] if list(player_data.BAG.keys())[self.indexes['bag_category']] != 'balls' else None}
                            self.bag_option_select - False
                            self.bag_option_pokemon_select = False
                            self.opponent_chosen_action = self.decide_opponent_action()
                            self.selection_mode = None
                            self.action_chosen = True
                            self.evaluate_chosen_action()
                            self.indexes['workflow'] += 1
                        if keys[pygame.K_z]:
                            self.selection_mode = 'bag'
                            self.bag_option_pokemon_select = False
                    else:
                        if keys[pygame.K_UP]:
                            self.indexes['bag_option'] -= 1
                        if keys[pygame.K_DOWN]:
                            self.indexes['bag_option'] += 1
                        self.indexes['bag_option'] = self.indexes['bag_option'] % 3
                        if keys[pygame.K_SPACE]:
                            if self.indexes['bag_option'] == 0: # use
                                if list(player_data.BAG.keys())[self.indexes['bag_category']] == 'balls':
                                    self.player_chosen_action = {'option': 'use', 'item': player_data.BAG[list(player_data.BAG.keys())[self.indexes['bag_category']]][self.indexes['bag']]['name'], 'affected_pokemon': None}
                                    self.bag_option_select - False
                                    self.bag_option_pokemon_select = False
                                    self.selection_mode = None
                                    self.action_chosen = True
                                else:
                                    item_name = player_data.BAG[list(player_data.BAG.keys())[self.indexes['bag_category']]][self.indexes['bag']]['name']
                                    if 'usable-in-battle' not in ITEM_DATA[item_name]['attributes']:
                                        if not self.dialog_input_overlap:
                                            self.dialog_tree = DialogTree(self.all_sprites, self.fonts['dialog'], self.display_surface, self.end_dialog, narration=[f"{item_name.replace('-', ' ').title()} cannot be used during a battle!"])
                                        if self.dialog_input_overlap:
                                            self.dialog_input_overlap = False 
                                    else:
                                        self.bag_option_pokemon_select = True
                            if self.indexes['bag_option'] == 1: # give
                                if not self.dialog_input_overlap:
                                    self.dialog_tree = DialogTree(self.all_sprites, self.fonts['dialog'], self.display_surface, self.end_dialog, narration=[f"You cannot give items during a battle!"])
                                if self.dialog_input_overlap:
                                    self.dialog_input_overlap = False 
                            if self.indexes['bag_option'] == 2: # trash
                                if not self.dialog_input_overlap:
                                    self.dialog_tree = DialogTree(self.all_sprites, self.fonts['dialog'], self.display_surface, self.end_dialog, narration=[f"You cannot trash items during a battle!"])
                                if self.dialog_input_overlap:
                                    self.dialog_input_overlap = False 
                        if keys[pygame.K_z]:
                            self.selection_mode = 'bag'
                            self.bag_open = False
                            self.bag_option_select = False
                else:
                    if keys[pygame.K_UP]:
                        self.indexes['bag'] -= 1
                    if keys[pygame.K_DOWN]:
                        self.indexes['bag'] += 1
                    if keys[pygame.K_RIGHT]:
                        self.indexes['bag_category'] -= 1
                        self.indexes['bag'] = 0
                    if keys[pygame.K_LEFT]:
                        self.indexes['bag_category'] += 1
                        self.indexes['bag'] = 0
                    self.indexes['bag_category'] = self.indexes['bag_category'] % len(list(player_data.BAG.keys()))
                    self.indexes['bag'] = self.indexes['bag'] % len(player_data.BAG[list(player_data.BAG.keys())[self.indexes['bag_category']]])
                    if keys[pygame.K_SPACE]:
                        if self.bag_open:
                            self.selected_bag_index = (self.indexes['bag_category'], self.indexes['bag'])
                            self.bag_option_select = True
                    if keys[pygame.K_z]:
                        self.selection_mode = 'menu'

            elif self.selection_mode == 'party':
                if self.party_option_select:
                    if keys[pygame.K_UP]:
                        self.indexes['pokemon_option'] -= 1
                    if keys[pygame.K_DOWN]:
                        self.indexes['pokemon_option'] += 1
                    self.indexes['pokemon_option'] = self.indexes['pokemon_option'] % 3
                    if keys[pygame.K_SPACE]:
                        if self.indexes['pokemon_option'] == 0:
                            if self.current_player_pokemon == self.order[self.indexes['party'][1]][self.indexes['party'][0]]:
                                if not self.dialog_input_overlap:
                                    self.dialog_tree = DialogTree(self.all_sprites, self.fonts['dialog'], self.display_surface, self.end_dialog, narration=[f"{self.current_player_pokemon.name.capitalize()} is already in battle!"])
                                if self.dialog_input_overlap:
                                    self.dialog_input_overlap = False
                            elif self.order[self.indexes['party'][1]][self.indexes['party'][0]].current_hp <= 0:
                                if not self.dialog_input_overlap:
                                    self.dialog_tree = DialogTree(self.all_sprites, self.fonts['dialog'], self.display_surface, self.end_dialog, narration=[f"{self.order[self.indexes['party'][1]][self.indexes['party'][0]].name.capitalize()} is not able to fight!"])
                                if self.dialog_input_overlap:
                                    self.dialog_input_overlap = False
                            else:
                                if self.switch_party_selection_mode:
                                    self.switch_pokemon('player', self.order[self.indexes['party'][1]][self.indexes['party'][0]])
                                    self.switch_party_selection_mode = False
                                    self.selection_mode = 'menu'
                                    self.indexes['workflow'] = 0
                                    self.indexes['move_order'] = 0
                                else:
                                    self.player_chosen_action = {'option': 'switch', 'affected_pokemon': self.order[self.indexes['party'][1]][self.indexes['party'][0]]}
                                    self.opponent_chosen_action = self.decide_opponent_action()
                                    self.selection_mode = None
                                    self.action_chosen = True
                                    self.evaluate_chosen_action()
                                    self.indexes['workflow'] += 1
                        if self.indexes['pokemon_option'] == 1:
                            self.selection_mode = 'pokemon_stats'
                            self.party_open = False
                            self.party_option_select = False
                        if self.indexes['pokemon_option'] == 2:
                            self.selection_mode = 'moves_menu'
                            self.party_open = False
                            self.party_option_select = False
                    if keys[pygame.K_z]:
                        self.selection_mode = 'party'
                        self.party_open = False
                        self.party_option_select = False
                else:
                    if keys[pygame.K_UP]:
                        self.indexes['party'] = (self.indexes['party'][0], self.indexes['party'][1] - 1)
                    if keys[pygame.K_DOWN]:
                        self.indexes['party'] = (self.indexes['party'][0], self.indexes['party'][1] + 1)
                    if keys[pygame.K_LEFT]:
                        self.indexes['party'] = (self.indexes['party'][0] - 1, self.indexes['party'][1])
                    if keys[pygame.K_RIGHT]:
                        self.indexes['party'] = (self.indexes['party'][0] + 1, self.indexes['party'][1])
                    self.indexes['party'] = (self.indexes['party'][0] % 3, self.indexes['party'][1] % 2)
                    if keys[pygame.K_SPACE]:
                        if self.party_open:
                            if self.order[self.indexes['party'][1]][self.indexes['party'][0]] is not None:
                                self.selected_party_index = self.indexes['party']
                                self.party_option_select = True
                    if keys[pygame.K_z]:
                        if not self.switch_party_selection_mode:
                            self.selection_mode = 'menu'

            elif self.selection_mode == 'pokemon_stats':
                if keys[pygame.K_UP]:
                    self.indexes['pokemon_stats_move'] -= 1
                if keys[pygame.K_DOWN]:
                    self.indexes['pokemon_stats_move'] += 1
                self.indexes['pokemon_stats_move'] = self.indexes['pokemon_stats_move'] % 4
                if keys[pygame.K_z]:
                        self.selection_mode = 'party'
                        self.party_open = True
                        self.party_option_select = False

            elif self.selection_mode == 'menu':
                match self.selection_mode:
                    case 'menu': limiter = len(BATTLE_CHOICES)
                if keys[pygame.K_LEFT]:
                    self.indexes[self.selection_mode] = (self.indexes['menu'] - 1) % limiter
                if keys[pygame.K_RIGHT]:
                    self.indexes[self.selection_mode] = (self.indexes['menu'] + 1) % limiter
                if keys[pygame.K_SPACE]:
                    if self.selection_mode == 'menu':
                        if self.indexes['menu'] == 0:
                            if not all([move['current_pp'] for move in self.current_player_pokemon.moves.values() if move is not None ]):
                                self.player_chosen_action = {'option': 'fight', 'move': 'struggle'}
                                self.opponent_chosen_action = self.decide_opponent_action()
                                self.selection_mode == None
                                self.evaluate_chosen_action()
                                self.indexes['workflow'] += 1
                            else:
                                self.selection_mode = 'fight'
                        if self.indexes['menu'] == 1:
                            self.selection_mode = 'bag'
                            self.bag_open = False
                            self.bag_option_select = False
                        if self.indexes['menu'] == 2:
                            self.selection_mode = 'party'
                            self.party_open = False
                            self.party_option_select = False
                        if self.indexes['menu'] == 3:
                            if self.is_trainer:
                                if not self.dialog_input_overlap:
                                    self.dialog_tree = DialogTree(self.all_sprites, self.fonts['dialog'], self.display_surface, self.end_dialog, narration=BATTLE_TEXT['trainer run'])
                                if self.dialog_input_overlap:
                                    self.dialog_input_overlap = False
                            else:
                                self.player_chosen_action = {'option': 'run'}
                                self.dialog_tree = DialogTree(self.all_sprites, self.fonts['dialog'], self.display_surface, self.end_dialog, narration=BATTLE_TEXT['attempt run'])
                                self.selection_mode = None
                                self.action_chosen = True

    def update(self, dt):
        self.display_surface.blit(self.bg_surf, (0, self.bg_surf_pos))

        self.battle_sprites.update(dt)
        self.battle_sprites.draw(self.display_surface)

        if any(timer.active for timer in self.timers.values()):
            for timer in self.timers.values():
                if timer.active:
                    timer.update()
        else:

            if self.battle_state == 'fainting' and self.waiting_for_input:
                # Wait for player input to clear fainting message and continue the battle
                if self.player_pressed_continue():
                    self.waiting_for_input = False
                    self.battle_state = 'experience'

            elif self.battle_state == 'experience':
                self.calculate_experience()
                self.battle_state = 'post_experience'

            elif self.battle_state == 'post_experience':
                # Check if the battle should end
                if not self.finish_token:
                    # Switch or select next Pokémon
                    if self.entity == 'opponent':
                        self.current_opponent_pokemon = self.select_next_opponent_pokemon(self.current_player_pokemon, list(self.opponent_pokemon.values()))
                    elif self.entity == 'player':
                        self.selection_mode = 'party'
                        self.switch_party_selection_mode = True

            if self.workflow[self.indexes['workflow']] == 'select':
                if self.selection_mode == 'bag' or \
                    self.selection_mode == 'party' or \
                        self.selection_mode == 'pokemon' or \
                            self.selection_mode == 'pokemon_stats':
                    self.display_surface.blit(self.tint_surf, (0,0))

                if self.selection_mode == 'menu':
                    self.draw_menu()
                if self.selection_mode == 'bag':
                    self.draw_bag()
                    if self.bag_option_select:
                        self.draw_bag_option_select()
                        if self.bag_option_pokemon_select:
                            self.draw_bag_option_pokemon_select()
                if self.selection_mode == 'fight':
                    self.draw_fight()
                if self.selection_mode == 'party':
                    self.draw_party()
                    if self.party_option_select:
                        self.draw_party_option_select()
                if self.selection_mode == 'pokemon_stats':
                    self.draw_pokemon_stats()

            if self.workflow[self.indexes['workflow']] == 'start_effects':
                if not self.workflow_active:
                    self.timers[self.workflow[self.indexes['workflow']]].activate()
                    self.start_effects()
                    self.workflow_active = True
                if not self.timers[self.workflow[self.indexes['workflow']]].active and self.workflow_active:
                    self.workflow_active = False
                    self.indexes['workflow'] += 1

            if self.workflow[self.indexes['workflow']] == 'start_effects_text':
                if not self.workflow_active:
                    self.start_effects_text()
                    self.workflow_active = True
                if self.dialog_tree is None:
                    if len(self.start_effects_dialog_stack) > 0:
                        self.start_effects_text()
                    elif self.workflow_active:
                        self.workflow_active = False
                        self.indexes['workflow'] += 1

            if self.workflow[self.indexes['workflow']] == 'pre_move_text':
                if not self.workflow_active:
                    self.pre_move_text()
                    self.workflow_active = True

            if self.workflow[self.indexes['workflow']] == 'resolve_action':
                if not self.workflow_active:
                    self.timers[self.workflow[self.indexes['workflow']]].activate()
                    if self.player_chosen_action['option'] == 'switch' and self.move_order[self.indexes['move_order']] == 'player':
                        self.switch_pokemon('player', self.player_chosen_action['affected_pokemon'])
                    if self.opponent_chosen_action['option'] == 'switch' and self.move_order[self.indexes['move_order']] == 'opponent':
                        self.switch_pokemon('opponent', self.opponent_chosen_action['affected_pokemon'])
                    if self.player_chosen_action['option'] == 'fight':
                        self.resolve_move_damage()
                    self.workflow_active = True
                if not self.timers[self.workflow[self.indexes['workflow']]].active and self.workflow_active:
                    self.workflow_active = False
                    self.indexes['workflow'] += 1

            if self.workflow[self.indexes['workflow']] == 'apply_effects':
                if not self.workflow_active:
                    self.timers[self.workflow[self.indexes['workflow']]].activate()
                    self.apply_effects()
                    self.workflow_active = True
                if not self.timers[self.workflow[self.indexes['workflow']]].active and self.workflow_active:
                    self.workflow_active = False
                    self.indexes['workflow'] += 1

            if self.workflow[self.indexes['workflow']] == 'post_move_text':
                if not self.workflow_active:
                    self.post_move_text()
                    self.workflow_active = True
                if self.dialog_tree is None:
                    if len(self.post_move_text_dialog_stack) > 0:
                        self.post_move_text()
                    elif self.workflow_active:
                        self.workflow_active = False
                        self.indexes['workflow'] += 1

            if self.workflow[self.indexes['workflow']] == 'post_effect_text':
                if not self.workflow_active:
                    self.post_effect_text()
                    self.workflow_active = True
                if self.dialog_tree is None:
                    if len(self.post_effect_text_dialog_stack) > 0:
                        self.post_effect_text()
                    elif self.workflow_active:
                        self.workflow_active = False
                        self.indexes['workflow'] += 1

            if self.workflow[self.indexes['workflow']] == 'end_effects':
                if not self.workflow_active:
                    self.end_effects()
                    self.update_fainting_and_experience()
                    self.workflow_active = True
                elif not self.timers[self.workflow[self.indexes['workflow']]].active and self.workflow_active:
                    self.workflow_active = False
                    self.indexes['workflow'] += 1

            if self.workflow[self.indexes['workflow']] == 'end_effects_text':
                if not self.workflow_active:
                    self.end_effects_text()
                    self.workflow_active = True
                if self.dialog_tree is None:
                    if len(self.end_effects_dialog_stack) > 0:
                        self.end_effects_text()
                    else:
                        # Check if the battle is actually finished, and only set final_dialog here
                        if self.finish_token and not self.final_dialog:
                            self.final_dialog = True
                        elif self.final_dialog and self.dialog_tree is None:
                            self.battle_finished = True
                        else:
                            self.workflow_active = False
                            if self.indexes['workflow'] + 1 == len(self.workflow):
                                self.next_round_reset()
                            else:
                                self.indexes['workflow'] += 1
                            self.indexes['move_order'] += 1
                            self.indexes['move_order'] = self.indexes['move_order'] % 2

            if self.dialog_tree:
                self.dialog_tree.update()
            else:
                if self.workflow[self.indexes['workflow']] == 'select':
                    self.input()

            if self.final_dialog and self.dialog_tree is None:
                self.battle_finished = True
