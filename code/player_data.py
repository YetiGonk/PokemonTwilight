import random

POKEMON = {
    0: None,
    1: None,
    2: None,
    3: None,
    4: None,
    5: None
}

BOX_POKEMON = {}

DISCOVERED_POKEMON = ['decidueye','magneton','azumarill','sawsbuck','arcanine','lopunny','piloswine']

CAUGHT_POKEMON = ['decidueye','magneton','azumarill','sawsbuck','arcanine','lopunny','piloswine']

BAG = {
    "items": [
        {'name': 'quick-claw', 'count': 1},
        {'name': 'kings-rock', 'count': 1},
        {'name': 'amulet-coin', 'count': 1},
        {'name': 'black-belt', 'count': 1},
        {'name': 'black-glasses', 'count': 1},
        {'name': 'charcoal', 'count': 1},
        {'name': 'choice-band', 'count': 1}
    ],
    "medicine": [
        {'name': 'antidote', 'count': random.randint(1, 10)},
        {'name': 'paralyze-heal', 'count': random.randint(1, 10)},
        {'name': 'burn-heal', 'count': random.randint(1, 10)},
        {'name': 'ice-heal', 'count': random.randint(1, 10)},
        {'name': 'awakening', 'count': random.randint(1, 10)},
        {'name': 'full-restore', 'count': random.randint(1, 10)},
        {'name': 'elixir', 'count': random.randint(1, 10)},
        {'name': 'max-potion', 'count': random.randint(1, 10)},
    ],
    "balls": [
        {'name': 'poke', 'count': random.randint(1, 10)},
        {'name': 'great', 'count': random.randint(1, 10)},
        {'name': 'ultra', 'count': random.randint(1, 10)},
        {'name': 'master', 'count': random.randint(1, 10)},
        {'name': 'net', 'count': random.randint(1, 10)},
        {'name': 'timer', 'count': random.randint(1, 10)},
        {'name': 'dive', 'count': random.randint(1, 10)},
        {'name': 'luxury', 'count': random.randint(1, 10)},
    ],
    "battle-items": [
        {'name': 'x-attack', 'count': random.randint(1, 10)},
        {'name': 'x-defense', 'count': random.randint(1, 10)},
        {'name': 'x-speed', 'count': random.randint(1, 10)},
        {'name': 'x-sp-def', 'count': random.randint(1, 10)},
        {'name': 'dire-hit', 'count': random.randint(1, 10)},
        {'name': 'guard-spec', 'count': random.randint(1, 10)},
        {'name': 'x-accuracy', 'count': random.randint(1, 10)},
        {'name': 'x-sp-atk', 'count': random.randint(1, 10)},
    ],
    "berries": [
        {'name': 'oran', 'count': random.randint(1, 10)},
        {'name': 'sitrus', 'count': random.randint(1, 10)},
        {'name': 'charti', 'count': random.randint(1, 10)},
        {'name': 'chesto', 'count': random.randint(1, 10)},
        {'name': 'pecha', 'count': random.randint(1, 10)},
        {'name': 'rawst', 'count': random.randint(1, 10)},
        {'name': 'aspear', 'count': random.randint(1, 10)},
        {'name': 'leppa', 'count': random.randint(1, 10)},
    ],
    "tms": [
        {'name': 'grass-knot', 'count': 1},
        {'name': 'nasty-plot', 'count': 1},
        {'name': 'breaking-swipe', 'count': 1}
    ],
    "key-items": [
        {'name': 'bicycle', 'count': 1},
        {'name': 'super-rod', 'count': 1},
        {'name': 'good-rod', 'count': 1},
        {'name': 'old-rod', 'count': 1},
        {'name': 'town-map', 'count': 1},
        {'name': 'shiny-charm', 'count': 1},
        {'name': 'oval-charm', 'count': 1},
        {'name': 'exp-share', 'count': 1}
    ]
}

BATTLES = {}

BADGES = {}