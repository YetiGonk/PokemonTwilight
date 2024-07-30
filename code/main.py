from settings import *
from game_data import *
from pytmx.util_pygame import load_pygame
from os.path import join

from sprites import Sprite, AnimatedSprite, PokemonPatchSprite, BorderSprite, CollidableSprite
from entities import Player, Character
from groups import AllSprites
from cutscenes import TitleIntro, Classroom
from dialog import DialogTree, DialogSprite
from support import *

class Game:
    def __init__(self):
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Pokémon Twilight")
        self.clock = pygame.time.Clock()

        self.fade_screen = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.fade_screen.fill(COLOURS['white'])
        self.fade_alpha = 255
        self.fade('in')

        self.player_gender = 'hilda'

        # groups
        self.all_sprites = AllSprites()
        self.collision_sprites = pygame.sprite.Group()
        self.character_sprites = pygame.sprite.Group()

        self.dialog_tree = None

        self.import_assets()
        self.start_story()
        self.cutscene = TitleIntro(self.all_sprites, self.display_surface, self.fonts['dialog'], dad_obj={'portrait': self.portraits['characters']['dad'], 'dialog': TRAINER_DATA['dad intro']}, game=self)


    def fade(self, direction, speed=5):
        if direction == 'in':
            fade_speed = speed
            self.fade_alpha -= fade_speed
            if self.fade_alpha <= 0:
                self.fade_alpha = 0
        elif direction == 'out':
            fade_speed = speed
            self.fade_alpha += fade_speed
            if self.fade_alpha >= 255:
                self.fade_alpha = 255
        self.fade_screen.set_alpha(self.fade_alpha)

    def start_story(self):
        self.scene = MAP_ORDER['forest_road']
        self.load_setup(self.scene['player_pos'])

    def load_setup(self, player_pos):
        if self.scene["scene_type"] == 'cutscene':
            self.setup_cutscene(self.tmx_maps[self.scene["map_name"]])
        elif self.scene["scene_type"] == 'game':
            self.setup(self.tmx_maps[self.scene["map_name"]], player_pos)

    def get_camera_pos(self):
        if self.scene["camera"] == 'player':
            return self.player.rect.center
        if self.scene["camera"] == 'locked':
            return self.scene["camera_pos"]
        if self.scene["camera"] == 'track':
            return self.cutscene.car.rect.center
        else:
            return (0, 0)

    def import_assets(self):
        self.tmx_maps = {
            'forest_road': load_pygame(join('..', 'data', 'maps', 'forest_road.tmx')),
            'classroom': load_pygame(join('..', 'data', 'maps', 'classroom.tmx'))
        }

        self.overworld_frames = {
            'characters': all_character_import(join('..', 'graphics', 'characters', 'overworld'))
        }

        self.fonts = {
            'dialog': pygame.font.Font(join('..', 'graphics', 'fonts', 'PixeloidSans.ttf'), 30)
        }

        self.portraits = {
            'characters': import_folder_dict(join('..', 'graphics', 'characters', 'portrait'))
        }

    def setup_cutscene(self, tmx_map):
        for x, y, surf in tmx_map.get_layer_by_name('Terrain').tiles():
            Sprite((x * TILE_SIZE, y * TILE_SIZE), surf, self.all_sprites, WORLD_LAYERS['bg'])

        if 'Terrain Top' in tmx_map.layers:
            for x, y, surf in tmx_map.get_layer_by_name('Terrain Top').tiles():
                Sprite((x * TILE_SIZE, y * TILE_SIZE), surf, self.all_sprites, WORLD_LAYERS['bg'])

        for obj in tmx_map.get_layer_by_name('Objects'):
            Sprite((obj.x, obj.y), obj.image, self.all_sprites)

        if 'Entities' in tmx_map.layers:
            for obj in tmx_map.get_layer_by_name('Entities'):
                Character(
                    pos = (obj.x, obj.y),
                    frames = self.overworld_frames['characters'][obj.properties['graphic']],
                    groups = (self.all_sprites, self.collision_sprites, self.character_sprites),
                    facing_direction = obj.properties['direction'],
                    character_data = TRAINER_DATA[obj.properties['character_id']],
                    portrait = self.portraits['characters'][obj.properties['graphic']]
                )

    def setup(self, tmx_map, player_start_pos):
        for layer in ['Terrain', 'Terrain Top']:
            for x, y, surf in tmx_map.get_layer_by_name(layer).tiles():
                Sprite((x * TILE_SIZE, y * TILE_SIZE), surf, self.all_sprites, WORLD_LAYERS['bg'])

        for obj in tmx_map.get_layer_by_name('Objects'):
            CollidableSprite((obj.x, obj.y), obj.image, (self.all_sprites, self.collision_sprites))
            
        for obj in tmx_map.get_layer_by_name('Collisions'):
            BorderSprite((obj.x, obj.y), pygame.Surface((obj.width, obj.height)), self.collision_sprites)

        # for obj in tmx_map.get_layer_by_name('Grass Patches'):
        #     PokemonPatchSprite((obj.x, obj.y), obj.image, self.all_sprites)

        for obj in tmx_map.get_layer_by_name('Entities'):
            if obj.name == 'Player':
                if obj.properties['pos'] == player_start_pos:
                    self.player = Player(
                        pos = (obj.x, obj.y),
                        frames = self.overworld_frames['characters'][self.player_gender],
                        groups = self.all_sprites,
                        facing_direction = obj.properties['direction'],
                        collision_sprites = self.collision_sprites
                    )
            else: 
                Character(
                    pos = (obj.x, obj.y),
                    frames = self.overworld_frames['characters'][obj.properties['graphic']],
                    groups = (self.all_sprites, self.collision_sprites, self.character_sprites),
                    facing_direction = obj.properties['direction'],
                    character_data = TRAINER_DATA[obj.properties['character_id']],
                    portrait = self.portraits['characters'][obj.properties['graphic']]
                )

    def input(self):
        if not self.dialog_tree:
            keys = pygame.key.get_just_pressed()
            if keys[pygame.K_SPACE]:
                for character in self.character_sprites:
                    if check_connection(48, self.player, character):
                        self.player.block()
                        character.change_facing_direction(self.player.rect.center)
                        self.create_dialog(character=character)

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


    def end_dialog(self):
        self.dialog_tree = None
        if self.player:
            self.player.unblock()

    def draw_dialog(self):
        for sprite in self.all_sprites:
            if isinstance(sprite, DialogSprite):
                sprite.draw()

    def run(self):
        while True:
            dt = self.clock.tick() / 1000
            # event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            # game logic
            self.input()
            if self.scene["scene_type"] == 'cutscene':
                self.cutscene.update(dt)
            elif self.scene["scene_type"] == 'game':
                self.all_sprites.update(dt)

            # draw everything
            self.display_surface.fill('black')

            if self.scene["scene_type"] == 'cutscene':
                self.cutscene.draw()
            elif self.scene["scene_type"] == 'game':
                self.all_sprites.draw(self.get_camera_pos())

            if self.dialog_tree:
                self.dialog_tree.update()
            
            self.draw_dialog()

            # draw fade screen
            if self.fade_screen.get_alpha() > 0:
                self.fade('in')
                self.display_surface.blit(self.fade_screen, (0, 0))

            pygame.display.update()

if __name__ == '__main__':
    game = Game()
    game.run()