from settings import *
from game_data import *
from pytmx.util_pygame import load_pygame
from os.path import join

from sprites import Sprite, AnimatedSprite
from entities import Player
from groups import AllSprites
from dialog import DialogTree

from support import *

class Intro:
    def __init__(self, tmx_map):
        self.tmx_map = tmx_map
        pass

    def setup(self):
        for x, y, surf in self.tmx_map.get_layer_by_name('Background').tiles():
            Sprite((x * TILE_SIZE, y * TILE_SIZE), surf, self.all_sprites, WORLD_LAYERS['bg'])
        for obj in self.tmx_map.get_layer_by_name('Objects'):
            Sprite((obj.x, obj.y), obj.image, self.all_sprites, WORLD_LAYERS['main'])
        for obj in self.tmx_map.get_layer_by_name('Entities'):
            Sprite((obj.x, obj.y), obj.image, self.all_sprites, WORLD_LAYERS['top'])
