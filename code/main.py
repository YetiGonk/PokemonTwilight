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
from pokemon_data import POKEMON_DATA

class Game:
    def __init__(self):
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Pokémon Twilight")
        self.clock = pygame.time.Clock()

        self.player_pokemon = {
            0: Pokemon('decidueye', 36),
            1: Pokemon('magneton', 40),
            2: Pokemon('azumarill', 32),
            3: Pokemon('sawsbuck', 36),
            4: Pokemon('arcanine', 32),
            5: Pokemon('lopunny', 36)
        }

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

        self.cutscene_index = 2
        self.scene = None
        self.cutscene = self.load_cutscene_setup()
        
        print(list(POKEMON_DATA.keys()))

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

    def start_fade(self):
        self.fading = True
        self.fade_direction = 'out'
        print(self.fade_direction)
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
            'pokeball': import_image(join('..', 'graphics', 'other', 'pokeball'))
        }

        self.fonts = {
            'dialog': pygame.font.Font(join('..', 'graphics', 'fonts', 'PixeloidSans.ttf'), 30),
            'large': pygame.font.Font(join('..', 'graphics', 'fonts', 'PixeloidSans.ttf'), 24),
            'regular': pygame.font.Font(join('..', 'graphics', 'fonts', 'PixeloidSans.ttf'), 18),
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
        print(f"Setting up game with map: {tmx_map}")
        
        self.all_sprites.empty()
        self.collision_sprites.empty()
        self.character_sprites.empty()
        self.transition_sprites.empty()

        layer_names = [layer.name for layer in tmx_map.layers]

        for layer in ['Terrain', 'Terrain Top']:
            for x, y, surf in tmx_map.get_layer_by_name(layer).tiles():
                print(f"Drawing terrain at ({x}, {y})")
                Sprite((x * TILE_SIZE, y * TILE_SIZE), surf, self.all_sprites, WORLD_LAYERS['bg'])

        for obj in tmx_map.get_layer_by_name('Objects'):
            print(f"Placing object at ({obj.x}, {obj.y})")
            CollidableSprite((obj.x, obj.y), obj.image, (self.all_sprites, self.collision_sprites))

        for obj in tmx_map.get_layer_by_name('Collisions'):
            BorderSprite((obj.x, obj.y), pygame.Surface((obj.width, obj.height)), self.collision_sprites)

        for obj in tmx_map.get_layer_by_name('Transitions'):
            print(f"Adding transition at ({obj.x}, {obj.y}) to {obj.properties['target']} at {obj.properties['pos']}")
            TransitionSprite((obj.x, obj.y), (obj.width, obj.height), (obj.properties['target'], obj.properties['pos']), self.transition_sprites)

        if 'Grass Patches' in layer_names:
            for obj in tmx_map.get_layer_by_name('Grass Patches'):
                PokemonPatchSprite((obj.x, obj.y), obj.image, self.all_sprites)

        for obj in tmx_map.get_layer_by_name('Entities'):
            if obj.name == 'Player' and obj.properties['pos'] == player_start_pos:
                print(f"Adding player with {obj.properties}")
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
        if not self.dialog_tree:
            if self.scene["scene_type"] == 'game':
                keys = pygame.key.get_just_pressed()
                if keys[pygame.K_SPACE]:
                    for character in self.character_sprites:
                        if check_connection(48, self.player, character):
                            self.player.block()
                            character.change_facing_direction(self.player.rect.center)
                            self.create_dialog(character=character)
                if keys[pygame.K_RETURN]:
                    self.pokedex_open = not self.pokedex_open
                    self.player.blocked = not self.player.blocked
        else:
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
            self.load_starter_select()
        else:
            if self.player:
                self.player.unblock()

    def draw_dialog(self):
        for sprite in self.all_sprites:
            if isinstance(sprite, DialogSprite):
                sprite.draw()

    def load_starter_select(self):
        print('yuh!!!!!')
        self.player.unblock()

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