import pygame
from pygame.math import Vector2 as vector 
from sys import exit

WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
TILE_SIZE = 32
ANIMATION_SPEED = 4
BATTLE_OUTLINE_WIDTH = 4

COLOURS = {
	'white': '#f4fefa', 
	'pure white': '#ffffff',
	'dark': '#2b292c',
	'light': '#c8c8c8',
	'gray': '#3a373b',
	'gold': '#ffd700',
	'light-gray': '#4b484d',
    'normal': '#A8A77A',
    'fire': '#EE8130',
    'water': '#6390F0',
    'electric': '#F7D02C',
    'grass': '#7AC74C',
    'ice': '#96D9D6',
    'fighting': '#C22E28',
    'poison': '#A33EA1',
    'ground': '#E2BF65',
    'flying': '#A98FF3',
    'psychic': '#F95587',
    'bug': '#A6B91A',
    'rock': '#B6A136',
    'ghost': '#735797',
    'dragon': '#6F35FC',
    'dark': '#705746',
    'steel': '#B7B7CE',
    'fairy': '#D685AD',
	'black': '#000000', 
	'red': '#f03131',
	'blue': '#66d7ee'
}

WORLD_LAYERS = {
	'water': 0,
	'bg': 1,
	'shadow': 2,
	'main': 3,
	'top': 4
}

BATTLE_POSITIONS = {
	'player': (360, 260),
	'opponent': (900, 260)
}

BATTLE_LAYERS =  {
	'bg': 0,
	'podiums': 1,
	'monster': 2,
	'effects': 3,
	'overlay': 4
}

MAP_ORDER = {
    'forest_road': {
        "map_name": 'forest_road',
        "scene_type": 'cutscene',
        "camera": 'track',
        "player_pos": 'car'
    },
    'classroom_intro': {
        "map_name": 'classroom',
        "scene_type": 'cutscene',
        "camera": 'locked',
        "player_pos": (0,0)
	},
    'classroom': {
        "map_name": 'classroom',
        "scene_type": 'game',
        "camera": 'player',
        "player_pos": 'seat'
	}
}