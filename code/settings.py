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
	'dark-grey': '#2b292c',
	'light': '#c8c8c8',
	'grey': '#3a373b',
	'gold': '#ffd700',
	'light-grey': '#4b484d',
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
	'blue': '#66d7ee',
    'amber': '#ffBf00',
    'green': '#6fc276',
    'navy': '#0d47a1'
}

WORLD_LAYERS = {
	'water': 0,
	'bg': 1,
	'shadow': 2,
	'main': 3,
	'top': 4
}

MAP_ORDER = {
    'forest_road_intro': {
        "map_name": 'forest_road',
        "scene_type": 'cutscene',
        "camera": 'track',
        "player_pos": 'car'
    },
    'forest_road_dad': {
        "map_name": 'forest_road',
        "scene_type": 'cutscene',
        "camera": 'track',
        "player_pos": 'car'
    },
    'classroom_intro': {
        "map_name": 'classroom_intro',
        "scene_type": 'cutscene',
        "camera": 'locked',
        "player_pos": None
	},
    'classroom': {
        "map_name": 'classroom',
        "scene_type": 'game',
        "player_pos": 'seat'
	},
    'schoolyard': {
        "map_name": 'schoolyard',
        "scene_type": 'game',
        "player_pos": 'entrance'
    }
}

CUTSCENE_ORDER = ['title_intro', 'dad_intro', 'classroom']

BATTLE_CHOICES = {
    'fight': {'pos': vector(-343.6*2/3, -352.4*2/3), 'icon': 'fight'},
    'bag': {'pos': vector(-156.7*2/3, -520*2/3), 'icon': 'bag'},
    'party': {'pos': vector(159.7*2/3, -515.9*2/3), 'icon': 'party'},
    'run': {'pos': vector(331*2/3, -346.5*2/3), 'icon': 'run'}
}

BATTLE_ROUND_FLOW = ['select', 'resolve_damage', 'apply_effects', 'text', 'resolve_damage', 'apply_effects', 'text']

BATTLE_TEXT = {
    'trainer run': ["There's no running from a trainer battle!"],
    'attempt run': ["You tried to run!"],
    'fail run': ["You couldn't get away!"],
    'success run': ["You got away safely!"],
    'party full': ["Oops! You've got no space in your party!", "Sending to your box..."],
    'shake 0': ["Oh no! The pokemon broke free!"],
    'shake 1': ["Aww! It appeared to be caught!"],
    'shake 2': ["Argh! Almost had it!"],
    'shake 3': ["Shoot, it was so close too!"]
}