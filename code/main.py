from settings import *
from game_data import *
from pytmx.util_pygame import load_pygame
from os.path import join

from sprites import Sprite, AnimatedSprite, PokemonPatchSprite, BorderSprite, CollidableSprite, TransitionSprite
from entities import Player, Character
from groups import AllSprites
from cutscenes import TitleIntro, DadIntro, ClassroomIntro
from dialog import DialogTree, DialogSprite
from support import *
from pokemon import Pokemon
from pokedex import Pokedex
from poke_party import PokeParty
from bag import Bag
from battle import Battle
from starter_select import StarterSelect
from pokemon_data import POKEMON_DATA
import player_data

class Game:
    def __init__(self):
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Pokémon Twilight")
        self.clock = pygame.time.Clock()

        self.player_pokemon = {
            0: Pokemon('breloom', 20),
            1: Pokemon('magnezone', 30),
            2: Pokemon('sawsbuck', 14)
        }

        for i in range(len(self.player_pokemon)):
            player_data.POKEMON[i] = self.player_pokemon[i]

        self.fade_screen = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.fade_screen.fill(COLOURS['black'])
        self.fade_screen.set_alpha(255)
        self.fade_alpha = 255
        self.fade_speed = 300
        self.fading = True
        self.fade_direction = 'in'
        self.fade_complete = False  # New flag to check if fade-out is complete
        self.player_gender = 'hilda'
        self.all_sprites = AllSprites()
        self.collision_sprites = pygame.sprite.Group()
        self.character_sprites = pygame.sprite.Group()
        self.transition_sprites = pygame.sprite.Group()
        self.transition_target = None

        self.import_assets()

        self.dialog_tree = None
        self.pokedex = Pokedex(self.fonts, self.pokemon_graphics, self.other_graphics['pokeball'])
        self.pokedex_open = False

        self.poke_party = PokeParty(self.fonts, self.pokemon_graphics, self.other_graphics)
        self.poke_party_open = False
        
        self.current_area = 'path'
        
        self.battle = Battle(self.player_pokemon, self.get_opponent_pokemon('edward 2'), self.current_area, self.fonts, self.all_sprites, self.pokemon_graphics, self.item_graphics, self.battle_bgs, self.other_graphics, is_trainer=False)
        self.battle_open = False

        self.bag = Bag(self.fonts, self.pokemon_graphics, self.item_graphics, self.other_graphics)
        self.bag_open = False

        self.starter_select = None

        self.cutscene_index = 2
        self.scene = None
        self.cutscene = self.load_cutscene_setup()

    def fade(self, dt):
        if self.fade_direction:
            if self.fade_direction == 'in':
                if self.fade_alpha > 0:
                    self.fade_alpha -= self.fade_speed * dt
                    if self.fade_alpha < 0:
                        self.fade_alpha = 0
                else:
                    self.fading = False
            elif self.fade_direction == 'out':
                if self.fade_alpha < 255:
                    self.fade_alpha += self.fade_speed * dt
                    if self.fade_alpha > 255:
                        self.fade_alpha = 255
                else:
                    self.fade_direction = 'in'
                    self.fade_complete = True  # Fade-out is complete
            self.fade_screen.set_alpha(self.fade_alpha)
            self.display_surface.blit(self.fade_screen, (0, 0))

    def battle_transition(self, dt):
        if self.fade_direction:
            if self.fade_direction == 'in':
                if self.fade_alpha > 0:
                    self.fade_alpha -= self.fade_speed * dt
                    if self.fade_alpha < 0:
                        self.fade_alpha = 0
                else:
                    self.fading = False
            elif self.fade_direction == 'out':
                if self.fade_alpha < 255:
                    self.fade_alpha += self.fade_speed * dt
                    if self.fade_alpha > 255:
                        self.fade_alpha = 255
                else:
                    self.fade_direction = 'in'
                    self.fade_complete = True  # Fade-out is complete
            self.fade_screen.set_alpha(self.fade_alpha)
            self.display_surface.blit(self.fade_screen, (0, 0))

    def start_fade(self):
        self.fading = True
        self.fade_direction = 'out'
        self.fade_complete = False  # Reset the fade_complete flag

    def load_cutscene_setup(self):
        self.scene = list(MAP_ORDER.values())[self.cutscene_index]
        self.load_game_setup()
        if CUTSCENE_ORDER[self.cutscene_index] == 'title_intro':
            return TitleIntro(self.all_sprites, self.display_surface, self.fonts['dialog'], self.end_cutscene)
        elif CUTSCENE_ORDER[self.cutscene_index] == 'dad_intro':
            return DadIntro(self.all_sprites, self.display_surface, self.fonts['dialog'], self.end_cutscene, self.end_dialog)
        elif CUTSCENE_ORDER[self.cutscene_index] == 'classroom':
            return ClassroomIntro(self.all_sprites, self.display_surface, self.fonts['dialog'], self.end_cutscene, self.end_dialog, self.overworld_frames['characters']['drayden'])

    def end_cutscene(self):
        self.cutscene_index += 1
        self.start_fade()
        # The scene change logic will be handled in the run method after fade-out is complete

    def load_game_setup(self):
        if self.scene["scene_type"] == 'cutscene':
            self.setup_cutscene(self.tmx_maps[self.scene["map_name"]])
        elif self.scene["scene_type"] == 'game':
            self.setup_game(self.tmx_maps[self.scene["map_name"]], self.scene['player_pos'])

    def change_scene(self):
        if self.transition_target:
            self.setup_game(self.tmx_maps[self.transition_target], self.transition_pos)
        else:
            if self.cutscene_index >= len(CUTSCENE_ORDER):
                self.scene = MAP_ORDER['classroom']
                self.load_game_setup()
            else:
                self.cutscene = self.load_cutscene_setup()

    def get_camera_pos(self):
        if 'camera' in self.scene.keys():
            if self.scene["camera"] == 'player':
                return self.player.rect.center
            elif self.scene["camera"] == 'locked':
                return self.scene["camera_pos"]
            elif self.scene["camera"] == 'track':
                return self.cutscene.car.rect.center
        else:
            return self.player.rect.center

    def import_assets(self):
        self.tmx_maps = {
            'forest_road': load_pygame(join('..', 'data', 'maps', 'forest_road.tmx')),
            'classroom_intro': load_pygame(join('..', 'data', 'maps', 'classroom_intro.tmx')),
            'classroom': load_pygame(join('..', 'data', 'maps', 'classroom.tmx')),
            'schoolyard': load_pygame(join('..', 'data', 'maps', 'schoolyard.tmx')),
        }

        self.overworld_frames = {
            'characters': all_character_import(join('..', 'graphics', 'characters', 'overworld'))
        }
        
        self.other_graphics = {
            'pokeball': import_image(join('..', 'graphics', 'other', 'pokeball')),
            'physical': import_image(join('..', 'graphics', 'other', 'physical')),
            'special': import_image(join('..', 'graphics', 'other', 'special')),
            'status': import_image(join('..', 'graphics', 'other', 'status')),
            'bag_icons': import_folder_dict(join('..', 'graphics', 'other', 'bag icons')),
            'bag_sprites': import_folder_dict(join('..', 'graphics', 'other', 'bag sprites')),
            'gender': import_folder_dict(join('..', 'graphics', 'other', 'gender icons')),
            'status_conditions': import_folder_dict(join('..', 'graphics', 'other', 'status icons'))
        }

        self.item_graphics = {
            'balls': import_folder_dict(join('..', 'graphics', 'items', 'balls')),
            'battle-items': import_folder_dict(join('..', 'graphics', 'items', 'battle-items')),
            'berries': import_folder_dict(join('..', 'graphics', 'items', 'berries')),
            'items': {
                **import_folder_dict(join('..', 'graphics', 'items', 'evo-items')),
                **import_folder_dict(join('..', 'graphics', 'items', 'held-items'))
            },
            'key-items': import_folder_dict(join('..', 'graphics', 'items', 'key-items')),
            'medicine': import_folder_dict(join('..', 'graphics', 'items', 'medicine')),
            'tms': import_folder_dict(join('..', 'graphics', 'items', 'tms')),
        }

        self.fonts = {
            'dialog': pygame.font.Font(join('..', 'graphics', 'fonts', 'PixeloidSans.ttf'), 30),
            'large': pygame.font.Font(join('..', 'graphics', 'fonts', 'PixeloidSans.ttf'), 24),
            'regular': pygame.font.Font(join('..', 'graphics', 'fonts', 'PixeloidSans.ttf'), 18),
            'bag': pygame.font.Font(join('..', 'graphics', 'fonts', 'PixeloidSans.ttf'), 16),
            'small': pygame.font.Font(join('..', 'graphics', 'fonts', 'PixeloidSans.ttf'), 14),
            'bold': pygame.font.Font(join('..', 'graphics', 'fonts', 'dogicapixelbold.otf'), 20)
        }

        self.portraits = {
            'characters': import_folder_dict(join('..', 'graphics', 'characters', 'portrait'))
        }

        self.pokemon_graphics = {
            'battle_sprites': import_folder_dict(join('..', 'graphics', 'pokemon', 'battle_sprites')),
            'box_sprites': import_folder_dict(join('..', 'graphics', 'pokemon', 'box_sprites'))
        }

        self.battle_bgs = import_folder_dict(join('..', 'graphics', 'battle_bgs'))

        self.battle_transitions = {
            'swirl': import_folder_dict(join('..', 'graphics', 'other', 'swirl transition')),
        }

    def setup_cutscene(self, tmx_map):
        self.all_sprites.empty()
        self.collision_sprites.empty()
        self.character_sprites.empty()

        layer_names = [layer.name for layer in tmx_map.layers]

        for x, y, surf in tmx_map.get_layer_by_name('Terrain').tiles():
            Sprite((x * TILE_SIZE, y * TILE_SIZE), surf, self.all_sprites, WORLD_LAYERS['bg'])

        if 'Terrain Top' in layer_names:
            for x, y, surf in tmx_map.get_layer_by_name('Terrain Top').tiles():
                Sprite((x * TILE_SIZE, y * TILE_SIZE), surf, self.all_sprites, WORLD_LAYERS['bg'])

        for obj in tmx_map.get_layer_by_name('Objects'):
            Sprite((obj.x, obj.y), obj.image, self.all_sprites)

        if 'Entities' in layer_names:
            for obj in tmx_map.get_layer_by_name('Entities'):
                if obj.name == 'Character':
                    Character(
                        pos = (obj.x, obj.y),
                        frames = self.overworld_frames['characters'][obj.properties['graphic']],
                        groups = (self.all_sprites, self.collision_sprites, self.character_sprites),
                        facing_direction = obj.properties['direction'],
                        character_data = None,
                        portrait = self.portraits['characters'][obj.properties['graphic']],
                        player = None,
                        create_dialog = None,
                        collision_sprites = None,
                        radius = None
                    )

    def setup_game(self, tmx_map, player_start_pos):        
        self.all_sprites.empty()
        self.collision_sprites.empty()
        self.character_sprites.empty()
        self.transition_sprites.empty()

        layer_names = [layer.name for layer in tmx_map.layers]

        for layer in ['Terrain', 'Terrain Top']:
            for x, y, surf in tmx_map.get_layer_by_name(layer).tiles():
                Sprite((x * TILE_SIZE, y * TILE_SIZE), surf, self.all_sprites, WORLD_LAYERS['bg'])

        for obj in tmx_map.get_layer_by_name('Objects'):
            CollidableSprite((obj.x, obj.y), obj.image, (self.all_sprites, self.collision_sprites))

        for obj in tmx_map.get_layer_by_name('Collisions'):
            BorderSprite((obj.x, obj.y), pygame.Surface((obj.width, obj.height)), self.collision_sprites)

        for obj in tmx_map.get_layer_by_name('Transitions'):
            TransitionSprite((obj.x, obj.y), (obj.width, obj.height), (obj.properties['target'], obj.properties['pos']), self.transition_sprites)

        if 'Grass Patches' in layer_names:
            for obj in tmx_map.get_layer_by_name('Grass Patches'):
                PokemonPatchSprite((obj.x, obj.y), obj.image, self.all_sprites)

        for obj in tmx_map.get_layer_by_name('Entities'):
            if obj.name == 'Player' and obj.properties['pos'] == player_start_pos:
                self.player = Player(
                    pos = (obj.x, obj.y),
                    frames = self.overworld_frames['characters'][self.player_gender],
                    groups = self.all_sprites,
                    facing_direction = obj.properties['direction'],
                    collision_sprites = self.collision_sprites
                )
                break

        for obj in tmx_map.get_layer_by_name('Entities'):
            if obj.name == 'Character':
                Character(
                    pos = (obj.x, obj.y),
                    frames = self.overworld_frames['characters'][obj.properties['graphic']],
                    groups = (self.all_sprites, self.collision_sprites, self.character_sprites),
                    facing_direction = obj.properties['direction'],
                    character_data = TRAINER_DATA[obj.properties['character_id']],
                    portrait = self.portraits['characters'][obj.properties['graphic']],
                    player = self.player,
                    create_dialog = self.create_dialog,
                    collision_sprites = self.collision_sprites,
                    radius = obj.properties['radius']
                )

    def input(self):
        if not self.dialog_tree and not self.battle_open:
            if self.scene["scene_type"] == 'game':
                keys = pygame.key.get_just_pressed()
                if keys[pygame.K_SPACE]:
                    for character in self.character_sprites:
                        if check_connection(48, self.player, character):
                            self.player.block()
                            character.change_facing_direction(self.player.rect.center)
                            self.create_dialog(character=character)
                if keys[pygame.K_q]:
                    if not self.poke_party_open or not self.bag_open:
                        self.pokedex_open = not self.pokedex_open
                        self.player.blocked = not self.player.blocked
                if keys[pygame.K_w]:
                    if not self.poke_party_open or not self.pokedex_open:
                        self.bag_open = not self.bag_open
                        self.player.blocked = not self.player.blocked
                if keys[pygame.K_e]:
                    if not self.pokedex_open  or not self.bag_open:
                        self.poke_party_open = not self.poke_party_open
                        self.player.blocked = not self.player.blocked
                        self.poke_party.current_window = 'party'
                if keys[pygame.K_b]:
                    if not self.battle_open:
                        self.battle_open = not self.battle_open
                        self.player.blocked = not self.player.blocked

        elif self.dialog_tree:
            self.dialog_tree.input()

    def create_dialog(self, character=None, narration=None, non_character=None):
        if not self.dialog_tree:
            if character:
                self.dialog_tree = DialogTree(self.all_sprites, self.fonts['dialog'], self.display_surface, self.end_dialog, character=character)
            elif narration:
                self.dialog_tree = DialogTree(self.all_sprites, self.fonts['dialog'], self.display_surface, self.end_dialog, narration=narration)
            elif non_character:
                self.dialog_tree = DialogTree(self.all_sprites, self.fonts['dialog'], self.display_surface, self.end_dialog, non_character=non_character)
            else:
                raise ValueError("Neither character nor narration has been specified.")

    def end_dialog(self, result = None):
        self.dialog_tree = None
        if result == 'starter':
            self.starter_select = StarterSelect(self.display_surface, self.pokemon_graphics['battle_sprites'], self.fonts)
        else:
            if self.player:
                self.player.unblock()

    def draw_dialog(self):
        for sprite in self.all_sprites:
            if isinstance(sprite, DialogSprite):
                sprite.draw()

    def get_opponent_pokemon(self, opponent_name):
        return {index: Pokemon(*TRAINER_DATA[opponent_name]['pokemon'][index]) for index, pokemon_list in TRAINER_DATA[opponent_name]['pokemon'].items()}

    def transition_check(self):
        sprites = [sprite for sprite in self.transition_sprites if sprite.rect.colliderect(self.player.hitbox)]
        if sprites:
            self.player.block()
            self.transition_target = sprites[0].target[0]
            self.transition_pos = sprites[0].target[1]
            self.start_fade()

    def run(self):
        while True:
            dt = self.clock.tick() / 1000
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            if not self.fading:
                self.input()

            self.transition_check()

            if self.scene:
                if self.scene["scene_type"] == 'cutscene':
                    if not self.fading:
                        self.cutscene.update(dt)
                elif self.scene["scene_type"] == 'game':
                    self.all_sprites.update(dt)

                self.display_surface.fill('black')

                if self.scene["scene_type"] == 'cutscene':
                    self.cutscene.draw()
                elif self.scene["scene_type"] == 'game':
                    self.all_sprites.draw(self.get_camera_pos())

            # overlays
            if self.dialog_tree and not self.fading: self.dialog_tree.update()
            if self.pokedex_open: self.pokedex.update(dt)
            if self.poke_party_open: self.poke_party.update(dt)
            if self.battle_open: self.battle.update(dt)
            if self.bag_open: self.bag.update(dt)
            if self.starter_select: self.starter_select.update(dt)

            if self.battle.battle_finished:
                self.battle_open = False
                self.player.blocked = not self.player.blocked

            self.draw_dialog()

            if self.fading:
                self.fade(dt)

            if self.fade_complete:
                self.change_scene()
                self.fade_complete = False

            pygame.display.update()

if __name__ == '__main__':
    game = Game()
    game.run()