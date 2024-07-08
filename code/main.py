from settings import *
from pytmx.util_pygame import load_pygame
from os.path import join

from sprites import Sprite
from entities import Player, CutsceneEntity
from groups import AllSprites

class Game:
    def __init__(self):
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Pokémon Twilight")
        self.clock = pygame.time.Clock()

        # groups
        self.all_sprites = AllSprites()

        self.import_assets()
        self.start_story()

    def start_story(self):
        self.scene = INTRO_MAP_ORDER['title']
        self.load_setup()

    def load_setup(self):
        if self.scene["scene_type"] == 'cutscene':
            self.setup_cutscene(self.tmx_maps[self.scene["map_name"]])
        elif self.scene["scene_type"] == 'game':
            self.setup(self.tmx_maps[self.scene["map_name"]])
    
    def get_camera_pos(self):
        if self.scene["camera"] == 'player':
            return self.player.rect.center
        if self.scene["camera"] == 'locked':
            return self.scene["camera_pos"]

    def import_assets(self):
        self.tmx_maps = {'forest_road':load_pygame(join('..','data','maps','forest_road.tmx'))}

    def setup_cutscene(self, tmx_map):
        for x, y, surf in tmx_map.get_layer_by_name('Terrain').tiles():
            Sprite((x * TILE_SIZE, y * TILE_SIZE), surf, self.all_sprites)
        
        for x, y, surf in tmx_map.get_layer_by_name('Cutscene Objs').tiles():
            Sprite((x * TILE_SIZE, y * TILE_SIZE), surf, self.all_sprites)

        for obj in tmx_map.get_layer_by_name('Entities'):
            if obj.name == 'Player':
                self.player = Player((obj.x, obj.y), self.all_sprites)

    def setup(self, tmx_map, player_pos):
        for x,y,surf in tmx_map.get_layer_by_name('Terrain').tiles():
            Sprite((x * TILE_SIZE, y * TILE_SIZE), surf, self.all_sprites)
        
        for obj in tmx_map.get_layer_by_name('Objects'):
            Sprite((obj.x, obj.y), obj.image, self.all_sprites)
        
        for obj in tmx_map.get_layer_by_name('Entities'):
            if obj.name == 'Player' and obj.properties['pos'] == player_start_pos:
                self.player = Player((obj.x, obj.y), self.all_sprites)

    def run(self):
        while True:
            dt = self.clock.tick() / 1000
            # event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
            # game logic
            self.all_sprites.update(dt)
            self.display_surface.fill('black')
            self.all_sprites.draw(self.get_camera_pos())
            pygame.display.update()

if __name__ == '__main__':
    game = Game()
    game.run()
            