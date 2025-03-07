MOVE_DATA = {
    "double-kick": {
        "name": "double-kick",
        "id": 24,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 30,
        "power": 30,
        "type": "fighting",
        "damage_class": "physical",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": 2,
            "max_turns": None,
            "min_hits": 2,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Hits twice in one turn.",
        "flavor_text_entry": "A double kicking attack."
    },
    "jump-kick": {
        "name": "jump-kick",
        "id": 26,
        "accuracy": 95,
        "priority": 0,
        "max_pp": 10,
        "power": 100,
        "type": "fighting",
        "damage_class": "physical",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "If the user misses, it takes half the damage it would have inflicted in recoil.",
        "flavor_text_entry": "A strong jumping kick. May miss and hurt the kicker."
    },
    "sand-attack": {
        "name": "sand-attack",
        "id": 28,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 15,
        "power": None,
        "type": "ground",
        "damage_class": "status",
        "stat_changes": [
            {
                "change": -1,
                "stat": {
                    "name": "accuracy",
                    "url": "https://pokeapi.co/api/v2/stat/7/"
                }
            }
        ],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "net-good-stats",
                "url": "https://pokeapi.co/api/v2/move-category/2/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Lowers the target's accuracy by one stage.",
        "flavor_text_entry": "Reduces accuracy by throwing sand."
    },
    "headbutt": {
        "name": "headbutt",
        "id": 29,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 15,
        "power": 70,
        "type": "normal",
        "damage_class": "physical",
        "stat_changes": [],
        "effect_chance": 30,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 30,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Has a 30% chance to make the target flinch.",
        "flavor_text_entry": "An attack that may make foe flinch."
    },
    "tackle": {
        "name": "tackle",
        "id": 33,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 35,
        "power": 40,
        "type": "normal",
        "damage_class": "physical",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Inflicts regular damage with no additional effect.",
        "flavor_text_entry": "A full-body charge attack."
    },
    "body-slam": {
        "name": "body-slam",
        "id": 34,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 15,
        "power": 85,
        "type": "normal",
        "damage_class": "physical",
        "stat_changes": [],
        "effect_chance": 30,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "paralysis",
                "url": "https://pokeapi.co/api/v2/move-ailment/1/"
            },
            "ailment_chance": 30,
            "category": {
                "name": "damage+ailment",
                "url": "https://pokeapi.co/api/v2/move-category/4/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Has a 30% chance to paralyze the target.",
        "flavor_text_entry": "An attack that may cause paralysis."
    },
    "take-down": {
        "name": "take-down",
        "id": 36,
        "accuracy": 85,
        "priority": 0,
        "max_pp": 20,
        "power": 90,
        "type": "normal",
        "damage_class": "physical",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 0,
            "drain": -25,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "User receives 1/4 the damage it inflicts in recoil.",
        "flavor_text_entry": "A tackle that also hurts the user."
    },
    "double-edge": {
        "name": "double-edge",
        "id": 38,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 15,
        "power": 120,
        "type": "normal",
        "damage_class": "physical",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 0,
            "drain": -33,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "User receives 1/3 the damage inflicted in recoil.",
        "flavor_text_entry": "A tackle that also hurts the user."
    },
    "growl": {
        "name": "growl",
        "id": 45,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 40,
        "power": None,
        "type": "normal",
        "damage_class": "status",
        "stat_changes": [
            {
                "change": -1,
                "stat": {
                    "name": "Atk",
                    "url": "https://pokeapi.co/api/v2/stat/2/"
                }
            }
        ],
        "effect_chance": None,
        "target": "all-opponents",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "net-good-stats",
                "url": "https://pokeapi.co/api/v2/move-category/2/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Lowers the target's Attack by one stage.",
        "flavor_text_entry": "Reduces the foe's ATTACK."
    },
    "leech-seed": {
        "name": "leech-seed",
        "id": 73,
        "accuracy": 90,
        "priority": 0,
        "max_pp": 10,
        "power": None,
        "type": "grass",
        "damage_class": "status",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "leech-seed",
                "url": "https://pokeapi.co/api/v2/move-ailment/18/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "ailment",
                "url": "https://pokeapi.co/api/v2/move-category/1/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Seeds the target, stealing HP from it every turn.",
        "flavor_text_entry": "Steals HP from the foe on every turn."
    },
    "solar-beam": {
        "name": "solar-beam",
        "id": 76,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 10,
        "power": 120,
        "type": "grass",
        "damage_class": "special",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Requires a turn to charge before attacking.",
        "flavor_text_entry": "1st turn: Prepare 2nd turn: Attack"
    },
    "thunder-wave": {
        "name": "thunder-wave",
        "id": 86,
        "accuracy": 90,
        "priority": 0,
        "max_pp": 20,
        "power": None,
        "type": "electric",
        "damage_class": "status",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "paralysis",
                "url": "https://pokeapi.co/api/v2/move-ailment/1/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "ailment",
                "url": "https://pokeapi.co/api/v2/move-category/1/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Paralyzes the target.",
        "flavor_text_entry": "A move that may cause paralysis."
    },
    "dig": {
        "name": "dig",
        "id": 91,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 10,
        "power": 80,
        "type": "ground",
        "damage_class": "physical",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "User digs underground, dodging all attacks, and hits next turn.",
        "flavor_text_entry": "1st turn: Burrow 2nd turn: Attack"
    },
    "toxic": {
        "name": "toxic",
        "id": 92,
        "accuracy": 90,
        "priority": 0,
        "max_pp": 10,
        "power": None,
        "type": "poison",
        "damage_class": "status",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "poison",
                "url": "https://pokeapi.co/api/v2/move-ailment/5/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "ailment",
                "url": "https://pokeapi.co/api/v2/move-category/1/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": 15,
            "min_hits": None,
            "min_turns": 15,
            "stat_chance": 0
        },
        "effect_entries": "Badly poisons the target, inflicting more damage every turn.",
        "flavor_text_entry": "Poisons the foe with an intensifying toxin."
    },
    "agility": {
        "name": "agility",
        "id": 97,
        "accuracy": None,
        "priority": 0,
        "max_pp": 30,
        "power": None,
        "type": "psychic",
        "damage_class": "status",
        "stat_changes": [
            {
                "change": 2,
                "stat": {
                    "name": "Speed",
                    "url": "https://pokeapi.co/api/v2/stat/6/"
                }
            }
        ],
        "effect_chance": None,
        "target": "user",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "net-good-stats",
                "url": "https://pokeapi.co/api/v2/move-category/2/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Raises the user's Speed by two stages.",
        "flavor_text_entry": "Sharply increases the user's SPEED."
    },
    "double-team": {
        "name": "double-team",
        "id": 104,
        "accuracy": None,
        "priority": 0,
        "max_pp": 15,
        "power": None,
        "type": "normal",
        "damage_class": "status",
        "stat_changes": [
            {
                "change": 1,
                "stat": {
                    "name": "evasion",
                    "url": "https://pokeapi.co/api/v2/stat/8/"
                }
            }
        ],
        "effect_chance": None,
        "target": "user",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "net-good-stats",
                "url": "https://pokeapi.co/api/v2/move-category/2/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Raises the user's evasion by one stage.",
        "flavor_text_entry": "Heightens evasive\u00ad ness."
    },
    "light-screen": {
        "name": "light-screen",
        "id": 113,
        "accuracy": None,
        "priority": 0,
        "max_pp": 30,
        "power": None,
        "type": "psychic",
        "damage_class": "status",
        "stat_changes": [],
        "effect_chance": None,
        "target": "users-field",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "field-effect",
                "url": "https://pokeapi.co/api/v2/move-category/11/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Reduces damage from special attacks by 50% for five turns.",
        "flavor_text_entry": "Ups SPCL.DEF with a wall of light."
    },
    "flash": {
        "name": "flash",
        "id": 148,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 20,
        "power": None,
        "type": "normal",
        "damage_class": "status",
        "stat_changes": [
            {
                "change": -1,
                "stat": {
                    "name": "accuracy",
                    "url": "https://pokeapi.co/api/v2/stat/7/"
                }
            }
        ],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "net-good-stats",
                "url": "https://pokeapi.co/api/v2/move-category/2/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Lowers the target's accuracy by one stage.",
        "flavor_text_entry": "Blinds the foe to reduce accuracy."
    },
    "rest": {
        "name": "rest",
        "id": 156,
        "accuracy": None,
        "priority": 0,
        "max_pp": 5,
        "power": None,
        "type": "psychic",
        "damage_class": "status",
        "stat_changes": [],
        "effect_chance": None,
        "target": "user",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "unique",
                "url": "https://pokeapi.co/api/v2/move-category/13/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "User sleeps for two turns, completely healing itself.",
        "flavor_text_entry": "Sleep for 2 turns to fully recover."
    },
    "substitute": {
        "name": "substitute",
        "id": 164,
        "accuracy": None,
        "priority": 0,
        "max_pp": 10,
        "power": None,
        "type": "normal",
        "damage_class": "status",
        "stat_changes": [],
        "effect_chance": None,
        "target": "user",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "unique",
                "url": "https://pokeapi.co/api/v2/move-category/13/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Transfers 1/4 of the user's max HP into a doll, protecting the user from further damage or status changes until it breaks.",
        "flavor_text_entry": "Makes a decoy with 1/4 user's max HP."
    },
    "snore": {
        "name": "snore",
        "id": 173,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 15,
        "power": 50,
        "type": "normal",
        "damage_class": "special",
        "stat_changes": [],
        "effect_chance": 30,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 30,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Has a 30% chance to make the target flinch.  Only works if the user is sleeping.",
        "flavor_text_entry": "An attack useable only while asleep."
    },
    "protect": {
        "name": "protect",
        "id": 182,
        "accuracy": None,
        "priority": 4,
        "max_pp": 10,
        "power": None,
        "type": "normal",
        "damage_class": "status",
        "stat_changes": [],
        "effect_chance": None,
        "target": "user",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "unique",
                "url": "https://pokeapi.co/api/v2/move-category/13/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Prevents any moves from hitting the user this turn.",
        "flavor_text_entry": "Foils attack that turn. It may fail."
    },
    "feint-attack": {
        "name": "feint-attack",
        "id": 185,
        "accuracy": None,
        "priority": 0,
        "max_pp": 20,
        "power": 60,
        "type": "dark",
        "damage_class": "physical",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Never misses.",
        "flavor_text_entry": "An attack that never misses."
    },
    "giga-drain": {
        "name": "giga-drain",
        "id": 202,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 10,
        "power": 75,
        "type": "grass",
        "damage_class": "special",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage+heal",
                "url": "https://pokeapi.co/api/v2/move-category/8/"
            },
            "crit_rate": 0,
            "drain": 50,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Drains half the damage inflicted to heal the user.",
        "flavor_text_entry": "Steals 1/2 of the damage inflicted."
    },
    "endure": {
        "name": "endure",
        "id": 203,
        "accuracy": None,
        "priority": 4,
        "max_pp": 10,
        "power": None,
        "type": "normal",
        "damage_class": "status",
        "stat_changes": [],
        "effect_chance": None,
        "target": "user",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "unique",
                "url": "https://pokeapi.co/api/v2/move-category/13/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Prevents the user's HP from lowering below 1 this turn.",
        "flavor_text_entry": "Always leaves at least 1HP."
    },
    "charm": {
        "name": "charm",
        "id": 204,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 20,
        "power": None,
        "type": "fairy",
        "damage_class": "status",
        "stat_changes": [
            {
                "change": -2,
                "stat": {
                    "name": "Atk",
                    "url": "https://pokeapi.co/api/v2/stat/2/"
                }
            }
        ],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "net-good-stats",
                "url": "https://pokeapi.co/api/v2/move-category/2/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Lowers the target's Attack by two stages.",
        "flavor_text_entry": "Sharply lowers the foe's ATTACK."
    },
    "swagger": {
        "name": "swagger",
        "id": 207,
        "accuracy": 85,
        "priority": 0,
        "max_pp": 15,
        "power": None,
        "type": "normal",
        "damage_class": "status",
        "stat_changes": [
            {
                "change": 2,
                "stat": {
                    "name": "Atk",
                    "url": "https://pokeapi.co/api/v2/stat/2/"
                }
            }
        ],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "confusion",
                "url": "https://pokeapi.co/api/v2/move-ailment/6/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "swagger",
                "url": "https://pokeapi.co/api/v2/move-category/5/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": 5,
            "min_hits": None,
            "min_turns": 2,
            "stat_chance": 0
        },
        "effect_entries": "Raises the target's Attack by two stages and confuses the target.",
        "flavor_text_entry": "Causes confusion and raises ATTACK."
    },
    "attract": {
        "name": "attract",
        "id": 213,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 15,
        "power": None,
        "type": "normal",
        "damage_class": "status",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "infatuation",
                "url": "https://pokeapi.co/api/v2/move-ailment/7/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "ailment",
                "url": "https://pokeapi.co/api/v2/move-category/1/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Target falls in love if it has the opposite gender, and has a 50% chance to refuse attacking the user.",
        "flavor_text_entry": "Makes the opposite gender infatuated."
    },
    "sleep-talk": {
        "name": "sleep-talk",
        "id": 214,
        "accuracy": None,
        "priority": 0,
        "max_pp": 10,
        "power": None,
        "type": "normal",
        "damage_class": "status",
        "stat_changes": [],
        "effect_chance": None,
        "target": "user",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "unique",
                "url": "https://pokeapi.co/api/v2/move-category/13/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Randomly uses one of the user's other three moves.  Only works if the user is sleeping.",
        "flavor_text_entry": "Randomly attacks while asleep."
    },
    "return": {
        "name": "return",
        "id": 216,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 20,
        "power": None,
        "type": "normal",
        "damage_class": "physical",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Power increases with happiness, up to a maximum of 102.",
        "flavor_text_entry": "An attack that increases in power with friendship."
    },
    "frustration": {
        "name": "frustration",
        "id": 218,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 20,
        "power": None,
        "type": "normal",
        "damage_class": "physical",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Power increases as happiness decreases, up to a maximum of 102.",
        "flavor_text_entry": "An attack based on lack of loyalty."
    },
    "safeguard": {
        "name": "safeguard",
        "id": 219,
        "accuracy": None,
        "priority": 0,
        "max_pp": 25,
        "power": None,
        "type": "normal",
        "damage_class": "status",
        "stat_changes": [],
        "effect_chance": None,
        "target": "users-field",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "field-effect",
                "url": "https://pokeapi.co/api/v2/move-category/11/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Protects the user's field from major status ailments and confusion for five turns.",
        "flavor_text_entry": "Prevents all status problems."
    },
    "baton-pass": {
        "name": "baton-pass",
        "id": 226,
        "accuracy": None,
        "priority": 0,
        "max_pp": 40,
        "power": None,
        "type": "normal",
        "damage_class": "status",
        "stat_changes": [],
        "effect_chance": None,
        "target": "user",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "unique",
                "url": "https://pokeapi.co/api/v2/move-category/13/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Allows the trainer to switch out the user and pass effects along to its replacement.",
        "flavor_text_entry": "Switches while keeping effects."
    },
    "synthesis": {
        "name": "synthesis",
        "id": 235,
        "accuracy": None,
        "priority": 0,
        "max_pp": 5,
        "power": None,
        "type": "grass",
        "damage_class": "status",
        "stat_changes": [],
        "effect_chance": None,
        "target": "user",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "heal",
                "url": "https://pokeapi.co/api/v2/move-category/3/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 50,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Heals the user by half its max HP.  Affected by weather.",
        "flavor_text_entry": "Restores HP (varies by time)."
    },
    "hidden-power": {
        "name": "hidden-power",
        "id": 237,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 15,
        "power": 60,
        "type": "normal",
        "damage_class": "special",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Power and type depend upon user's IVs.  Power can range from 30 to 70.",
        "flavor_text_entry": "The power varies with the POK\u00e9MON."
    },
    "rain-dance": {
        "name": "rain-dance",
        "id": 240,
        "accuracy": None,
        "priority": 0,
        "max_pp": 5,
        "power": None,
        "type": "water",
        "damage_class": "status",
        "stat_changes": [],
        "effect_chance": None,
        "target": "entire-field",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "whole-field-effect",
                "url": "https://pokeapi.co/api/v2/move-category/10/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Changes the weather to rain for five turns.",
        "flavor_text_entry": "Boosts water-type moves for 5 turns."
    },
    "sunny-day": {
        "name": "sunny-day",
        "id": 241,
        "accuracy": None,
        "priority": 0,
        "max_pp": 5,
        "power": None,
        "type": "fire",
        "damage_class": "status",
        "stat_changes": [],
        "effect_chance": None,
        "target": "entire-field",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "whole-field-effect",
                "url": "https://pokeapi.co/api/v2/move-category/10/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Changes the weather to sunny for five turns.",
        "flavor_text_entry": "Boosts fire-type moves for 5 turns."
    },
    "shadow-ball": {
        "name": "shadow-ball",
        "id": 247,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 15,
        "power": 80,
        "type": "ghost",
        "damage_class": "special",
        "stat_changes": [
            {
                "change": -1,
                "stat": {
                    "name": "SpDef",
                    "url": "https://pokeapi.co/api/v2/stat/5/"
                }
            }
        ],
        "effect_chance": 20,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage+lower",
                "url": "https://pokeapi.co/api/v2/move-category/6/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 20
        },
        "effect_entries": "Has a 20% chance to lower the target's Special Defense by one stage.",
        "flavor_text_entry": "An attack that may lower SPCL.DEF."
    },
    "facade": {
        "name": "facade",
        "id": 263,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 20,
        "power": 70,
        "type": "normal",
        "damage_class": "physical",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Power doubles if user is burned, paralyzed, or poisoned.",
        "flavor_text_entry": "Boosts ATTACK when burned, paralyzed, or poisoned."
    },
    "nature-power": {
        "name": "nature-power",
        "id": 267,
        "accuracy": None,
        "priority": 0,
        "max_pp": 20,
        "power": None,
        "type": "normal",
        "damage_class": "status",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "unique",
                "url": "https://pokeapi.co/api/v2/move-category/13/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Uses a move which depends upon the terrain.",
        "flavor_text_entry": "The type of attack varies depending on the location."
    },
    "helping-hand": {
        "name": "helping-hand",
        "id": 270,
        "accuracy": None,
        "priority": 5,
        "max_pp": 20,
        "power": None,
        "type": "normal",
        "damage_class": "status",
        "stat_changes": [],
        "effect_chance": None,
        "target": "ally",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "unique",
                "url": "https://pokeapi.co/api/v2/move-category/13/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Ally's next move inflicts half more damage.",
        "flavor_text_entry": "Boosts the power of the recipient\u2019s moves."
    },
    "endeavor": {
        "name": "endeavor",
        "id": 283,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 5,
        "power": None,
        "type": "normal",
        "damage_class": "physical",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Lowers the target's HP to equal the user's.",
        "flavor_text_entry": "Gains power if the user\u2019s HP is lower than the foe\u2019s HP."
    },
    "secret-power": {
        "name": "secret-power",
        "id": 290,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 20,
        "power": 70,
        "type": "normal",
        "damage_class": "physical",
        "stat_changes": [],
        "effect_chance": 30,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 30,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Has a 30% chance to inflict a status effect which depends upon the terrain.",
        "flavor_text_entry": "An attack with effects that vary by location."
    },
    "camouflage": {
        "name": "camouflage",
        "id": 293,
        "accuracy": None,
        "priority": 0,
        "max_pp": 20,
        "power": None,
        "type": "normal",
        "damage_class": "status",
        "stat_changes": [],
        "effect_chance": None,
        "target": "user",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "unique",
                "url": "https://pokeapi.co/api/v2/move-category/13/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "User's type changes to match the terrain.",
        "flavor_text_entry": "Alters the POK\u00e9MON\u2019s type depending on the location."
    },
    "aromatherapy": {
        "name": "aromatherapy",
        "id": 312,
        "accuracy": None,
        "priority": 0,
        "max_pp": 5,
        "power": None,
        "type": "grass",
        "damage_class": "status",
        "stat_changes": [],
        "effect_chance": None,
        "target": "user-and-allies",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "unique",
                "url": "https://pokeapi.co/api/v2/move-category/13/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Cures the entire party of major status effects.",
        "flavor_text_entry": "Heals all status problems with a soothing scent."
    },
    "fake-tears": {
        "name": "fake-tears",
        "id": 313,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 20,
        "power": None,
        "type": "dark",
        "damage_class": "status",
        "stat_changes": [
            {
                "change": -2,
                "stat": {
                    "name": "SpDef",
                    "url": "https://pokeapi.co/api/v2/stat/5/"
                }
            }
        ],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "net-good-stats",
                "url": "https://pokeapi.co/api/v2/move-category/2/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Lowers the target's Special Defense by two stages.",
        "flavor_text_entry": "Feigns crying to sharply lower the foe\u2019s SP. DEF."
    },
    "odor-sleuth": {
        "name": "odor-sleuth",
        "id": 316,
        "accuracy": None,
        "priority": 0,
        "max_pp": 40,
        "power": None,
        "type": "normal",
        "damage_class": "status",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "no-type-immunity",
                "url": "https://pokeapi.co/api/v2/move-ailment/17/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "ailment",
                "url": "https://pokeapi.co/api/v2/move-category/1/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Forces the target to have no Evade, and allows it to be hit by Normal and Fighting moves even if it's a Ghost.",
        "flavor_text_entry": "Negates the foe\u2019s efforts to heighten evasiveness."
    },
    "grass-whistle": {
        "name": "grass-whistle",
        "id": 320,
        "accuracy": 55,
        "priority": 0,
        "max_pp": 15,
        "power": None,
        "type": "grass",
        "damage_class": "status",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "sleep",
                "url": "https://pokeapi.co/api/v2/move-ailment/2/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "ailment",
                "url": "https://pokeapi.co/api/v2/move-category/1/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": 4,
            "min_hits": None,
            "min_turns": 2,
            "stat_chance": 0
        },
        "effect_entries": "Puts the target to sleep.",
        "flavor_text_entry": "Lulls the foe into sleep with a pleasant melody."
    },
    "bullet-seed": {
        "name": "bullet-seed",
        "id": 331,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 30,
        "power": 25,
        "type": "grass",
        "damage_class": "physical",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": 5,
            "max_turns": None,
            "min_hits": 2,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Hits 2-5 times in one turn.",
        "flavor_text_entry": "Shoots 2 to 5 seeds in a row to strike the foe."
    },
    "bounce": {
        "name": "bounce",
        "id": 340,
        "accuracy": 85,
        "priority": 0,
        "max_pp": 5,
        "power": 85,
        "type": "flying",
        "damage_class": "physical",
        "stat_changes": [],
        "effect_chance": 30,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "paralysis",
                "url": "https://pokeapi.co/api/v2/move-ailment/1/"
            },
            "ailment_chance": 30,
            "category": {
                "name": "damage+ailment",
                "url": "https://pokeapi.co/api/v2/move-category/4/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "User bounces high into the air, dodging all attacks, and hits next turn.",
        "flavor_text_entry": "Bounces up, then down the next turn. May paralyze."
    },
    "magical-leaf": {
        "name": "magical-leaf",
        "id": 345,
        "accuracy": None,
        "priority": 0,
        "max_pp": 20,
        "power": 60,
        "type": "grass",
        "damage_class": "special",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Never misses.",
        "flavor_text_entry": "Attacks with a strange leaf that cannot be evaded."
    },
    "natural-gift": {
        "name": "natural-gift",
        "id": 363,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 15,
        "power": None,
        "type": "normal",
        "damage_class": "physical",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Power and type depend on the held berry.",
        "flavor_text_entry": "The user draws power to attack by using its held Berry. The Berry determines its type and power."
    },
    "last-resort": {
        "name": "last-resort",
        "id": 387,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 5,
        "power": 140,
        "type": "normal",
        "damage_class": "physical",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Can only be used after all of the user's other moves have been used.",
        "flavor_text_entry": "This move can be used only after the user has used all the other moves it knows in the battle."
    },
    "worry-seed": {
        "name": "worry-seed",
        "id": 388,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 10,
        "power": None,
        "type": "grass",
        "damage_class": "status",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "unique",
                "url": "https://pokeapi.co/api/v2/move-category/13/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Changes the target's ability to Insomnia.",
        "flavor_text_entry": "A seed that causes worry is planted on the foe. It prevents sleep by making its ability Insomnia."
    },
    "seed-bomb": {
        "name": "seed-bomb",
        "id": 402,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 15,
        "power": 80,
        "type": "grass",
        "damage_class": "physical",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Inflicts regular damage with no additional effect.",
        "flavor_text_entry": "The user slams a barrage of hard- shelled seeds down on the foe from above."
    },
    "energy-ball": {
        "name": "energy-ball",
        "id": 412,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 10,
        "power": 90,
        "type": "grass",
        "damage_class": "special",
        "stat_changes": [
            {
                "change": -1,
                "stat": {
                    "name": "SpDef",
                    "url": "https://pokeapi.co/api/v2/stat/5/"
                }
            }
        ],
        "effect_chance": 10,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage+lower",
                "url": "https://pokeapi.co/api/v2/move-category/6/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 10
        },
        "effect_entries": "Has a 10% chance to lower the target's Special Defense by one stage.",
        "flavor_text_entry": "The user draws power from nature and fires it at the foe. It may also lower the target\u2019s Sp. Def."
    },
    "zen-headbutt": {
        "name": "zen-headbutt",
        "id": 428,
        "accuracy": 90,
        "priority": 0,
        "max_pp": 15,
        "power": 80,
        "type": "psychic",
        "damage_class": "physical",
        "stat_changes": [],
        "effect_chance": 20,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 20,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Has a 20% chance to make the target flinch.",
        "flavor_text_entry": "The user focuses its willpower to its head and rams the foe. It may also make the target flinch."
    },
    "leaf-storm": {
        "name": "leaf-storm",
        "id": 437,
        "accuracy": 90,
        "priority": 0,
        "max_pp": 5,
        "power": 130,
        "type": "grass",
        "damage_class": "special",
        "stat_changes": [
            {
                "change": -2,
                "stat": {
                    "name": "SpAtk",
                    "url": "https://pokeapi.co/api/v2/stat/4/"
                }
            }
        ],
        "effect_chance": 100,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage+raise",
                "url": "https://pokeapi.co/api/v2/move-category/7/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 100
        },
        "effect_entries": "Lowers the user's Special Attack by two stages after inflicting damage.",
        "flavor_text_entry": "A storm of sharp leaves is whipped up. The attack\u2019s recoil sharply reduces the user\u2019s Sp. Atk stat."
    },
    "grass-knot": {
        "name": "grass-knot",
        "id": 447,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 20,
        "power": None,
        "type": "grass",
        "damage_class": "special",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Inflicts more damage to heavier targets, with a maximum of 120 power.",
        "flavor_text_entry": "The user snares the foe with grass and trips it. The heavier the foe, the greater the damage."
    },
    "round": {
        "name": "round",
        "id": 496,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 15,
        "power": 60,
        "type": "normal",
        "damage_class": "special",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Has double power if it's used more than once per turn.",
        "flavor_text_entry": "The user attacks the target with a song. Others can join in the Round and make the attack do greater damage."
    },
    "echoed-voice": {
        "name": "echoed-voice",
        "id": 497,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 15,
        "power": 40,
        "type": "normal",
        "damage_class": "special",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Power increases by 100% for each consecutive use by any friendly Pok\u00e9mon, to a maximum of 200.",
        "flavor_text_entry": "The user attacks the target with an echoing voice. If this move is used every turn, it does greater damage."
    },
    "retaliate": {
        "name": "retaliate",
        "id": 514,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 5,
        "power": 70,
        "type": "normal",
        "damage_class": "physical",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Has double power if a friendly Pok\u00e9mon fainted last turn.",
        "flavor_text_entry": "The user gets revenge for a fainted ally. If an ally fainted in the previous turn, this attack\u2019s damage increases."
    },
    "bulldoze": {
        "name": "bulldoze",
        "id": 523,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 20,
        "power": 60,
        "type": "ground",
        "damage_class": "physical",
        "stat_changes": [
            {
                "change": -1,
                "stat": {
                    "name": "Speed",
                    "url": "https://pokeapi.co/api/v2/stat/6/"
                }
            }
        ],
        "effect_chance": 100,
        "target": "all-other-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage+lower",
                "url": "https://pokeapi.co/api/v2/move-category/6/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 100
        },
        "effect_entries": "Has a 100% chance to lower the target's Speed by one stage.",
        "flavor_text_entry": "The user stomps down on the ground and attacks everything in the area. Hit Pok\u00e9mon\u2019s Speed stat is reduced."
    },
    "work-up": {
        "name": "work-up",
        "id": 526,
        "accuracy": None,
        "priority": 0,
        "max_pp": 30,
        "power": None,
        "type": "normal",
        "damage_class": "status",
        "stat_changes": [
            {
                "change": 1,
                "stat": {
                    "name": "Atk",
                    "url": "https://pokeapi.co/api/v2/stat/2/"
                }
            },
            {
                "change": 1,
                "stat": {
                    "name": "SpAtk",
                    "url": "https://pokeapi.co/api/v2/stat/4/"
                }
            }
        ],
        "effect_chance": None,
        "target": "user",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "net-good-stats",
                "url": "https://pokeapi.co/api/v2/move-category/2/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Raises the user's Attack and Special Attack by one stage each.",
        "flavor_text_entry": "The user is roused, and its Attack and Sp. Atk stats increase."
    },
    "wild-charge": {
        "name": "wild-charge",
        "id": 528,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 15,
        "power": 90,
        "type": "electric",
        "damage_class": "physical",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 0,
            "drain": -25,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "User receives 1/4 the damage it inflicts in recoil.",
        "flavor_text_entry": "The user shrouds itself in electricity and smashes into its target. It also damages the user a little."
    },
    "grassy-terrain": {
        "name": "grassy-terrain",
        "id": 580,
        "accuracy": None,
        "priority": 0,
        "max_pp": 10,
        "power": None,
        "type": "grass",
        "damage_class": "status",
        "stat_changes": [],
        "effect_chance": None,
        "target": "entire-field",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "whole-field-effect",
                "url": "https://pokeapi.co/api/v2/move-category/10/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "For five turns, heals all Pok\u00e9mon on the ground for 1/16 max HP each turn and strengthens their grass moves to 1.5\u00d7 their power.",
        "flavor_text_entry": "The user turns the ground under everyone\u2019s feet to grass for five turns. This restores the HP of Pok\u00e9mon on the ground a little every turn."
    },
    "play-rough": {
        "name": "play-rough",
        "id": 583,
        "accuracy": 90,
        "priority": 0,
        "max_pp": 10,
        "power": 90,
        "type": "fairy",
        "damage_class": "physical",
        "stat_changes": [
            {
                "change": -1,
                "stat": {
                    "name": "Atk",
                    "url": "https://pokeapi.co/api/v2/stat/2/"
                }
            }
        ],
        "effect_chance": 10,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage+lower",
                "url": "https://pokeapi.co/api/v2/move-category/6/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 10
        },
        "effect_entries": "Has a 10% chance to lower the target's Attack by one stage.",
        "flavor_text_entry": "The user plays rough with the target and attacks it. This may also lower the target\u2019s Attack stat."
    },
    "confide": {
        "name": "confide",
        "id": 590,
        "accuracy": None,
        "priority": 0,
        "max_pp": 20,
        "power": None,
        "type": "normal",
        "damage_class": "status",
        "stat_changes": [
            {
                "change": -1,
                "stat": {
                    "name": "SpAtk",
                    "url": "https://pokeapi.co/api/v2/stat/4/"
                }
            }
        ],
        "effect_chance": 100,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "net-good-stats",
                "url": "https://pokeapi.co/api/v2/move-category/2/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 100
        },
        "effect_entries": "Lowers the target's Special Attack by one stage.",
        "flavor_text_entry": "The user tells the target a secret, and the target loses its ability to concentrate. This lowers the target\u2019s Sp. Atk stat."
    },
    "grassy-glide": {
        "name": "grassy-glide",
        "id": 803,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 20,
        "power": 55,
        "type": "grass",
        "damage_class": "physical",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Inflicts regular damage with no additional effect.",
        "flavor_text_entry": "Gliding on the ground, the user attacks the target. This move always goes first on Grassy Terrain."
    },
    "tera-blast": {
        "name": "tera-blast",
        "id": 851,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 10,
        "power": 80,
        "type": "normal",
        "damage_class": "special",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": None
    },
    "trailblaze": {
        "name": "trailblaze",
        "id": 885,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 20,
        "power": 50,
        "type": "grass",
        "damage_class": "physical",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": None
    },
    "swords-dance": {
        "name": "swords-dance",
        "id": 14,
        "accuracy": None,
        "priority": 0,
        "max_pp": 20,
        "power": None,
        "type": "normal",
        "damage_class": "status",
        "stat_changes": [
            {
                "change": 2,
                "stat": {
                    "name": "Atk",
                    "url": "https://pokeapi.co/api/v2/stat/2/"
                }
            }
        ],
        "effect_chance": None,
        "target": "user",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "net-good-stats",
                "url": "https://pokeapi.co/api/v2/move-category/2/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Raises the user's Attack by two stages.",
        "flavor_text_entry": "A dance that in\u00ad creases ATTACK."
    },
    "cut": {
        "name": "cut",
        "id": 15,
        "accuracy": 95,
        "priority": 0,
        "max_pp": 30,
        "power": 50,
        "type": "normal",
        "damage_class": "physical",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Inflicts regular damage with no additional effect.",
        "flavor_text_entry": "Cuts using claws, scythes, etc."
    },
    "hyper-beam": {
        "name": "hyper-beam",
        "id": 63,
        "accuracy": 90,
        "priority": 0,
        "max_pp": 5,
        "power": 150,
        "type": "normal",
        "damage_class": "special",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "User foregoes its next turn to recharge.",
        "flavor_text_entry": "1st turn: Attack 2nd turn: Rest"
    },
    "curse": {
        "name": "curse",
        "id": 174,
        "accuracy": None,
        "priority": 0,
        "max_pp": 10,
        "power": None,
        "type": "ghost",
        "damage_class": "status",
        "stat_changes": [],
        "effect_chance": None,
        "target": "specific-move",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "unique",
                "url": "https://pokeapi.co/api/v2/move-category/13/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Ghosts pay half their max HP to hurt the target every turn.  Others decrease Speed but raise Attack and Defense.",
        "flavor_text_entry": "Works differently for ghost-types."
    },
    "megahorn": {
        "name": "megahorn",
        "id": 224,
        "accuracy": 85,
        "priority": 0,
        "max_pp": 10,
        "power": 120,
        "type": "bug",
        "damage_class": "physical",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Inflicts regular damage with no additional effect.",
        "flavor_text_entry": "A powerful charge attack."
    },
    "rock-smash": {
        "name": "rock-smash",
        "id": 249,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 15,
        "power": 40,
        "type": "fighting",
        "damage_class": "physical",
        "stat_changes": [
            {
                "change": -1,
                "stat": {
                    "name": "Def",
                    "url": "https://pokeapi.co/api/v2/stat/3/"
                }
            }
        ],
        "effect_chance": 50,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage+lower",
                "url": "https://pokeapi.co/api/v2/move-category/6/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 50
        },
        "effect_entries": "Has a 50% chance to lower the target's Defense by one stage.",
        "flavor_text_entry": "A rock-crushing attack that may lower DEFENSE."
    },
    "giga-impact": {
        "name": "giga-impact",
        "id": 416,
        "accuracy": 90,
        "priority": 0,
        "max_pp": 5,
        "power": 150,
        "type": "normal",
        "damage_class": "physical",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "User foregoes its next turn to recharge.",
        "flavor_text_entry": "The user charges at the foe using every bit of its power. The user must rest on the next turn."
    },
    "horn-leech": {
        "name": "horn-leech",
        "id": 532,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 10,
        "power": 75,
        "type": "grass",
        "damage_class": "physical",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage+heal",
                "url": "https://pokeapi.co/api/v2/move-category/8/"
            },
            "crit_rate": 0,
            "drain": 50,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Drains half the damage inflicted to heal the user.",
        "flavor_text_entry": "The user drains the target\u2019s energy with its horns. The user\u2019s HP is restored by half the damage taken by the target."
    },
    "petal-blizzard": {
        "name": "petal-blizzard",
        "id": 572,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 15,
        "power": 90,
        "type": "grass",
        "damage_class": "physical",
        "stat_changes": [],
        "effect_chance": None,
        "target": "all-other-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Inflicts regular damage.",
        "flavor_text_entry": "The user stirs up a violent petal blizzard and attacks everything around it."
    },
    "high-horsepower": {
        "name": "high-horsepower",
        "id": 667,
        "accuracy": 95,
        "priority": 0,
        "max_pp": 10,
        "power": 95,
        "type": "ground",
        "damage_class": "physical",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Inflicts regular damage with no additional effect.",
        "flavor_text_entry": "The user fiercely attacks the target using its entire body."
    },
    "throat-chop": {
        "name": "throat-chop",
        "id": 675,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 15,
        "power": 80,
        "type": "dark",
        "damage_class": "physical",
        "stat_changes": [],
        "effect_chance": 100,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "silence",
                "url": "https://pokeapi.co/api/v2/move-ailment/24/"
            },
            "ailment_chance": 100,
            "category": {
                "name": "damage+ailment",
                "url": "https://pokeapi.co/api/v2/move-category/4/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": 2,
            "min_hits": None,
            "min_turns": 2,
            "stat_chance": 0
        },
        "effect_entries": "Prevents the target from using sound-based moves for two turns.",
        "flavor_text_entry": "The user attacks the target\u2019s throat, and the resultant suffering prevents the target from using moves that emit sound for two turns."
    },
    "smart-strike": {
        "name": "smart-strike",
        "id": 684,
        "accuracy": None,
        "priority": 0,
        "max_pp": 10,
        "power": 70,
        "type": "steel",
        "damage_class": "physical",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Never misses.",
        "flavor_text_entry": "The user stabs the target with a sharp horn. This attack never misses."
    },
    "stomping-tantrum": {
        "name": "stomping-tantrum",
        "id": 707,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 10,
        "power": 75,
        "type": "ground",
        "damage_class": "physical",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Has double power if the user's last move failed.",
        "flavor_text_entry": "Driven by frustration, the user attacks the target. If the user\u2019s previous move has failed, the power of this move doubles."
    },
    "thunder-punch": {
        "name": "thunder-punch",
        "id": 9,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 15,
        "power": 75,
        "type": "electric",
        "damage_class": "physical",
        "stat_changes": [],
        "effect_chance": 10,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "paralysis",
                "url": "https://pokeapi.co/api/v2/move-ailment/1/"
            },
            "ailment_chance": 10,
            "category": {
                "name": "damage+ailment",
                "url": "https://pokeapi.co/api/v2/move-category/4/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Has a 10% chance to paralyze the target.",
        "flavor_text_entry": "An electric punch. It may paralyze."
    },
    "tail-whip": {
        "name": "tail-whip",
        "id": 39,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 30,
        "power": None,
        "type": "normal",
        "damage_class": "status",
        "stat_changes": [
            {
                "change": -1,
                "stat": {
                    "name": "Def",
                    "url": "https://pokeapi.co/api/v2/stat/3/"
                }
            }
        ],
        "effect_chance": None,
        "target": "all-opponents",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "net-good-stats",
                "url": "https://pokeapi.co/api/v2/move-category/2/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Lowers the target's Defense by one stage.",
        "flavor_text_entry": "Lowers the foe's DEFENSE."
    },
    "bite": {
        "name": "bite",
        "id": 44,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 25,
        "power": 60,
        "type": "dark",
        "damage_class": "physical",
        "stat_changes": [],
        "effect_chance": 30,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 30,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Has a 30% chance to make the target flinch.",
        "flavor_text_entry": "An attack that may cause flinching."
    },
    "thunder-shock": {
        "name": "thunder-shock",
        "id": 84,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 30,
        "power": 40,
        "type": "electric",
        "damage_class": "special",
        "stat_changes": [],
        "effect_chance": 10,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "paralysis",
                "url": "https://pokeapi.co/api/v2/move-ailment/1/"
            },
            "ailment_chance": 10,
            "category": {
                "name": "damage+ailment",
                "url": "https://pokeapi.co/api/v2/move-category/4/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Has a 10% chance to paralyze the target.",
        "flavor_text_entry": "An attack that may cause paralysis."
    },
    "thunderbolt": {
        "name": "thunderbolt",
        "id": 85,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 15,
        "power": 90,
        "type": "electric",
        "damage_class": "special",
        "stat_changes": [],
        "effect_chance": 10,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "paralysis",
                "url": "https://pokeapi.co/api/v2/move-ailment/1/"
            },
            "ailment_chance": 10,
            "category": {
                "name": "damage+ailment",
                "url": "https://pokeapi.co/api/v2/move-category/4/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Has a 10% chance to paralyze the target.",
        "flavor_text_entry": "An attack that may cause paralysis."
    },
    "thunder": {
        "name": "thunder",
        "id": 87,
        "accuracy": 70,
        "priority": 0,
        "max_pp": 10,
        "power": 110,
        "type": "electric",
        "damage_class": "special",
        "stat_changes": [],
        "effect_chance": 30,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "paralysis",
                "url": "https://pokeapi.co/api/v2/move-ailment/1/"
            },
            "ailment_chance": 30,
            "category": {
                "name": "damage+ailment",
                "url": "https://pokeapi.co/api/v2/move-category/4/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Has a 30% chance to paralyze the target.",
        "flavor_text_entry": "An attack that may cause paralysis."
    },
    "quick-attack": {
        "name": "quick-attack",
        "id": 98,
        "accuracy": 100,
        "priority": 1,
        "max_pp": 30,
        "power": 40,
        "type": "normal",
        "damage_class": "physical",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Inflicts regular damage with no additional effect.",
        "flavor_text_entry": "Lets the user get in the first hit."
    },
    "defense-curl": {
        "name": "defense-curl",
        "id": 111,
        "accuracy": None,
        "priority": 0,
        "max_pp": 40,
        "power": None,
        "type": "normal",
        "damage_class": "status",
        "stat_changes": [
            {
                "change": 1,
                "stat": {
                    "name": "Def",
                    "url": "https://pokeapi.co/api/v2/stat/3/"
                }
            }
        ],
        "effect_chance": None,
        "target": "user",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "net-good-stats",
                "url": "https://pokeapi.co/api/v2/move-category/2/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Raises user's Defense by one stage.",
        "flavor_text_entry": "Heightens the user's DEFENSE."
    },
    "bide": {
        "name": "bide",
        "id": 117,
        "accuracy": None,
        "priority": 1,
        "max_pp": 10,
        "power": None,
        "type": "normal",
        "damage_class": "physical",
        "stat_changes": [],
        "effect_chance": None,
        "target": "user",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "User waits for two turns, then hits back for twice the damage it took.",
        "flavor_text_entry": "Waits 2-3 turns & hits back double."
    },
    "swift": {
        "name": "swift",
        "id": 129,
        "accuracy": None,
        "priority": 0,
        "max_pp": 20,
        "power": 60,
        "type": "normal",
        "damage_class": "special",
        "stat_changes": [],
        "effect_chance": None,
        "target": "all-opponents",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Never misses.",
        "flavor_text_entry": "An attack that never misses."
    },
    "hyper-fang": {
        "name": "hyper-fang",
        "id": 158,
        "accuracy": 90,
        "priority": 0,
        "max_pp": 15,
        "power": 80,
        "type": "normal",
        "damage_class": "physical",
        "stat_changes": [],
        "effect_chance": 10,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 10,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Has a 10% chance to make the target flinch.",
        "flavor_text_entry": "An attack that may cause flinching."
    },
    "super-fang": {
        "name": "super-fang",
        "id": 162,
        "accuracy": 90,
        "priority": 0,
        "max_pp": 10,
        "power": None,
        "type": "normal",
        "damage_class": "physical",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Inflicts damage equal to half the target's HP.",
        "flavor_text_entry": "Cuts the foe's HP by 1/2."
    },
    "thief": {
        "name": "thief",
        "id": 168,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 25,
        "power": 60,
        "type": "dark",
        "damage_class": "physical",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Takes the target's item.",
        "flavor_text_entry": "An attack that may steal a held item."
    },
    "flail": {
        "name": "flail",
        "id": 175,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 15,
        "power": None,
        "type": "normal",
        "damage_class": "physical",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Inflicts more damage when the user has less HP remaining, with a maximum of 200 power.",
        "flavor_text_entry": "Stronger if the user's HP is low."
    },
    "sweet-kiss": {
        "name": "sweet-kiss",
        "id": 186,
        "accuracy": 75,
        "priority": 0,
        "max_pp": 10,
        "power": None,
        "type": "fairy",
        "damage_class": "status",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "confusion",
                "url": "https://pokeapi.co/api/v2/move-ailment/6/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "ailment",
                "url": "https://pokeapi.co/api/v2/move-category/1/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": 5,
            "min_hits": None,
            "min_turns": 2,
            "stat_chance": 0
        },
        "effect_entries": "Confuses the target.",
        "flavor_text_entry": "A move that causes confusion."
    },
    "mud-slap": {
        "name": "mud-slap",
        "id": 189,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 10,
        "power": 20,
        "type": "ground",
        "damage_class": "special",
        "stat_changes": [
            {
                "change": -1,
                "stat": {
                    "name": "accuracy",
                    "url": "https://pokeapi.co/api/v2/stat/7/"
                }
            }
        ],
        "effect_chance": 100,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage+lower",
                "url": "https://pokeapi.co/api/v2/move-category/6/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 100
        },
        "effect_entries": "Has a 100% chance to lower the target's accuracy by one stage.",
        "flavor_text_entry": "Reduces the foe's accuracy."
    },
    "rollout": {
        "name": "rollout",
        "id": 205,
        "accuracy": 90,
        "priority": 0,
        "max_pp": 20,
        "power": 30,
        "type": "rock",
        "damage_class": "physical",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Power doubles every turn this move is used in succession after the first, resetting after five turns.",
        "flavor_text_entry": "Attacks 5 turns with rising power."
    },
    "spark": {
        "name": "spark",
        "id": 209,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 20,
        "power": 65,
        "type": "electric",
        "damage_class": "physical",
        "stat_changes": [],
        "effect_chance": 30,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "paralysis",
                "url": "https://pokeapi.co/api/v2/move-ailment/1/"
            },
            "ailment_chance": 30,
            "category": {
                "name": "damage+ailment",
                "url": "https://pokeapi.co/api/v2/move-category/4/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Has a 30% chance to paralyze the target.",
        "flavor_text_entry": "An attack that may cause paralysis."
    },
    "encore": {
        "name": "encore",
        "id": 227,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 5,
        "power": None,
        "type": "normal",
        "damage_class": "status",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "unique",
                "url": "https://pokeapi.co/api/v2/move-category/13/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Forces the target to repeat its last used move every turn for 2 to 6 turns.",
        "flavor_text_entry": "Makes the foe re\u00ad peat 2-6 times."
    },
    "iron-tail": {
        "name": "iron-tail",
        "id": 231,
        "accuracy": 75,
        "priority": 0,
        "max_pp": 15,
        "power": 100,
        "type": "steel",
        "damage_class": "physical",
        "stat_changes": [
            {
                "change": -1,
                "stat": {
                    "name": "Def",
                    "url": "https://pokeapi.co/api/v2/stat/3/"
                }
            }
        ],
        "effect_chance": 30,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage+lower",
                "url": "https://pokeapi.co/api/v2/move-category/6/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 30
        },
        "effect_entries": "Has a 30% chance to lower the target's Defense by one stage.",
        "flavor_text_entry": "An attack that may reduce DEFENSE."
    },
    "uproar": {
        "name": "uproar",
        "id": 253,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 10,
        "power": 90,
        "type": "normal",
        "damage_class": "special",
        "stat_changes": [],
        "effect_chance": None,
        "target": "random-opponent",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": 3,
            "min_hits": None,
            "min_turns": 3,
            "stat_chance": 0
        },
        "effect_entries": "Forced to use this move for several turns.  Pok\u00e9mon cannot fall asleep in that time.",
        "flavor_text_entry": "Causes an uproar for 2 to 5 turns and prevents sleep."
    },
    "flatter": {
        "name": "flatter",
        "id": 260,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 15,
        "power": None,
        "type": "dark",
        "damage_class": "status",
        "stat_changes": [
            {
                "change": 1,
                "stat": {
                    "name": "SpAtk",
                    "url": "https://pokeapi.co/api/v2/stat/4/"
                }
            }
        ],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "confusion",
                "url": "https://pokeapi.co/api/v2/move-ailment/6/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "swagger",
                "url": "https://pokeapi.co/api/v2/move-category/5/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": 5,
            "min_hits": None,
            "min_turns": 2,
            "stat_chance": 0
        },
        "effect_entries": "Raises the target's Special Attack by one stage and confuses the target.",
        "flavor_text_entry": "Confuses the foe, but raises its SP. ATK."
    },
    "follow-me": {
        "name": "follow-me",
        "id": 266,
        "accuracy": None,
        "priority": 2,
        "max_pp": 20,
        "power": None,
        "type": "normal",
        "damage_class": "status",
        "stat_changes": [],
        "effect_chance": None,
        "target": "user",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "unique",
                "url": "https://pokeapi.co/api/v2/move-category/13/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Redirects the target's single-target effects to the user for this turn.",
        "flavor_text_entry": "Draws attention to make foes attack only the user."
    },
    "charge": {
        "name": "charge",
        "id": 268,
        "accuracy": None,
        "priority": 0,
        "max_pp": 20,
        "power": None,
        "type": "electric",
        "damage_class": "status",
        "stat_changes": [
            {
                "change": 1,
                "stat": {
                    "name": "SpDef",
                    "url": "https://pokeapi.co/api/v2/stat/5/"
                }
            }
        ],
        "effect_chance": None,
        "target": "user",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "net-good-stats",
                "url": "https://pokeapi.co/api/v2/move-category/2/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Raises the user's Special Defense by one stage.  User's Electric moves have doubled power next turn.",
        "flavor_text_entry": "Charges power to boost the electric move used next."
    },
    "aerial-ace": {
        "name": "aerial-ace",
        "id": 332,
        "accuracy": None,
        "priority": 0,
        "max_pp": 20,
        "power": 60,
        "type": "flying",
        "damage_class": "physical",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Never misses.",
        "flavor_text_entry": "An extremely speedy and unavoidable attack."
    },
    "mud-shot": {
        "name": "mud-shot",
        "id": 341,
        "accuracy": 95,
        "priority": 0,
        "max_pp": 15,
        "power": 55,
        "type": "ground",
        "damage_class": "special",
        "stat_changes": [
            {
                "change": -1,
                "stat": {
                    "name": "Speed",
                    "url": "https://pokeapi.co/api/v2/stat/6/"
                }
            }
        ],
        "effect_chance": 100,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage+lower",
                "url": "https://pokeapi.co/api/v2/move-category/6/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 100
        },
        "effect_entries": "Has a 100% chance to lower the target's Speed by one stage.",
        "flavor_text_entry": "Hurls mud at the foe and reduces SPEED."
    },
    "covet": {
        "name": "covet",
        "id": 343,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 25,
        "power": 60,
        "type": "normal",
        "damage_class": "physical",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Takes the target's item.",
        "flavor_text_entry": "Cutely begs to obtain an item held by the foe."
    },
    "shock-wave": {
        "name": "shock-wave",
        "id": 351,
        "accuracy": None,
        "priority": 0,
        "max_pp": 20,
        "power": 60,
        "type": "electric",
        "damage_class": "special",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Never misses.",
        "flavor_text_entry": "A fast and unavoidable electric attack."
    },
    "u-turn": {
        "name": "u-turn",
        "id": 369,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 20,
        "power": 70,
        "type": "bug",
        "damage_class": "physical",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "User must switch out after attacking.",
        "flavor_text_entry": "After making its attack, the user rushes back to switch places with a party Pok\u00e9mon in waiting."
    },
    "fling": {
        "name": "fling",
        "id": 374,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 10,
        "power": None,
        "type": "dark",
        "damage_class": "physical",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Throws held item at the target; power depends on the item.",
        "flavor_text_entry": "The user flings its held item at the foe to attack. Its power and effects depend on the item."
    },
    "magnet-rise": {
        "name": "magnet-rise",
        "id": 393,
        "accuracy": None,
        "priority": 0,
        "max_pp": 10,
        "power": None,
        "type": "electric",
        "damage_class": "status",
        "stat_changes": [],
        "effect_chance": None,
        "target": "user",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "unique",
                "url": "https://pokeapi.co/api/v2/move-category/13/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "User is immune to Ground moves and effects for five turns.",
        "flavor_text_entry": "The user levitates using electrically generated magnetism for five turns. "
    },
    "thunder-fang": {
        "name": "thunder-fang",
        "id": 422,
        "accuracy": 95,
        "priority": 0,
        "max_pp": 15,
        "power": 65,
        "type": "electric",
        "damage_class": "physical",
        "stat_changes": [],
        "effect_chance": 10,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "paralysis",
                "url": "https://pokeapi.co/api/v2/move-ailment/1/"
            },
            "ailment_chance": 10,
            "category": {
                "name": "damage+ailment",
                "url": "https://pokeapi.co/api/v2/move-category/4/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 10,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Has a 10% chance to paralyze the target and a 10% chance to make the target flinch.",
        "flavor_text_entry": "The user bites with electrified fangs. It may also make the foe flinch or become paralyzed."
    },
    "discharge": {
        "name": "discharge",
        "id": 435,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 15,
        "power": 80,
        "type": "electric",
        "damage_class": "special",
        "stat_changes": [],
        "effect_chance": 30,
        "target": "all-other-pokemon",
        "meta": {
            "ailment": {
                "name": "paralysis",
                "url": "https://pokeapi.co/api/v2/move-ailment/1/"
            },
            "ailment_chance": 30,
            "category": {
                "name": "damage+ailment",
                "url": "https://pokeapi.co/api/v2/move-category/4/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Has a 30% chance to paralyze the target.",
        "flavor_text_entry": "A flare of electricity is loosed to strike all Pok\u00e9mon in battle. It may also cause paralysis."
    },
    "gunk-shot": {
        "name": "gunk-shot",
        "id": 441,
        "accuracy": 80,
        "priority": 0,
        "max_pp": 5,
        "power": 120,
        "type": "poison",
        "damage_class": "physical",
        "stat_changes": [],
        "effect_chance": 30,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "poison",
                "url": "https://pokeapi.co/api/v2/move-ailment/5/"
            },
            "ailment_chance": 30,
            "category": {
                "name": "damage+ailment",
                "url": "https://pokeapi.co/api/v2/move-category/4/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Has a 30% chance to poison the target.",
        "flavor_text_entry": "The user shoots filthy garbage at the foe to attack. It may also poison the target."
    },
    "captivate": {
        "name": "captivate",
        "id": 445,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 20,
        "power": None,
        "type": "normal",
        "damage_class": "status",
        "stat_changes": [
            {
                "change": -2,
                "stat": {
                    "name": "SpAtk",
                    "url": "https://pokeapi.co/api/v2/stat/4/"
                }
            }
        ],
        "effect_chance": None,
        "target": "all-opponents",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "net-good-stats",
                "url": "https://pokeapi.co/api/v2/move-category/2/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Lowers the target's Special Attack by two stages if it's the opposite gender.",
        "flavor_text_entry": "If it is the opposite gender of the user, the foe is charmed into sharply lowering its Sp. Atk stat."
    },
    "charge-beam": {
        "name": "charge-beam",
        "id": 451,
        "accuracy": 90,
        "priority": 0,
        "max_pp": 10,
        "power": 50,
        "type": "electric",
        "damage_class": "special",
        "stat_changes": [
            {
                "change": 1,
                "stat": {
                    "name": "SpAtk",
                    "url": "https://pokeapi.co/api/v2/stat/4/"
                }
            }
        ],
        "effect_chance": 70,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage+raise",
                "url": "https://pokeapi.co/api/v2/move-category/7/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 70
        },
        "effect_entries": "Has a 70% chance to raise the user's Special Attack by one stage.",
        "flavor_text_entry": "The user fires a concentrated bundle of electricity. It may also raise the user\u2019s Sp. Atk stat."
    },
    "electro-ball": {
        "name": "electro-ball",
        "id": 486,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 10,
        "power": None,
        "type": "electric",
        "damage_class": "special",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Power is higher when the user has greater Speed than the target, up to a maximum of 150.",
        "flavor_text_entry": "The user hurls an electric orb at the target. The faster the user is than the target, the greater the damage."
    },
    "bestow": {
        "name": "bestow",
        "id": 516,
        "accuracy": None,
        "priority": 0,
        "max_pp": 15,
        "power": None,
        "type": "normal",
        "damage_class": "status",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "unique",
                "url": "https://pokeapi.co/api/v2/move-category/13/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Gives the user's held item to the target.",
        "flavor_text_entry": "The user passes its held item to the target when the target isn\u2019t holding an item."
    },
    "volt-switch": {
        "name": "volt-switch",
        "id": 521,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 20,
        "power": 70,
        "type": "electric",
        "damage_class": "special",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "User must switch out after attacking.",
        "flavor_text_entry": "After making its attack, the user rushes back to switch places with a party Pok\u00e9mon in waiting."
    },
    "electroweb": {
        "name": "electroweb",
        "id": 527,
        "accuracy": 95,
        "priority": 0,
        "max_pp": 15,
        "power": 55,
        "type": "electric",
        "damage_class": "special",
        "stat_changes": [
            {
                "change": -1,
                "stat": {
                    "name": "Speed",
                    "url": "https://pokeapi.co/api/v2/stat/6/"
                }
            }
        ],
        "effect_chance": 100,
        "target": "all-opponents",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage+lower",
                "url": "https://pokeapi.co/api/v2/move-category/6/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 100
        },
        "effect_entries": "Lowers the target's Speed by one stage.",
        "flavor_text_entry": "The user captures and attacks opposing Pok\u00e9mon by using an electric net. It reduces the targets\u2019 Speed stat."
    },
    "ion-deluge": {
        "name": "ion-deluge",
        "id": 569,
        "accuracy": None,
        "priority": 1,
        "max_pp": 25,
        "power": None,
        "type": "electric",
        "damage_class": "status",
        "stat_changes": [],
        "effect_chance": None,
        "target": "entire-field",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "whole-field-effect",
                "url": "https://pokeapi.co/api/v2/move-category/10/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Changes all normal moves to electric moves for the rest of the turn.",
        "flavor_text_entry": "The user disperses electrically charged particles, which changes Normal-type moves to Electric-type moves."
    },
    "eerie-impulse": {
        "name": "eerie-impulse",
        "id": 598,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 15,
        "power": None,
        "type": "electric",
        "damage_class": "status",
        "stat_changes": [
            {
                "change": -2,
                "stat": {
                    "name": "SpAtk",
                    "url": "https://pokeapi.co/api/v2/stat/4/"
                }
            }
        ],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "net-good-stats",
                "url": "https://pokeapi.co/api/v2/move-category/2/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Lowers the target's Special Attack by two stages.",
        "flavor_text_entry": "The user\u2019s body generates an eerie impulse. Exposing the target to it harshly lowers the target\u2019s Sp. Atk stat."
    },
    "electric-terrain": {
        "name": "electric-terrain",
        "id": 604,
        "accuracy": None,
        "priority": 0,
        "max_pp": 10,
        "power": None,
        "type": "electric",
        "damage_class": "status",
        "stat_changes": [],
        "effect_chance": None,
        "target": "entire-field",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "whole-field-effect",
                "url": "https://pokeapi.co/api/v2/move-category/10/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "For five turns, prevents all Pok\u00e9mon on the ground from sleeping and strengthens their electric moves to 1.5\u00d7 their power.",
        "flavor_text_entry": "The user electrifies the ground under everyone\u2019s feet for five turns. Pok\u00e9mon on the ground no longer fall asleep."
    },
    "baby-doll-eyes": {
        "name": "baby-doll-eyes",
        "id": 608,
        "accuracy": 100,
        "priority": 1,
        "max_pp": 30,
        "power": None,
        "type": "fairy",
        "damage_class": "status",
        "stat_changes": [
            {
                "change": -1,
                "stat": {
                    "name": "Atk",
                    "url": "https://pokeapi.co/api/v2/stat/2/"
                }
            }
        ],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "net-good-stats",
                "url": "https://pokeapi.co/api/v2/move-category/2/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Lowers the target's Attack by one stage.",
        "flavor_text_entry": "The user stares at the target with its baby-doll eyes, which lowers its Attack stat. This move always goes first."
    },
    "nuzzle": {
        "name": "nuzzle",
        "id": 609,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 20,
        "power": 20,
        "type": "electric",
        "damage_class": "physical",
        "stat_changes": [],
        "effect_chance": 100,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "paralysis",
                "url": "https://pokeapi.co/api/v2/move-ailment/1/"
            },
            "ailment_chance": 100,
            "category": {
                "name": "damage+ailment",
                "url": "https://pokeapi.co/api/v2/move-category/4/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Has a 100% chance to paralyze the target.",
        "flavor_text_entry": "The user attacks by nuzzling its electrified cheeks against the target. This also leaves the target with paralysis."
    },
    "laser-focus": {
        "name": "laser-focus",
        "id": 673,
        "accuracy": None,
        "priority": 0,
        "max_pp": 30,
        "power": None,
        "type": "normal",
        "damage_class": "status",
        "stat_changes": [],
        "effect_chance": None,
        "target": "user",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "unique",
                "url": "https://pokeapi.co/api/v2/move-category/13/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Guarantees a critical hit with the user's next move.",
        "flavor_text_entry": "The user concentrates intensely. The attack on the next turn always results in a critical hit."
    },
    "alluring-voice": {
        "name": "alluring-voice",
        "id": 914,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 10,
        "power": 80,
        "type": "fairy",
        "damage_class": "special",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": None
    },
    "mega-punch": {
        "name": "mega-punch",
        "id": 5,
        "accuracy": 85,
        "priority": 0,
        "max_pp": 20,
        "power": 80,
        "type": "normal",
        "damage_class": "physical",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Inflicts regular damage with no additional effect.",
        "flavor_text_entry": "A powerful punch thrown very hard."
    },
    "fire-punch": {
        "name": "fire-punch",
        "id": 7,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 15,
        "power": 75,
        "type": "fire",
        "damage_class": "physical",
        "stat_changes": [],
        "effect_chance": 10,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "burn",
                "url": "https://pokeapi.co/api/v2/move-ailment/4/"
            },
            "ailment_chance": 10,
            "category": {
                "name": "damage+ailment",
                "url": "https://pokeapi.co/api/v2/move-category/4/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Has a 10% chance to burn the target.",
        "flavor_text_entry": "A fiery punch. May cause a burn."
    },
    "ice-punch": {
        "name": "ice-punch",
        "id": 8,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 15,
        "power": 75,
        "type": "ice",
        "damage_class": "physical",
        "stat_changes": [],
        "effect_chance": 10,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "freeze",
                "url": "https://pokeapi.co/api/v2/move-ailment/3/"
            },
            "ailment_chance": 10,
            "category": {
                "name": "damage+ailment",
                "url": "https://pokeapi.co/api/v2/move-category/4/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Has a 10% chance to freeze the target.",
        "flavor_text_entry": "An icy punch. May cause freezing."
    },
    "scratch": {
        "name": "scratch",
        "id": 10,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 35,
        "power": 40,
        "type": "normal",
        "damage_class": "physical",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Inflicts regular damage with no additional effect.",
        "flavor_text_entry": "Scratches with sharp claws."
    },
    "mega-kick": {
        "name": "mega-kick",
        "id": 25,
        "accuracy": 75,
        "priority": 0,
        "max_pp": 5,
        "power": 120,
        "type": "normal",
        "damage_class": "physical",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Inflicts regular damage with no additional effect.",
        "flavor_text_entry": "A powerful kicking attack."
    },
    "thrash": {
        "name": "thrash",
        "id": 37,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 10,
        "power": 120,
        "type": "normal",
        "damage_class": "physical",
        "stat_changes": [],
        "effect_chance": None,
        "target": "random-opponent",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Hits every turn for 2-3 turns, then confuses the user.",
        "flavor_text_entry": "Works 2-3 turns and confuses user."
    },
    "leer": {
        "name": "leer",
        "id": 43,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 30,
        "power": None,
        "type": "normal",
        "damage_class": "status",
        "stat_changes": [
            {
                "change": -1,
                "stat": {
                    "name": "Def",
                    "url": "https://pokeapi.co/api/v2/stat/3/"
                }
            }
        ],
        "effect_chance": 100,
        "target": "all-opponents",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "net-good-stats",
                "url": "https://pokeapi.co/api/v2/move-category/2/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 100
        },
        "effect_entries": "Lowers the target's Defense by one stage.",
        "flavor_text_entry": "Reduces the foe's DEFENSE."
    },
    "roar": {
        "name": "roar",
        "id": 46,
        "accuracy": None,
        "priority": -6,
        "max_pp": 20,
        "power": None,
        "type": "normal",
        "damage_class": "status",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "force-switch",
                "url": "https://pokeapi.co/api/v2/move-category/12/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Immediately ends wild battles.  Forces trainers to switch Pok\u00e9mon.",
        "flavor_text_entry": "Scares wild foes to end battle."
    },
    "low-kick": {
        "name": "low-kick",
        "id": 67,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 20,
        "power": None,
        "type": "fighting",
        "damage_class": "physical",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Inflicts more damage to heavier targets, with a maximum of 120 power.",
        "flavor_text_entry": "An attack that may cause flinching."
    },
    "counter": {
        "name": "counter",
        "id": 68,
        "accuracy": 100,
        "priority": -5,
        "max_pp": 20,
        "power": None,
        "type": "fighting",
        "damage_class": "physical",
        "stat_changes": [],
        "effect_chance": None,
        "target": "specific-move",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Inflicts twice the damage the user received from the last physical hit it took.",
        "flavor_text_entry": "Returns a physical blow double."
    },
    "seismic-toss": {
        "name": "seismic-toss",
        "id": 69,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 20,
        "power": None,
        "type": "fighting",
        "damage_class": "physical",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Inflicts damage equal to the user's level.",
        "flavor_text_entry": "Inflicts damage identical to the user\u2019s level."
    },
    "strength": {
        "name": "strength",
        "id": 70,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 15,
        "power": 80,
        "type": "normal",
        "damage_class": "physical",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Inflicts regular damage with no additional effect.",
        "flavor_text_entry": "A powerful physi\u00ad cal attack."
    },
    "earthquake": {
        "name": "earthquake",
        "id": 89,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 10,
        "power": 100,
        "type": "ground",
        "damage_class": "physical",
        "stat_changes": [],
        "effect_chance": None,
        "target": "all-other-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Inflicts regular damage and can hit Dig users.",
        "flavor_text_entry": "Tough but useless vs. flying foes."
    },
    "mimic": {
        "name": "mimic",
        "id": 102,
        "accuracy": None,
        "priority": 0,
        "max_pp": 10,
        "power": None,
        "type": "normal",
        "damage_class": "status",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "unique",
                "url": "https://pokeapi.co/api/v2/move-category/13/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Copies the target's last used move.",
        "flavor_text_entry": "Copies a move used by the foe."
    },
    "focus-energy": {
        "name": "focus-energy",
        "id": 116,
        "accuracy": None,
        "priority": 0,
        "max_pp": 30,
        "power": None,
        "type": "normal",
        "damage_class": "status",
        "stat_changes": [],
        "effect_chance": None,
        "target": "user",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "unique",
                "url": "https://pokeapi.co/api/v2/move-category/13/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Increases the user's chance to score a critical hit.",
        "flavor_text_entry": "Raises the criti\u00ad cal hit ratio."
    },
    "metronome": {
        "name": "metronome",
        "id": 118,
        "accuracy": None,
        "priority": 0,
        "max_pp": 10,
        "power": None,
        "type": "normal",
        "damage_class": "status",
        "stat_changes": [],
        "effect_chance": None,
        "target": "user",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "unique",
                "url": "https://pokeapi.co/api/v2/move-category/13/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Randomly selects and uses any move in the game.",
        "flavor_text_entry": "Randomly uses any POK\u00e9MON move."
    },
    "lick": {
        "name": "lick",
        "id": 122,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 30,
        "power": 30,
        "type": "ghost",
        "damage_class": "physical",
        "stat_changes": [],
        "effect_chance": 30,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "paralysis",
                "url": "https://pokeapi.co/api/v2/move-ailment/1/"
            },
            "ailment_chance": 30,
            "category": {
                "name": "damage+ailment",
                "url": "https://pokeapi.co/api/v2/move-category/4/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Has a 30% chance to paralyze the target.",
        "flavor_text_entry": "An attack that may cause paralysis."
    },
    "fury-swipes": {
        "name": "fury-swipes",
        "id": 154,
        "accuracy": 80,
        "priority": 0,
        "max_pp": 15,
        "power": 18,
        "type": "normal",
        "damage_class": "physical",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": 5,
            "max_turns": None,
            "min_hits": 2,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Hits 2-5 times in one turn.",
        "flavor_text_entry": "Quickly scratches 2-5 times."
    },
    "rock-slide": {
        "name": "rock-slide",
        "id": 157,
        "accuracy": 90,
        "priority": 0,
        "max_pp": 10,
        "power": 75,
        "type": "rock",
        "damage_class": "physical",
        "stat_changes": [],
        "effect_chance": 30,
        "target": "all-opponents",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 30,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Has a 30% chance to make the target flinch.",
        "flavor_text_entry": "An attack that may cause flinching."
    },
    "slash": {
        "name": "slash",
        "id": 163,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 20,
        "power": 70,
        "type": "normal",
        "damage_class": "physical",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 1,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Has an increased chance for a critical hit.",
        "flavor_text_entry": "Has a high criti\u00ad cal hit ratio."
    },
    "belly-drum": {
        "name": "belly-drum",
        "id": 187,
        "accuracy": None,
        "priority": 0,
        "max_pp": 10,
        "power": None,
        "type": "normal",
        "damage_class": "status",
        "stat_changes": [],
        "effect_chance": None,
        "target": "user",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "unique",
                "url": "https://pokeapi.co/api/v2/move-category/13/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "User pays half its max HP to max out its Attack.",
        "flavor_text_entry": "Reduces own HP to maximize ATTACK."
    },
    "zap-cannon": {
        "name": "zap-cannon",
        "id": 192,
        "accuracy": 50,
        "priority": 0,
        "max_pp": 5,
        "power": 120,
        "type": "electric",
        "damage_class": "special",
        "stat_changes": [],
        "effect_chance": 100,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "paralysis",
                "url": "https://pokeapi.co/api/v2/move-ailment/1/"
            },
            "ailment_chance": 100,
            "category": {
                "name": "damage+ailment",
                "url": "https://pokeapi.co/api/v2/move-category/4/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Has a 100% chance to paralyze the target.",
        "flavor_text_entry": "An attack that always paralyzes."
    },
    "fury-cutter": {
        "name": "fury-cutter",
        "id": 210,
        "accuracy": 95,
        "priority": 0,
        "max_pp": 20,
        "power": 40,
        "type": "bug",
        "damage_class": "physical",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Power doubles every turn this move is used in succession after the first, maxing out after five turns.",
        "flavor_text_entry": "An attack that intensifies on each successive hit."
    },
    "dynamic-punch": {
        "name": "dynamic-punch",
        "id": 223,
        "accuracy": 50,
        "priority": 0,
        "max_pp": 5,
        "power": 100,
        "type": "fighting",
        "damage_class": "physical",
        "stat_changes": [],
        "effect_chance": 100,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "confusion",
                "url": "https://pokeapi.co/api/v2/move-ailment/6/"
            },
            "ailment_chance": 100,
            "category": {
                "name": "damage+ailment",
                "url": "https://pokeapi.co/api/v2/move-category/4/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": 5,
            "min_hits": None,
            "min_turns": 2,
            "stat_chance": 0
        },
        "effect_entries": "Has a 100% chance to confuse the target.",
        "flavor_text_entry": "An attack that always confuses."
    },
    "sweet-scent": {
        "name": "sweet-scent",
        "id": 230,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 20,
        "power": None,
        "type": "normal",
        "damage_class": "status",
        "stat_changes": [
            {
                "change": -2,
                "stat": {
                    "name": "evasion",
                    "url": "https://pokeapi.co/api/v2/stat/8/"
                }
            }
        ],
        "effect_chance": None,
        "target": "all-opponents",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "net-good-stats",
                "url": "https://pokeapi.co/api/v2/move-category/2/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Lowers the target's evasion by one stage.",
        "flavor_text_entry": "Reduces the foe's evasiveness."
    },
    "metal-claw": {
        "name": "metal-claw",
        "id": 232,
        "accuracy": 95,
        "priority": 0,
        "max_pp": 35,
        "power": 50,
        "type": "steel",
        "damage_class": "physical",
        "stat_changes": [
            {
                "change": 1,
                "stat": {
                    "name": "Atk",
                    "url": "https://pokeapi.co/api/v2/stat/2/"
                }
            }
        ],
        "effect_chance": 10,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage+raise",
                "url": "https://pokeapi.co/api/v2/move-category/7/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 10
        },
        "effect_entries": "Has a 10% chance to raise the user's Attack by one stage.",
        "flavor_text_entry": "An attack that may up user's ATTACK."
    },
    "cross-chop": {
        "name": "cross-chop",
        "id": 238,
        "accuracy": 80,
        "priority": 0,
        "max_pp": 5,
        "power": 100,
        "type": "fighting",
        "damage_class": "physical",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 1,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Has an increased chance for a critical hit.",
        "flavor_text_entry": "Has a high criti\u00ad cal hit ratio."
    },
    "crunch": {
        "name": "crunch",
        "id": 242,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 15,
        "power": 80,
        "type": "dark",
        "damage_class": "physical",
        "stat_changes": [
            {
                "change": -1,
                "stat": {
                    "name": "Def",
                    "url": "https://pokeapi.co/api/v2/stat/3/"
                }
            }
        ],
        "effect_chance": 20,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage+lower",
                "url": "https://pokeapi.co/api/v2/move-category/6/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 20
        },
        "effect_entries": "Has a 20% chance to lower the target's Defense by one stage.",
        "flavor_text_entry": "An attack that may lower SPCL.DEF."
    },
    "torment": {
        "name": "torment",
        "id": 259,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 15,
        "power": None,
        "type": "dark",
        "damage_class": "status",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "torment",
                "url": "https://pokeapi.co/api/v2/move-ailment/12/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "ailment",
                "url": "https://pokeapi.co/api/v2/move-category/1/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Prevents the target from using the same move twice in a row.",
        "flavor_text_entry": "Torments the foe and stops successive use of a move."
    },
    "focus-punch": {
        "name": "focus-punch",
        "id": 264,
        "accuracy": 100,
        "priority": -3,
        "max_pp": 20,
        "power": 150,
        "type": "fighting",
        "damage_class": "physical",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "If the user takes damage before attacking, the attack is canceled.",
        "flavor_text_entry": "A powerful loyalty attack. The user flinches if hit."
    },
    "taunt": {
        "name": "taunt",
        "id": 269,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 20,
        "power": None,
        "type": "dark",
        "damage_class": "status",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "unique",
                "url": "https://pokeapi.co/api/v2/move-category/13/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "For the next few turns, the target can only use damaging moves.",
        "flavor_text_entry": "Taunts the foe into only using attack moves."
    },
    "superpower": {
        "name": "superpower",
        "id": 276,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 5,
        "power": 120,
        "type": "fighting",
        "damage_class": "physical",
        "stat_changes": [
            {
                "change": -1,
                "stat": {
                    "name": "Atk",
                    "url": "https://pokeapi.co/api/v2/stat/2/"
                }
            },
            {
                "change": -1,
                "stat": {
                    "name": "Def",
                    "url": "https://pokeapi.co/api/v2/stat/3/"
                }
            }
        ],
        "effect_chance": 100,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage+raise",
                "url": "https://pokeapi.co/api/v2/move-category/7/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 100
        },
        "effect_entries": "Lowers the user's Attack and Defense by one stage after inflicting damage.",
        "flavor_text_entry": "Boosts strength sharply, but lowers abilities."
    },
    "brick-break": {
        "name": "brick-break",
        "id": 280,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 15,
        "power": 75,
        "type": "fighting",
        "damage_class": "physical",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Destroys Reflect and Light Screen.",
        "flavor_text_entry": "Destroys barriers such as REFLECT and causes damage."
    },
    "yawn": {
        "name": "yawn",
        "id": 281,
        "accuracy": None,
        "priority": 0,
        "max_pp": 10,
        "power": None,
        "type": "normal",
        "damage_class": "status",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "yawn",
                "url": "https://pokeapi.co/api/v2/move-ailment/14/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "ailment",
                "url": "https://pokeapi.co/api/v2/move-category/1/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": 2,
            "min_hits": None,
            "min_turns": 2,
            "stat_chance": 0
        },
        "effect_entries": "Target sleeps at the end of the next turn.",
        "flavor_text_entry": "Lulls the foe into yawning, then sleeping next turn."
    },
    "hyper-voice": {
        "name": "hyper-voice",
        "id": 304,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 10,
        "power": 90,
        "type": "normal",
        "damage_class": "special",
        "stat_changes": [],
        "effect_chance": None,
        "target": "all-opponents",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Inflicts regular damage with no additional effect.",
        "flavor_text_entry": "A loud attack that uses sound waves to injure."
    },
    "rock-tomb": {
        "name": "rock-tomb",
        "id": 317,
        "accuracy": 95,
        "priority": 0,
        "max_pp": 15,
        "power": 60,
        "type": "rock",
        "damage_class": "physical",
        "stat_changes": [
            {
                "change": -1,
                "stat": {
                    "name": "Speed",
                    "url": "https://pokeapi.co/api/v2/stat/6/"
                }
            }
        ],
        "effect_chance": 100,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage+lower",
                "url": "https://pokeapi.co/api/v2/move-category/6/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 100
        },
        "effect_entries": "Has a 100% chance to lower the target's Speed by one stage.",
        "flavor_text_entry": "Stops the foe from moving with rocks and cuts SPEED."
    },
    "bulk-up": {
        "name": "bulk-up",
        "id": 339,
        "accuracy": None,
        "priority": 0,
        "max_pp": 20,
        "power": None,
        "type": "fighting",
        "damage_class": "status",
        "stat_changes": [
            {
                "change": 1,
                "stat": {
                    "name": "Atk",
                    "url": "https://pokeapi.co/api/v2/stat/2/"
                }
            },
            {
                "change": 1,
                "stat": {
                    "name": "Def",
                    "url": "https://pokeapi.co/api/v2/stat/3/"
                }
            }
        ],
        "effect_chance": None,
        "target": "user",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "net-good-stats",
                "url": "https://pokeapi.co/api/v2/move-category/2/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Raises the user's Attack and Defense by one stage.",
        "flavor_text_entry": "Bulks up the body to boost both ATTACK and DEFENSE."
    },
    "close-combat": {
        "name": "close-combat",
        "id": 370,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 5,
        "power": 120,
        "type": "fighting",
        "damage_class": "physical",
        "stat_changes": [
            {
                "change": -1,
                "stat": {
                    "name": "Def",
                    "url": "https://pokeapi.co/api/v2/stat/3/"
                }
            },
            {
                "change": -1,
                "stat": {
                    "name": "SpDef",
                    "url": "https://pokeapi.co/api/v2/stat/5/"
                }
            }
        ],
        "effect_chance": 100,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage+raise",
                "url": "https://pokeapi.co/api/v2/move-category/7/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 100
        },
        "effect_entries": "Lowers the user's Defense and Special Defense by one stage after inflicting damage.",
        "flavor_text_entry": "The user fights the foe in close without guarding itself. It also cuts the user\u2019s Defense and Sp. Def."
    },
    "payback": {
        "name": "payback",
        "id": 371,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 10,
        "power": 50,
        "type": "dark",
        "damage_class": "physical",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Power is doubled if the target has already moved this turn.",
        "flavor_text_entry": "If the user can use this attack after the foe attacks, its power is doubled. "
    },
    "night-slash": {
        "name": "night-slash",
        "id": 400,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 15,
        "power": 70,
        "type": "dark",
        "damage_class": "physical",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 1,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Has an increased chance for a critical hit.",
        "flavor_text_entry": "The user slashes the foe the instant an opportunity arises. It has a high critical-hit ratio."
    },
    "avalanche": {
        "name": "avalanche",
        "id": 419,
        "accuracy": 100,
        "priority": -4,
        "max_pp": 10,
        "power": 60,
        "type": "ice",
        "damage_class": "physical",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Inflicts double damage if the user takes damage before attacking this turn.",
        "flavor_text_entry": "An attack move that inflicts double the damage if the user has been hurt by the foe in the same turn."
    },
    "shadow-claw": {
        "name": "shadow-claw",
        "id": 421,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 15,
        "power": 70,
        "type": "ghost",
        "damage_class": "physical",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 1,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Has an increased chance for a critical hit.",
        "flavor_text_entry": "The user slashes with a sharp claw made from shadows. It has a high critical-hit ratio."
    },
    "hone-claws": {
        "name": "hone-claws",
        "id": 468,
        "accuracy": None,
        "priority": 0,
        "max_pp": 15,
        "power": None,
        "type": "dark",
        "damage_class": "status",
        "stat_changes": [
            {
                "change": 1,
                "stat": {
                    "name": "Atk",
                    "url": "https://pokeapi.co/api/v2/stat/2/"
                }
            },
            {
                "change": 1,
                "stat": {
                    "name": "accuracy",
                    "url": "https://pokeapi.co/api/v2/stat/7/"
                }
            }
        ],
        "effect_chance": None,
        "target": "user",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "net-good-stats",
                "url": "https://pokeapi.co/api/v2/move-category/2/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Raises the user's Attack and accuracy by one stage.",
        "flavor_text_entry": "The user sharpens its claws to boost its Attack stat and accuracy."
    },
    "smack-down": {
        "name": "smack-down",
        "id": 479,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 15,
        "power": 50,
        "type": "rock",
        "damage_class": "physical",
        "stat_changes": [],
        "effect_chance": 100,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "unknown",
                "url": "https://pokeapi.co/api/v2/move-ailment/-1/"
            },
            "ailment_chance": 100,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Removes any immunity to Ground damage.",
        "flavor_text_entry": "The user throws a stone or projectile to attack an opponent. A flying Pok\u00e9mon will fall to the ground when hit."
    },
    "chip-away": {
        "name": "chip-away",
        "id": 498,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 20,
        "power": 70,
        "type": "normal",
        "damage_class": "physical",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Ignores the target's stat modifiers.",
        "flavor_text_entry": "Looking for an opening, the user strikes continually. The target\u2019s stat changes don\u2019t affect this attack\u2019s damage."
    },
    "play-nice": {
        "name": "play-nice",
        "id": 589,
        "accuracy": None,
        "priority": 0,
        "max_pp": 20,
        "power": None,
        "type": "normal",
        "damage_class": "status",
        "stat_changes": [
            {
                "change": -1,
                "stat": {
                    "name": "Atk",
                    "url": "https://pokeapi.co/api/v2/stat/2/"
                }
            }
        ],
        "effect_chance": 100,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "net-good-stats",
                "url": "https://pokeapi.co/api/v2/move-category/2/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 100
        },
        "effect_entries": "Lowers the target's Attack by one stage.",
        "flavor_text_entry": "The user and the target become friends, and the target loses its will to fight. This lowers the target\u2019s Attack stat."
    },
    "power-up-punch": {
        "name": "power-up-punch",
        "id": 612,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 20,
        "power": 40,
        "type": "fighting",
        "damage_class": "physical",
        "stat_changes": [
            {
                "change": 1,
                "stat": {
                    "name": "Atk",
                    "url": "https://pokeapi.co/api/v2/stat/2/"
                }
            }
        ],
        "effect_chance": 100,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage+raise",
                "url": "https://pokeapi.co/api/v2/move-category/7/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 100
        },
        "effect_entries": "Raises the user's Attack by one stage after inflicting damage.",
        "flavor_text_entry": "Striking opponents over and over makes the user\u2019s fists harder. Hitting a target raises the Attack stat."
    },
    "scary-face": {
        "name": "scary-face",
        "id": 184,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 10,
        "power": None,
        "type": "normal",
        "damage_class": "status",
        "stat_changes": [
            {
                "change": -2,
                "stat": {
                    "name": "Speed",
                    "url": "https://pokeapi.co/api/v2/stat/6/"
                }
            }
        ],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "net-good-stats",
                "url": "https://pokeapi.co/api/v2/move-category/2/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Lowers the target's Speed by two stages.",
        "flavor_text_entry": "Sharply reduces the foe's SPEED."
    },
    "hammer-arm": {
        "name": "hammer-arm",
        "id": 359,
        "accuracy": 90,
        "priority": 0,
        "max_pp": 10,
        "power": 100,
        "type": "fighting",
        "damage_class": "physical",
        "stat_changes": [
            {
                "change": -1,
                "stat": {
                    "name": "Speed",
                    "url": "https://pokeapi.co/api/v2/stat/6/"
                }
            }
        ],
        "effect_chance": 100,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage+raise",
                "url": "https://pokeapi.co/api/v2/move-category/7/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 100
        },
        "effect_entries": "Lowers user's Speed by one stage.",
        "flavor_text_entry": "The user swings and hits with its strong and heavy fist. It lowers the user\u2019s Speed, however."
    },
    "focus-blast": {
        "name": "focus-blast",
        "id": 411,
        "accuracy": 70,
        "priority": 0,
        "max_pp": 5,
        "power": 120,
        "type": "fighting",
        "damage_class": "special",
        "stat_changes": [
            {
                "change": -1,
                "stat": {
                    "name": "SpDef",
                    "url": "https://pokeapi.co/api/v2/stat/5/"
                }
            }
        ],
        "effect_chance": 10,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage+lower",
                "url": "https://pokeapi.co/api/v2/move-category/6/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 10
        },
        "effect_entries": "Has a 10% chance to lower the target's Special Defense by one stage.",
        "flavor_text_entry": "The user heightens its mental focus and unleashes its power. It may also lower the target\u2019s Sp. Def."
    },
    "rock-climb": {
        "name": "rock-climb",
        "id": 431,
        "accuracy": 85,
        "priority": 0,
        "max_pp": 20,
        "power": 90,
        "type": "normal",
        "damage_class": "physical",
        "stat_changes": [],
        "effect_chance": 20,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "confusion",
                "url": "https://pokeapi.co/api/v2/move-ailment/6/"
            },
            "ailment_chance": 20,
            "category": {
                "name": "damage+ailment",
                "url": "https://pokeapi.co/api/v2/move-category/4/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": 5,
            "min_hits": None,
            "min_turns": 2,
            "stat_chance": 0
        },
        "effect_entries": "Has a 20% chance to confuse the target.",
        "flavor_text_entry": "A charging attack that may also leave the foe confused. It can also be used to scale rocky walls."
    },
    "stone-edge": {
        "name": "stone-edge",
        "id": 444,
        "accuracy": 80,
        "priority": 0,
        "max_pp": 5,
        "power": 100,
        "type": "rock",
        "damage_class": "physical",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 1,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Has an increased chance for a critical hit.",
        "flavor_text_entry": "The user stabs the foe with a sharpened stone. It has a high critical-hit ratio. "
    },
    "gust": {
        "name": "gust",
        "id": 16,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 35,
        "power": 40,
        "type": "flying",
        "damage_class": "special",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Inflicts regular damage and can hit Pok\u00e9mon in the air.",
        "flavor_text_entry": "Whips up a strong gust of wind."
    },
    "wing-attack": {
        "name": "wing-attack",
        "id": 17,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 35,
        "power": 60,
        "type": "flying",
        "damage_class": "physical",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Inflicts regular damage with no additional effect.",
        "flavor_text_entry": "Strikes the target with wings."
    },
    "fly": {
        "name": "fly",
        "id": 19,
        "accuracy": 95,
        "priority": 0,
        "max_pp": 15,
        "power": 90,
        "type": "flying",
        "damage_class": "physical",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "User flies high into the air, dodging all attacks, and hits next turn.",
        "flavor_text_entry": "1st turn: Fly 2nd turn: Attack"
    },
    "supersonic": {
        "name": "supersonic",
        "id": 48,
        "accuracy": 55,
        "priority": 0,
        "max_pp": 20,
        "power": None,
        "type": "normal",
        "damage_class": "status",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "confusion",
                "url": "https://pokeapi.co/api/v2/move-ailment/6/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "ailment",
                "url": "https://pokeapi.co/api/v2/move-category/1/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": 5,
            "min_hits": None,
            "min_turns": 2,
            "stat_chance": 0
        },
        "effect_entries": "Confuses the target.",
        "flavor_text_entry": "Sound waves that cause confusion."
    },
    "mist": {
        "name": "mist",
        "id": 54,
        "accuracy": None,
        "priority": 0,
        "max_pp": 30,
        "power": None,
        "type": "ice",
        "damage_class": "status",
        "stat_changes": [],
        "effect_chance": None,
        "target": "users-field",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "field-effect",
                "url": "https://pokeapi.co/api/v2/move-category/11/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Protects the user's stats from being changed by enemy moves.",
        "flavor_text_entry": "Prevents stat reduction."
    },
    "water-gun": {
        "name": "water-gun",
        "id": 55,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 25,
        "power": 40,
        "type": "water",
        "damage_class": "special",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Inflicts regular damage with no additional effect.",
        "flavor_text_entry": "Squirts water to attack."
    },
    "hydro-pump": {
        "name": "hydro-pump",
        "id": 56,
        "accuracy": 80,
        "priority": 0,
        "max_pp": 5,
        "power": 110,
        "type": "water",
        "damage_class": "special",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Inflicts regular damage with no additional effect.",
        "flavor_text_entry": "The target is blasted by a huge volume of water launched under great pressure."
    },
    "surf": {
        "name": "surf",
        "id": 57,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 15,
        "power": 90,
        "type": "water",
        "damage_class": "special",
        "stat_changes": [],
        "effect_chance": None,
        "target": "all-other-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Inflicts regular damage and can hit Dive users.",
        "flavor_text_entry": "A strong water- type attack."
    },
    "ice-beam": {
        "name": "ice-beam",
        "id": 58,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 10,
        "power": 90,
        "type": "ice",
        "damage_class": "special",
        "stat_changes": [],
        "effect_chance": 10,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "freeze",
                "url": "https://pokeapi.co/api/v2/move-ailment/3/"
            },
            "ailment_chance": 10,
            "category": {
                "name": "damage+ailment",
                "url": "https://pokeapi.co/api/v2/move-category/4/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Has a 10% chance to freeze the target.",
        "flavor_text_entry": "An attack that may freeze the foe."
    },
    "blizzard": {
        "name": "blizzard",
        "id": 59,
        "accuracy": 70,
        "priority": 0,
        "max_pp": 5,
        "power": 110,
        "type": "ice",
        "damage_class": "special",
        "stat_changes": [],
        "effect_chance": 10,
        "target": "all-opponents",
        "meta": {
            "ailment": {
                "name": "freeze",
                "url": "https://pokeapi.co/api/v2/move-ailment/3/"
            },
            "ailment_chance": 10,
            "category": {
                "name": "damage+ailment",
                "url": "https://pokeapi.co/api/v2/move-category/4/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Has a 10% chance to freeze the target.",
        "flavor_text_entry": "An attack that may freeze the foe."
    },
    "waterfall": {
        "name": "waterfall",
        "id": 127,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 15,
        "power": 80,
        "type": "water",
        "damage_class": "physical",
        "stat_changes": [],
        "effect_chance": 20,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 20,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Has a 20% chance to make the target flinch.",
        "flavor_text_entry": "An aquatic charge attack."
    },
    "sky-attack": {
        "name": "sky-attack",
        "id": 143,
        "accuracy": 90,
        "priority": 0,
        "max_pp": 5,
        "power": 140,
        "type": "flying",
        "damage_class": "physical",
        "stat_changes": [],
        "effect_chance": 30,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 1,
            "drain": 0,
            "flinch_chance": 30,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "User charges for one turn before attacking.  Has a 30% chance to make the target flinch.",
        "flavor_text_entry": "1st turn: Prepare 2nd turn: Attack"
    },
    "icy-wind": {
        "name": "icy-wind",
        "id": 196,
        "accuracy": 95,
        "priority": 0,
        "max_pp": 15,
        "power": 55,
        "type": "ice",
        "damage_class": "special",
        "stat_changes": [
            {
                "change": -1,
                "stat": {
                    "name": "Speed",
                    "url": "https://pokeapi.co/api/v2/stat/6/"
                }
            }
        ],
        "effect_chance": 100,
        "target": "all-opponents",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage+lower",
                "url": "https://pokeapi.co/api/v2/move-category/6/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 100
        },
        "effect_entries": "Has a 100% chance to lower the target's Speed by one stage.",
        "flavor_text_entry": "A chilling attack that lowers the foe\u2019s SPEED."
    },
    "steel-wing": {
        "name": "steel-wing",
        "id": 211,
        "accuracy": 90,
        "priority": 0,
        "max_pp": 25,
        "power": 70,
        "type": "steel",
        "damage_class": "physical",
        "stat_changes": [
            {
                "change": 1,
                "stat": {
                    "name": "Def",
                    "url": "https://pokeapi.co/api/v2/stat/3/"
                }
            }
        ],
        "effect_chance": 10,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage+raise",
                "url": "https://pokeapi.co/api/v2/move-category/7/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 10
        },
        "effect_entries": "Has a 10% chance to raise the user's Defense by one stage.",
        "flavor_text_entry": "Stiff wings strike the foe."
    },
    "pursuit": {
        "name": "pursuit",
        "id": 228,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 20,
        "power": 40,
        "type": "dark",
        "damage_class": "physical",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Has double power against, and can hit, Pok\u00e9mon attempting to switch out.",
        "flavor_text_entry": "Heavily strikes switching POK\u00e9MON."
    },
    "twister": {
        "name": "twister",
        "id": 239,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 20,
        "power": 40,
        "type": "dragon",
        "damage_class": "special",
        "stat_changes": [],
        "effect_chance": 20,
        "target": "all-opponents",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 20,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Has a 20% chance to make the target flinch.",
        "flavor_text_entry": "Whips up a tornado to attack."
    },
    "whirlpool": {
        "name": "whirlpool",
        "id": 250,
        "accuracy": 85,
        "priority": 0,
        "max_pp": 15,
        "power": 35,
        "type": "water",
        "damage_class": "special",
        "stat_changes": [],
        "effect_chance": 100,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "trap",
                "url": "https://pokeapi.co/api/v2/move-ailment/8/"
            },
            "ailment_chance": 100,
            "category": {
                "name": "damage+ailment",
                "url": "https://pokeapi.co/api/v2/move-category/4/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": 6,
            "min_hits": None,
            "min_turns": 5,
            "stat_chance": 0
        },
        "effect_entries": "Prevents the target from leaving battle and inflicts 1/16 its max HP in damage for 2-5 turns.",
        "flavor_text_entry": "Traps the foe for 2-5 turns."
    },
    "hail": {
        "name": "hail",
        "id": 258,
        "accuracy": None,
        "priority": 0,
        "max_pp": 10,
        "power": None,
        "type": "ice",
        "damage_class": "status",
        "stat_changes": [],
        "effect_chance": None,
        "target": "entire-field",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "whole-field-effect",
                "url": "https://pokeapi.co/api/v2/move-category/10/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Changes the weather to a hailstorm for five turns.",
        "flavor_text_entry": "Summons a hailstorm that strikes every turn."
    },
    "knock-off": {
        "name": "knock-off",
        "id": 282,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 20,
        "power": 65,
        "type": "dark",
        "damage_class": "physical",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Target drops its held item.",
        "flavor_text_entry": "Knocks down the foe\u2019s held item to prevent its use."
    },
    "feather-dance": {
        "name": "feather-dance",
        "id": 297,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 15,
        "power": None,
        "type": "flying",
        "damage_class": "status",
        "stat_changes": [
            {
                "change": -2,
                "stat": {
                    "name": "Atk",
                    "url": "https://pokeapi.co/api/v2/stat/2/"
                }
            }
        ],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "net-good-stats",
                "url": "https://pokeapi.co/api/v2/move-category/2/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Lowers the target's Attack by two stages.",
        "flavor_text_entry": "Envelops the foe with down to sharply reduce ATTACK."
    },
    "air-cutter": {
        "name": "air-cutter",
        "id": 314,
        "accuracy": 95,
        "priority": 0,
        "max_pp": 25,
        "power": 60,
        "type": "flying",
        "damage_class": "special",
        "stat_changes": [],
        "effect_chance": None,
        "target": "all-opponents",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 1,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Has an increased chance for a critical hit.",
        "flavor_text_entry": "Hacks with razorlike wind. High critical-hit ratio."
    },
    "muddy-water": {
        "name": "muddy-water",
        "id": 330,
        "accuracy": 85,
        "priority": 0,
        "max_pp": 10,
        "power": 90,
        "type": "water",
        "damage_class": "special",
        "stat_changes": [
            {
                "change": -1,
                "stat": {
                    "name": "accuracy",
                    "url": "https://pokeapi.co/api/v2/stat/7/"
                }
            }
        ],
        "effect_chance": 30,
        "target": "all-opponents",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage+lower",
                "url": "https://pokeapi.co/api/v2/move-category/6/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 30
        },
        "effect_entries": "Has a 30% chance to lower the target's accuracy by one stage.",
        "flavor_text_entry": "Attacks with muddy water. May lower accuracy."
    },
    "water-sport": {
        "name": "water-sport",
        "id": 346,
        "accuracy": None,
        "priority": 0,
        "max_pp": 15,
        "power": None,
        "type": "water",
        "damage_class": "status",
        "stat_changes": [],
        "effect_chance": None,
        "target": "entire-field",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "whole-field-effect",
                "url": "https://pokeapi.co/api/v2/move-category/10/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Halves all Fire-type damage.",
        "flavor_text_entry": "The user becomes soaked to raise resistance to fire."
    },
    "water-pulse": {
        "name": "water-pulse",
        "id": 352,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 20,
        "power": 60,
        "type": "water",
        "damage_class": "special",
        "stat_changes": [],
        "effect_chance": 20,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "confusion",
                "url": "https://pokeapi.co/api/v2/move-ailment/6/"
            },
            "ailment_chance": 20,
            "category": {
                "name": "damage+ailment",
                "url": "https://pokeapi.co/api/v2/move-category/4/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": 5,
            "min_hits": None,
            "min_turns": 2,
            "stat_chance": 0
        },
        "effect_entries": "Has a 20% chance to confuse the target.",
        "flavor_text_entry": "Attacks with ultrasonic waves. May confuse the foe"
    },
    "roost": {
        "name": "roost",
        "id": 355,
        "accuracy": None,
        "priority": 0,
        "max_pp": 5,
        "power": None,
        "type": "flying",
        "damage_class": "status",
        "stat_changes": [],
        "effect_chance": None,
        "target": "user",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "heal",
                "url": "https://pokeapi.co/api/v2/move-category/3/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 50,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Heals the user by half its max HP.",
        "flavor_text_entry": "The user lands and rests its body. It restores the user\u2019s HP by up to half of its max HP."
    },
    "brine": {
        "name": "brine",
        "id": 362,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 10,
        "power": 65,
        "type": "water",
        "damage_class": "special",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Has double power against Pok\u00e9mon that have less than half their max HP remaining.",
        "flavor_text_entry": "If the foe\u2019s HP is down to about half, this attack will hit with double the power."
    },
    "pluck": {
        "name": "pluck",
        "id": 365,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 20,
        "power": 60,
        "type": "flying",
        "damage_class": "physical",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "If target has a berry, inflicts double damage and uses the berry.",
        "flavor_text_entry": "The user pecks the foe. If the foe is holding a Berry, the user plucks it and gains its effect."
    },
    "tailwind": {
        "name": "tailwind",
        "id": 366,
        "accuracy": None,
        "priority": 0,
        "max_pp": 15,
        "power": None,
        "type": "flying",
        "damage_class": "status",
        "stat_changes": [],
        "effect_chance": None,
        "target": "users-field",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "field-effect",
                "url": "https://pokeapi.co/api/v2/move-category/11/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "For three turns, friendly Pok\u00e9mon have doubled Speed.",
        "flavor_text_entry": "The user whips up a turbulent whirlwind that ups the Speed of all party Pok\u00e9mon for three turns."
    },
    "aqua-ring": {
        "name": "aqua-ring",
        "id": 392,
        "accuracy": None,
        "priority": 0,
        "max_pp": 20,
        "power": None,
        "type": "water",
        "damage_class": "status",
        "stat_changes": [],
        "effect_chance": None,
        "target": "user",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "unique",
                "url": "https://pokeapi.co/api/v2/move-category/13/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Restores 1/16 of the user's max HP each turn.",
        "flavor_text_entry": "The user envelops itself in a veil made of water. It regains some HP on every turn."
    },
    "air-slash": {
        "name": "air-slash",
        "id": 403,
        "accuracy": 95,
        "priority": 0,
        "max_pp": 15,
        "power": 75,
        "type": "flying",
        "damage_class": "special",
        "stat_changes": [],
        "effect_chance": 30,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 30,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Has a 30% chance to make the target flinch.",
        "flavor_text_entry": "The user attacks with a blade of air that slices even the sky. It may also make the target flinch."
    },
    "brave-bird": {
        "name": "brave-bird",
        "id": 413,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 15,
        "power": 120,
        "type": "flying",
        "damage_class": "physical",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 0,
            "drain": -33,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "User receives 1/3 the damage inflicted in recoil.",
        "flavor_text_entry": "The user tucks in its wings and charges from a low altitude. The user also takes serious damage."
    },
    "defog": {
        "name": "defog",
        "id": 432,
        "accuracy": None,
        "priority": 0,
        "max_pp": 15,
        "power": None,
        "type": "flying",
        "damage_class": "status",
        "stat_changes": [
            {
                "change": -1,
                "stat": {
                    "name": "evasion",
                    "url": "https://pokeapi.co/api/v2/stat/8/"
                }
            }
        ],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "unique",
                "url": "https://pokeapi.co/api/v2/move-category/13/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Lowers the target's evasion by one stage.  Removes field effects from the enemy field.",
        "flavor_text_entry": "Obstacles are moved, reducing the foe\u2019s evasion stat. It can also be used to clear deep fog, etc."
    },
    "ominous-wind": {
        "name": "ominous-wind",
        "id": 466,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 5,
        "power": 60,
        "type": "ghost",
        "damage_class": "special",
        "stat_changes": [
            {
                "change": 1,
                "stat": {
                    "name": "Atk",
                    "url": "https://pokeapi.co/api/v2/stat/2/"
                }
            },
            {
                "change": 1,
                "stat": {
                    "name": "Def",
                    "url": "https://pokeapi.co/api/v2/stat/3/"
                }
            },
            {
                "change": 1,
                "stat": {
                    "name": "SpAtk",
                    "url": "https://pokeapi.co/api/v2/stat/4/"
                }
            },
            {
                "change": 1,
                "stat": {
                    "name": "SpDef",
                    "url": "https://pokeapi.co/api/v2/stat/5/"
                }
            },
            {
                "change": 1,
                "stat": {
                    "name": "Speed",
                    "url": "https://pokeapi.co/api/v2/stat/6/"
                }
            }
        ],
        "effect_chance": 10,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 10,
            "category": {
                "name": "damage+raise",
                "url": "https://pokeapi.co/api/v2/move-category/7/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 10
        },
        "effect_entries": "Has a 10% chance to raise all of the user's stats by one stage.",
        "flavor_text_entry": "The user creates a gust of repulsive wind. It may also raise all the user\u2019s stats at once."
    },
    "wide-guard": {
        "name": "wide-guard",
        "id": 469,
        "accuracy": None,
        "priority": 3,
        "max_pp": 10,
        "power": None,
        "type": "rock",
        "damage_class": "status",
        "stat_changes": [],
        "effect_chance": None,
        "target": "users-field",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "field-effect",
                "url": "https://pokeapi.co/api/v2/move-category/11/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Prevents any multi-target moves from hitting friendly Pok\u00e9mon this turn.",
        "flavor_text_entry": "The user and its allies are protected from wide-ranging attacks for one turn. If used in succession, its chance of failing rises."
    },
    "soak": {
        "name": "soak",
        "id": 487,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 20,
        "power": None,
        "type": "water",
        "damage_class": "status",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "unique",
                "url": "https://pokeapi.co/api/v2/move-category/13/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Changes the target's type to Water.",
        "flavor_text_entry": "The user shoots a torrent of water at the target and changes the target\u2019s type to Water."
    },
    "scald": {
        "name": "scald",
        "id": 503,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 15,
        "power": 80,
        "type": "water",
        "damage_class": "special",
        "stat_changes": [],
        "effect_chance": 30,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "burn",
                "url": "https://pokeapi.co/api/v2/move-ailment/4/"
            },
            "ailment_chance": 30,
            "category": {
                "name": "damage+ailment",
                "url": "https://pokeapi.co/api/v2/move-category/4/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Has a 30% chance to burn the target.",
        "flavor_text_entry": "The user shoots boiling hot water at its target. It may also leave the target with a burn."
    },
    "acrobatics": {
        "name": "acrobatics",
        "id": 512,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 15,
        "power": 55,
        "type": "flying",
        "damage_class": "physical",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Has double power if the user has no held item.",
        "flavor_text_entry": "The user nimbly strikes the target. If the user is not holding an item, this attack inflicts massive damage."
    },
    "hurricane": {
        "name": "hurricane",
        "id": 542,
        "accuracy": 70,
        "priority": 0,
        "max_pp": 10,
        "power": 110,
        "type": "flying",
        "damage_class": "special",
        "stat_changes": [],
        "effect_chance": 30,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "confusion",
                "url": "https://pokeapi.co/api/v2/move-ailment/6/"
            },
            "ailment_chance": 30,
            "category": {
                "name": "damage+ailment",
                "url": "https://pokeapi.co/api/v2/move-category/4/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": 5,
            "min_hits": None,
            "min_turns": 2,
            "stat_chance": 0
        },
        "effect_entries": "Has a 30% chance to confuse the target.",
        "flavor_text_entry": "The user attacks by wrapping its opponent in a fierce wind that flies up into the sky. It may also confuse the target."
    },
    "liquidation": {
        "name": "liquidation",
        "id": 710,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 10,
        "power": 85,
        "type": "water",
        "damage_class": "physical",
        "stat_changes": [
            {
                "change": -1,
                "stat": {
                    "name": "Def",
                    "url": "https://pokeapi.co/api/v2/stat/3/"
                }
            }
        ],
        "effect_chance": 20,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage+lower",
                "url": "https://pokeapi.co/api/v2/move-category/6/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 20
        },
        "effect_entries": "Has a 20% chance to lower the target's Defense by one stage.",
        "flavor_text_entry": "The user slams into the target using a full-force blast of water. This may also lower the target\u2019s Defense stat."
    },
    "dual-wingbeat": {
        "name": "dual-wingbeat",
        "id": 814,
        "accuracy": 90,
        "priority": 0,
        "max_pp": 10,
        "power": 40,
        "type": "flying",
        "damage_class": "physical",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": 2,
            "max_turns": None,
            "min_hits": 2,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Inflicts regular damage with no additional effect.",
        "flavor_text_entry": "The user slams the target with its wings. The target is hit twice in a row."
    },
    "snowscape": {
        "name": "snowscape",
        "id": 883,
        "accuracy": None,
        "priority": 0,
        "max_pp": 10,
        "power": 0,
        "type": "ice",
        "damage_class": "status",
        "stat_changes": [],
        "effect_chance": None,
        "target": "entire-field",
        "meta": None
    },
    "chilling-water": {
        "name": "chilling-water",
        "id": 886,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 20,
        "power": 50,
        "type": "water",
        "damage_class": "special",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": None
    },
    "stockpile": {
        "name": "stockpile",
        "id": 254,
        "accuracy": None,
        "priority": 0,
        "max_pp": 20,
        "power": None,
        "type": "normal",
        "damage_class": "status",
        "stat_changes": [
            {
                "change": 1,
                "stat": {
                    "name": "Def",
                    "url": "https://pokeapi.co/api/v2/stat/3/"
                }
            },
            {
                "change": 1,
                "stat": {
                    "name": "SpDef",
                    "url": "https://pokeapi.co/api/v2/stat/5/"
                }
            }
        ],
        "effect_chance": None,
        "target": "user",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "unique",
                "url": "https://pokeapi.co/api/v2/move-category/13/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Stores energy up to three times for use with Spit Up and Swallow.",
        "flavor_text_entry": "Charges up power for up to 3 turns."
    },
    "spit-up": {
        "name": "spit-up",
        "id": 255,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 10,
        "power": None,
        "type": "normal",
        "damage_class": "special",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Power is 100 times the amount of energy Stockpiled.",
        "flavor_text_entry": "Releases stockpiled power (the more the better)."
    },
    "swallow": {
        "name": "swallow",
        "id": 256,
        "accuracy": None,
        "priority": 0,
        "max_pp": 10,
        "power": None,
        "type": "normal",
        "damage_class": "status",
        "stat_changes": [],
        "effect_chance": None,
        "target": "user",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "heal",
                "url": "https://pokeapi.co/api/v2/move-category/3/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 25,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Recovers 1/4 HP after one Stockpile, 1/2 HP after two Stockpiles, or full HP after three Stockpiles.",
        "flavor_text_entry": "Absorbs stockpiled power and restores HP."
    },
    "weather-ball": {
        "name": "weather-ball",
        "id": 311,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 10,
        "power": 50,
        "type": "normal",
        "damage_class": "special",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "If there be weather, this move has doubled power and the weather's type.",
        "flavor_text_entry": "The move\u2019s type and power change with the weather."
    },
    "sky-drop": {
        "name": "sky-drop",
        "id": 507,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 10,
        "power": 60,
        "type": "flying",
        "damage_class": "physical",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Carries the target high into the air, dodging all attacks against either, and drops it next turn.",
        "flavor_text_entry": "The user takes the target into the sky, then drops it during the next turn. The target cannot attack while in the sky."
    },
    "psybeam": {
        "name": "psybeam",
        "id": 60,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 20,
        "power": 65,
        "type": "psychic",
        "damage_class": "special",
        "stat_changes": [],
        "effect_chance": 10,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "confusion",
                "url": "https://pokeapi.co/api/v2/move-ailment/6/"
            },
            "ailment_chance": 10,
            "category": {
                "name": "damage+ailment",
                "url": "https://pokeapi.co/api/v2/move-category/4/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": 5,
            "min_hits": None,
            "min_turns": 2,
            "stat_chance": 0
        },
        "effect_entries": "Has a 10% chance to confuse the target.",
        "flavor_text_entry": "The target is attacked with a peculiar ray. This may also leave the target confused."
    },
    "bubble-beam": {
        "name": "bubble-beam",
        "id": 61,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 20,
        "power": 65,
        "type": "water",
        "damage_class": "special",
        "stat_changes": [
            {
                "change": -1,
                "stat": {
                    "name": "Speed",
                    "url": "https://pokeapi.co/api/v2/stat/6/"
                }
            }
        ],
        "effect_chance": 10,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage+lower",
                "url": "https://pokeapi.co/api/v2/move-category/6/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 10
        },
        "effect_entries": "Has a 10% chance to lower the target's Speed by one stage.",
        "flavor_text_entry": "An attack that may lower SPEED."
    },
    "aurora-beam": {
        "name": "aurora-beam",
        "id": 62,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 20,
        "power": 65,
        "type": "ice",
        "damage_class": "special",
        "stat_changes": [
            {
                "change": -1,
                "stat": {
                    "name": "Atk",
                    "url": "https://pokeapi.co/api/v2/stat/2/"
                }
            }
        ],
        "effect_chance": 10,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage+lower",
                "url": "https://pokeapi.co/api/v2/move-category/6/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 10
        },
        "effect_entries": "Has a 10% chance to lower the target's Attack by one stage.",
        "flavor_text_entry": "An attack that may lower ATTACK."
    },
    "psychic": {
        "name": "psychic",
        "id": 94,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 10,
        "power": 90,
        "type": "psychic",
        "damage_class": "special",
        "stat_changes": [
            {
                "change": -1,
                "stat": {
                    "name": "SpDef",
                    "url": "https://pokeapi.co/api/v2/stat/5/"
                }
            }
        ],
        "effect_chance": 10,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage+lower",
                "url": "https://pokeapi.co/api/v2/move-category/6/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 10
        },
        "effect_entries": "Has a 10% chance to lower the target's Special Defense by one stage.",
        "flavor_text_entry": "An attack that may lower SPCL.DEF."
    },
    "rage": {
        "name": "rage",
        "id": 99,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 20,
        "power": 20,
        "type": "normal",
        "damage_class": "physical",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "If the user is hit after using this move, its Attack rises by one stage.",
        "flavor_text_entry": "Raises ATTACK if the user is hit."
    },
    "teleport": {
        "name": "teleport",
        "id": 100,
        "accuracy": None,
        "priority": -6,
        "max_pp": 20,
        "power": None,
        "type": "psychic",
        "damage_class": "status",
        "stat_changes": [],
        "effect_chance": None,
        "target": "user",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "unique",
                "url": "https://pokeapi.co/api/v2/move-category/13/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Immediately ends wild battles.  No effect otherwise.",
        "flavor_text_entry": "A move for fleeing from battle."
    },
    "recover": {
        "name": "recover",
        "id": 105,
        "accuracy": None,
        "priority": 0,
        "max_pp": 5,
        "power": None,
        "type": "normal",
        "damage_class": "status",
        "stat_changes": [],
        "effect_chance": None,
        "target": "user",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "heal",
                "url": "https://pokeapi.co/api/v2/move-category/3/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 50,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Heals the user by half its max HP.",
        "flavor_text_entry": "Restores HP by 1/2 the max HP."
    },
    "harden": {
        "name": "harden",
        "id": 106,
        "accuracy": None,
        "priority": 0,
        "max_pp": 30,
        "power": None,
        "type": "normal",
        "damage_class": "status",
        "stat_changes": [
            {
                "change": 1,
                "stat": {
                    "name": "Def",
                    "url": "https://pokeapi.co/api/v2/stat/3/"
                }
            }
        ],
        "effect_chance": None,
        "target": "user",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "net-good-stats",
                "url": "https://pokeapi.co/api/v2/move-category/2/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Raises the user's Defense by one stage.",
        "flavor_text_entry": "Raises the user's DEFENSE."
    },
    "minimize": {
        "name": "minimize",
        "id": 107,
        "accuracy": None,
        "priority": 0,
        "max_pp": 10,
        "power": None,
        "type": "normal",
        "damage_class": "status",
        "stat_changes": [
            {
                "change": 2,
                "stat": {
                    "name": "evasion",
                    "url": "https://pokeapi.co/api/v2/stat/8/"
                }
            }
        ],
        "effect_chance": None,
        "target": "user",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "net-good-stats",
                "url": "https://pokeapi.co/api/v2/move-category/2/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Raises the user's evasion by two stages.",
        "flavor_text_entry": "Heightens evasive\u00ad ness."
    },
    "confuse-ray": {
        "name": "confuse-ray",
        "id": 109,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 10,
        "power": None,
        "type": "ghost",
        "damage_class": "status",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "confusion",
                "url": "https://pokeapi.co/api/v2/move-ailment/6/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "ailment",
                "url": "https://pokeapi.co/api/v2/move-category/1/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": 5,
            "min_hits": None,
            "min_turns": 2,
            "stat_chance": 0
        },
        "effect_entries": "Confuses the target.",
        "flavor_text_entry": "A move that causes confusion."
    },
    "barrier": {
        "name": "barrier",
        "id": 112,
        "accuracy": None,
        "priority": 0,
        "max_pp": 20,
        "power": None,
        "type": "psychic",
        "damage_class": "status",
        "stat_changes": [
            {
                "change": 2,
                "stat": {
                    "name": "Def",
                    "url": "https://pokeapi.co/api/v2/stat/3/"
                }
            }
        ],
        "effect_chance": None,
        "target": "user",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "net-good-stats",
                "url": "https://pokeapi.co/api/v2/move-category/2/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Raises the user's Defense by two stages.",
        "flavor_text_entry": "Sharply increases user's DEFENSE."
    },
    "reflect": {
        "name": "reflect",
        "id": 115,
        "accuracy": None,
        "priority": 0,
        "max_pp": 20,
        "power": None,
        "type": "psychic",
        "damage_class": "status",
        "stat_changes": [],
        "effect_chance": None,
        "target": "users-field",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "field-effect",
                "url": "https://pokeapi.co/api/v2/move-category/11/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Reduces damage from physical attacks by half.",
        "flavor_text_entry": "Raises DEFENSE with a barrier."
    },
    "skull-bash": {
        "name": "skull-bash",
        "id": 130,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 10,
        "power": 130,
        "type": "normal",
        "damage_class": "physical",
        "stat_changes": [],
        "effect_chance": 100,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 100,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Raises the user's Defense by one stage.  User charges for one turn before attacking.",
        "flavor_text_entry": "1st turn: Prepare 2nd turn: Attack"
    },
    "psywave": {
        "name": "psywave",
        "id": 149,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 15,
        "power": None,
        "type": "psychic",
        "damage_class": "special",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Inflicts damage between 50% and 150% of the user's level.",
        "flavor_text_entry": "An attack with variable power."
    },
    "tri-attack": {
        "name": "tri-attack",
        "id": 161,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 10,
        "power": 80,
        "type": "normal",
        "damage_class": "special",
        "stat_changes": [],
        "effect_chance": 20,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "unknown",
                "url": "https://pokeapi.co/api/v2/move-ailment/-1/"
            },
            "ailment_chance": 20,
            "category": {
                "name": "damage+ailment",
                "url": "https://pokeapi.co/api/v2/move-category/4/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Has a 20% chance to burn, freeze, or paralyze the target.",
        "flavor_text_entry": "Fires three kinds of beams at once."
    },
    "pain-split": {
        "name": "pain-split",
        "id": 220,
        "accuracy": None,
        "priority": 0,
        "max_pp": 20,
        "power": None,
        "type": "normal",
        "damage_class": "status",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "unique",
                "url": "https://pokeapi.co/api/v2/move-category/13/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Sets the user's and targets's HP to the average of their current HP.",
        "flavor_text_entry": "Adds user & foe's HPs. Shares total."
    },
    "rapid-spin": {
        "name": "rapid-spin",
        "id": 229,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 40,
        "power": 50,
        "type": "normal",
        "damage_class": "physical",
        "stat_changes": [
            {
                "change": 1,
                "stat": {
                    "name": "Speed",
                    "url": "https://pokeapi.co/api/v2/stat/6/"
                }
            }
        ],
        "effect_chance": 100,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage+raise",
                "url": "https://pokeapi.co/api/v2/move-category/7/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 100
        },
        "effect_entries": "Frees the user from binding moves, removes Leech Seed, and blows away Spikes.",
        "flavor_text_entry": "A high-speed spinning attack."
    },
    "psych-up": {
        "name": "psych-up",
        "id": 244,
        "accuracy": None,
        "priority": 0,
        "max_pp": 10,
        "power": None,
        "type": "normal",
        "damage_class": "status",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "unique",
                "url": "https://pokeapi.co/api/v2/move-category/13/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Discards the user's stat changes and copies the target's.",
        "flavor_text_entry": "Copies the foe's stat changes."
    },
    "magic-coat": {
        "name": "magic-coat",
        "id": 277,
        "accuracy": None,
        "priority": 4,
        "max_pp": 15,
        "power": None,
        "type": "psychic",
        "damage_class": "status",
        "stat_changes": [],
        "effect_chance": None,
        "target": "user",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "unique",
                "url": "https://pokeapi.co/api/v2/move-category/13/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Reflects back the first effect move used on the user this turn.",
        "flavor_text_entry": "Reflects special effects back to the attacker."
    },
    "recycle": {
        "name": "recycle",
        "id": 278,
        "accuracy": None,
        "priority": 0,
        "max_pp": 10,
        "power": None,
        "type": "normal",
        "damage_class": "status",
        "stat_changes": [],
        "effect_chance": None,
        "target": "user",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "unique",
                "url": "https://pokeapi.co/api/v2/move-category/13/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "User recovers the item it last used up.",
        "flavor_text_entry": "Recycles a used item for one more use."
    },
    "dive": {
        "name": "dive",
        "id": 291,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 10,
        "power": 80,
        "type": "water",
        "damage_class": "physical",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "User dives underwater, dodging all attacks, and hits next turn.",
        "flavor_text_entry": "Dives underwater the first turn and strikes next turn."
    },
    "cosmic-power": {
        "name": "cosmic-power",
        "id": 322,
        "accuracy": None,
        "priority": 0,
        "max_pp": 20,
        "power": None,
        "type": "psychic",
        "damage_class": "status",
        "stat_changes": [
            {
                "change": 1,
                "stat": {
                    "name": "Def",
                    "url": "https://pokeapi.co/api/v2/stat/3/"
                }
            },
            {
                "change": 1,
                "stat": {
                    "name": "SpDef",
                    "url": "https://pokeapi.co/api/v2/stat/5/"
                }
            }
        ],
        "effect_chance": None,
        "target": "user",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "net-good-stats",
                "url": "https://pokeapi.co/api/v2/move-category/2/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Raises the user's Defense and Special Defense by one stage.",
        "flavor_text_entry": "Raises DEFENSE and SP. DEF with a mystic power."
    },
    "signal-beam": {
        "name": "signal-beam",
        "id": 324,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 15,
        "power": 75,
        "type": "bug",
        "damage_class": "special",
        "stat_changes": [],
        "effect_chance": 10,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "confusion",
                "url": "https://pokeapi.co/api/v2/move-ailment/6/"
            },
            "ailment_chance": 10,
            "category": {
                "name": "damage+ailment",
                "url": "https://pokeapi.co/api/v2/move-category/4/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": 5,
            "min_hits": None,
            "min_turns": 2,
            "stat_chance": 0
        },
        "effect_entries": "Has a 10% chance to confuse the target.",
        "flavor_text_entry": "A strange beam attack that may confuse the foe."
    },
    "gravity": {
        "name": "gravity",
        "id": 356,
        "accuracy": None,
        "priority": 0,
        "max_pp": 5,
        "power": None,
        "type": "psychic",
        "damage_class": "status",
        "stat_changes": [],
        "effect_chance": None,
        "target": "entire-field",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "whole-field-effect",
                "url": "https://pokeapi.co/api/v2/move-category/10/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Disables moves and immunities that involve flying or levitating for five turns.",
        "flavor_text_entry": "Gravity is intensified for five turns, making moves involving flying unusable and negating Levitation."
    },
    "gyro-ball": {
        "name": "gyro-ball",
        "id": 360,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 5,
        "power": None,
        "type": "steel",
        "damage_class": "physical",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Power raises when the user has lower Speed, up to a maximum of 150.",
        "flavor_text_entry": "The user tackles the foe with a high-speed spin. The slower the user, the greater the damage."
    },
    "power-gem": {
        "name": "power-gem",
        "id": 408,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 20,
        "power": 80,
        "type": "rock",
        "damage_class": "special",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Inflicts regular damage with no additional effect.",
        "flavor_text_entry": "The user attacks with a ray of light that sparkles as if it were made of gemstones. "
    },
    "flash-cannon": {
        "name": "flash-cannon",
        "id": 430,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 10,
        "power": 80,
        "type": "steel",
        "damage_class": "special",
        "stat_changes": [
            {
                "change": -1,
                "stat": {
                    "name": "SpDef",
                    "url": "https://pokeapi.co/api/v2/stat/5/"
                }
            }
        ],
        "effect_chance": 10,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage+lower",
                "url": "https://pokeapi.co/api/v2/move-category/6/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 10
        },
        "effect_entries": "Has a 10% chance to lower the target's Special Defense by one stage.",
        "flavor_text_entry": "The user gathers all its light energy and releases it at once. It may also lower the foe\u2019s Sp. Def stat."
    },
    "reflect-type": {
        "name": "reflect-type",
        "id": 513,
        "accuracy": None,
        "priority": 0,
        "max_pp": 15,
        "power": None,
        "type": "normal",
        "damage_class": "status",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "unique",
                "url": "https://pokeapi.co/api/v2/move-category/13/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "User becomes the target's type.",
        "flavor_text_entry": "The user reflects the target\u2019s type, making it the same type as the target."
    },
    "dazzling-gleam": {
        "name": "dazzling-gleam",
        "id": 605,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 10,
        "power": 80,
        "type": "fairy",
        "damage_class": "special",
        "stat_changes": [],
        "effect_chance": None,
        "target": "all-opponents",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Inflicts regular damage with no additional effect.",
        "flavor_text_entry": "The user damages opposing Pok\u00e9mon by emitting a powerful flash."
    },
    "flip-turn": {
        "name": "flip-turn",
        "id": 812,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 20,
        "power": 60,
        "type": "water",
        "damage_class": "physical",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Inflicts regular damage with no additional effect.",
        "flavor_text_entry": "After making its attack, the user rushes back to switch places with a party Pok\u00e9mon in waiting."
    },
    "dream-eater": {
        "name": "dream-eater",
        "id": 138,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 15,
        "power": 100,
        "type": "psychic",
        "damage_class": "special",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage+heal",
                "url": "https://pokeapi.co/api/v2/move-category/8/"
            },
            "crit_rate": 0,
            "drain": 50,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Only works on sleeping Pok\u00e9mon.  Drains half the damage inflicted to heal the user.",
        "flavor_text_entry": "Steals HP from a sleeping victim."
    },
    "nightmare": {
        "name": "nightmare",
        "id": 171,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 15,
        "power": None,
        "type": "ghost",
        "damage_class": "status",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "nightmare",
                "url": "https://pokeapi.co/api/v2/move-ailment/9/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "ailment",
                "url": "https://pokeapi.co/api/v2/move-category/1/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Target loses 1/4 its max HP every turn as long as it's asleep.",
        "flavor_text_entry": "A sleeper loses 1/4 HP every turn."
    },
    "trick": {
        "name": "trick",
        "id": 271,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 10,
        "power": None,
        "type": "psychic",
        "damage_class": "status",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "unique",
                "url": "https://pokeapi.co/api/v2/move-category/13/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "User and target swap items.",
        "flavor_text_entry": "Tricks the foe into trading held items."
    },
    "skill-swap": {
        "name": "skill-swap",
        "id": 285,
        "accuracy": None,
        "priority": 0,
        "max_pp": 10,
        "power": None,
        "type": "psychic",
        "damage_class": "status",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "unique",
                "url": "https://pokeapi.co/api/v2/move-category/13/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "User and target swap abilities.",
        "flavor_text_entry": "The user swaps special abilities with the target."
    },
    "psycho-cut": {
        "name": "psycho-cut",
        "id": 427,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 20,
        "power": 70,
        "type": "psychic",
        "damage_class": "physical",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 1,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Has an increased chance for a critical hit.",
        "flavor_text_entry": "The user tears at the foe with blades formed by psychic power. It has a high critical-hit ratio."
    },
    "trick-room": {
        "name": "trick-room",
        "id": 433,
        "accuracy": None,
        "priority": -7,
        "max_pp": 5,
        "power": None,
        "type": "psychic",
        "damage_class": "status",
        "stat_changes": [],
        "effect_chance": None,
        "target": "entire-field",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "whole-field-effect",
                "url": "https://pokeapi.co/api/v2/move-category/10/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "For five turns, slower Pok\u00e9mon will act before faster Pok\u00e9mon.",
        "flavor_text_entry": "The user creates a bizarre area in which slower Pok\u00e9mon get to move first for five turns."
    },
    "wonder-room": {
        "name": "wonder-room",
        "id": 472,
        "accuracy": None,
        "priority": 0,
        "max_pp": 10,
        "power": None,
        "type": "psychic",
        "damage_class": "status",
        "stat_changes": [],
        "effect_chance": None,
        "target": "entire-field",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "whole-field-effect",
                "url": "https://pokeapi.co/api/v2/move-category/10/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "All Pok\u00e9mon's Defense and Special Defense are swapped for 5 turns.",
        "flavor_text_entry": "The user creates a bizarre area in which Pok\u00e9mon\u2019s Defense and Sp. Def stats are swapped for five turns."
    },
    "psyshock": {
        "name": "psyshock",
        "id": 473,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 10,
        "power": 80,
        "type": "psychic",
        "damage_class": "special",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Inflicts damage based on the target's Defense, not Special Defense.",
        "flavor_text_entry": "The user materializes an odd psychic wave to attack the target. This attack does physical damage."
    },
    "telekinesis": {
        "name": "telekinesis",
        "id": 477,
        "accuracy": None,
        "priority": 0,
        "max_pp": 15,
        "power": None,
        "type": "psychic",
        "damage_class": "status",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "unknown",
                "url": "https://pokeapi.co/api/v2/move-ailment/-1/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "ailment",
                "url": "https://pokeapi.co/api/v2/move-category/1/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": 3,
            "min_hits": None,
            "min_turns": 3,
            "stat_chance": 0
        },
        "effect_entries": "Moves have 100% accuracy against the target for three turns.",
        "flavor_text_entry": "The user makes the target float with its psychic power. The target is easier to hit for three turns."
    },
    "ally-switch": {
        "name": "ally-switch",
        "id": 502,
        "accuracy": None,
        "priority": 2,
        "max_pp": 15,
        "power": None,
        "type": "psychic",
        "damage_class": "status",
        "stat_changes": [],
        "effect_chance": None,
        "target": "user",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "unique",
                "url": "https://pokeapi.co/api/v2/move-category/13/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "User switches places with the friendly Pok\u00e9mon opposite it.",
        "flavor_text_entry": "The user teleports using a strange power and switches its place with one of its allies."
    },
    "spotlight": {
        "name": "spotlight",
        "id": 671,
        "accuracy": None,
        "priority": 3,
        "max_pp": 15,
        "power": None,
        "type": "normal",
        "damage_class": "status",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "unique",
                "url": "https://pokeapi.co/api/v2/move-category/13/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Forces the target's opponents to aim at the target for the rest of the turn.",
        "flavor_text_entry": "The user shines a spotlight on the target so that only the target will be attacked during the turn."
    },
    "expanding-force": {
        "name": "expanding-force",
        "id": 797,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 10,
        "power": 80,
        "type": "psychic",
        "damage_class": "special",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Inflicts regular damage with no additional effect.",
        "flavor_text_entry": "The user attacks the target with its psychic power. This move\u2019s power goes up and damages all opposing Pok\u00e9mon on Psychic Terrain."
    },
    "meteor-beam": {
        "name": "meteor-beam",
        "id": 800,
        "accuracy": 90,
        "priority": 0,
        "max_pp": 10,
        "power": 120,
        "type": "rock",
        "damage_class": "special",
        "stat_changes": [],
        "effect_chance": 100,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 100,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Inflicts regular damage with no additional effect.",
        "flavor_text_entry": "In this two-turn attack, the user gathers space power and boosts its Sp. Atk stat, then attacks the target on the next turn."
    },
    "fissure": {
        "name": "fissure",
        "id": 90,
        "accuracy": 30,
        "priority": 0,
        "max_pp": 5,
        "power": None,
        "type": "ground",
        "damage_class": "physical",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "ohko",
                "url": "https://pokeapi.co/api/v2/move-category/9/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Causes a one-hit KO.",
        "flavor_text_entry": "A ground-type, one-hit KO attack."
    },
    "powder-snow": {
        "name": "powder-snow",
        "id": 181,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 25,
        "power": 40,
        "type": "ice",
        "damage_class": "special",
        "stat_changes": [],
        "effect_chance": 10,
        "target": "all-opponents",
        "meta": {
            "ailment": {
                "name": "freeze",
                "url": "https://pokeapi.co/api/v2/move-ailment/3/"
            },
            "ailment_chance": 10,
            "category": {
                "name": "damage+ailment",
                "url": "https://pokeapi.co/api/v2/move-category/4/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Has a 10% chance to freeze the target.",
        "flavor_text_entry": "An attack that may cause freezing."
    },
    "ice-ball": {
        "name": "ice-ball",
        "id": 301,
        "accuracy": 90,
        "priority": 0,
        "max_pp": 20,
        "power": 30,
        "type": "ice",
        "damage_class": "physical",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Power doubles every turn this move is used in succession after the first, resetting after five turns.",
        "flavor_text_entry": "A 5-turn attack that gains power on successive hits."
    },
    "sheer-cold": {
        "name": "sheer-cold",
        "id": 329,
        "accuracy": 30,
        "priority": 0,
        "max_pp": 5,
        "power": None,
        "type": "ice",
        "damage_class": "special",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "ohko",
                "url": "https://pokeapi.co/api/v2/move-category/9/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Causes a one-hit KO.",
        "flavor_text_entry": "A chilling attack that causes fainting if it hits."
    },
    "aqua-tail": {
        "name": "aqua-tail",
        "id": 401,
        "accuracy": 90,
        "priority": 0,
        "max_pp": 10,
        "power": 90,
        "type": "water",
        "damage_class": "physical",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Inflicts regular damage with no additional effect.",
        "flavor_text_entry": "The user attacks by swinging its tail as if it were a vicious wave in a raging storm. "
    },
    "frost-breath": {
        "name": "frost-breath",
        "id": 524,
        "accuracy": 90,
        "priority": 0,
        "max_pp": 10,
        "power": 60,
        "type": "ice",
        "damage_class": "special",
        "stat_changes": [],
        "effect_chance": 100,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 100,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 6,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Always scores a critical hit.",
        "flavor_text_entry": "The user blows a cold breath on the target. This attack always results in a critical hit."
    },
    "steel-roller": {
        "name": "steel-roller",
        "id": 798,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 5,
        "power": 130,
        "type": "steel",
        "damage_class": "physical",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Inflicts regular damage with no additional effect.",
        "flavor_text_entry": "The user attacks while destroying the terrain. This move fails when the ground hasn\u2019t turned into a terrain."
    },
    "icicle-spear": {
        "name": "icicle-spear",
        "id": 333,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 30,
        "power": 25,
        "type": "ice",
        "damage_class": "physical",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": 5,
            "max_turns": None,
            "min_hits": 2,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Hits 2-5 times in one turn.",
        "flavor_text_entry": "Attacks the foe by firing 2 to 5 icicles in a row."
    },
    "block": {
        "name": "block",
        "id": 335,
        "accuracy": None,
        "priority": 0,
        "max_pp": 5,
        "power": None,
        "type": "normal",
        "damage_class": "status",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "unique",
                "url": "https://pokeapi.co/api/v2/move-category/13/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Prevents the target from leaving battle.",
        "flavor_text_entry": "Blocks the foe\u2019s way to prevent escape."
    },
    "ice-fang": {
        "name": "ice-fang",
        "id": 423,
        "accuracy": 95,
        "priority": 0,
        "max_pp": 15,
        "power": 65,
        "type": "ice",
        "damage_class": "physical",
        "stat_changes": [],
        "effect_chance": 10,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "freeze",
                "url": "https://pokeapi.co/api/v2/move-ailment/3/"
            },
            "ailment_chance": 10,
            "category": {
                "name": "damage+ailment",
                "url": "https://pokeapi.co/api/v2/move-category/4/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 10,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Has a 10% chance to freeze the target and a 10% chance to make the target flinch.",
        "flavor_text_entry": "The user bites with cold-infused fangs. It may also make the foe flinch or freeze. "
    },
    "iron-head": {
        "name": "iron-head",
        "id": 442,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 15,
        "power": 80,
        "type": "steel",
        "damage_class": "physical",
        "stat_changes": [],
        "effect_chance": 30,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 30,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Has a 30% chance to make the target flinch.",
        "flavor_text_entry": "The foe slams the target with its steel-hard head. It may also make the target flinch."
    },
    "heavy-slam": {
        "name": "heavy-slam",
        "id": 484,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 10,
        "power": None,
        "type": "steel",
        "damage_class": "physical",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Power is higher when the user weighs more than the target, up to a maximum of 120.",
        "flavor_text_entry": "The user slams into the target with its heavy body. The more the user outweighs the target, the greater its damage."
    },
    "body-press": {
        "name": "body-press",
        "id": 776,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 10,
        "power": 80,
        "type": "fighting",
        "damage_class": "physical",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "flavor_text_entry": "The user attacks by slamming its body into the target. The higher the user\u2019s Defense, the more damage it can inflict on the target."
    },
    "flamethrower": {
        "name": "flamethrower",
        "id": 53,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 15,
        "power": 90,
        "type": "fire",
        "damage_class": "special",
        "stat_changes": [],
        "effect_chance": 10,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "burn",
                "url": "https://pokeapi.co/api/v2/move-ailment/4/"
            },
            "ailment_chance": 10,
            "category": {
                "name": "damage+ailment",
                "url": "https://pokeapi.co/api/v2/move-category/4/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Has a 10% chance to burn the target.",
        "flavor_text_entry": "An attack that may inflict a burn."
    },
    "fire-blast": {
        "name": "fire-blast",
        "id": 126,
        "accuracy": 85,
        "priority": 0,
        "max_pp": 5,
        "power": 110,
        "type": "fire",
        "damage_class": "special",
        "stat_changes": [],
        "effect_chance": 10,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "burn",
                "url": "https://pokeapi.co/api/v2/move-ailment/4/"
            },
            "ailment_chance": 10,
            "category": {
                "name": "damage+ailment",
                "url": "https://pokeapi.co/api/v2/move-category/4/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Has a 10% chance to burn the target.",
        "flavor_text_entry": "An attack that may cause a burn."
    },
    "amnesia": {
        "name": "amnesia",
        "id": 133,
        "accuracy": None,
        "priority": 0,
        "max_pp": 20,
        "power": None,
        "type": "psychic",
        "damage_class": "status",
        "stat_changes": [
            {
                "change": 2,
                "stat": {
                    "name": "SpDef",
                    "url": "https://pokeapi.co/api/v2/stat/5/"
                }
            }
        ],
        "effect_chance": None,
        "target": "user",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "net-good-stats",
                "url": "https://pokeapi.co/api/v2/move-category/2/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Raises the user's Special Defense by two stages.",
        "flavor_text_entry": "Sharply raises the user's SPCL.DEF."
    },
    "slack-off": {
        "name": "slack-off",
        "id": 303,
        "accuracy": None,
        "priority": 0,
        "max_pp": 5,
        "power": None,
        "type": "normal",
        "damage_class": "status",
        "stat_changes": [],
        "effect_chance": None,
        "target": "user",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "heal",
                "url": "https://pokeapi.co/api/v2/move-category/3/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 50,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Heals the user by half its max HP.",
        "flavor_text_entry": "Slacks off and restores half the maximum HP."
    },
    "crush-claw": {
        "name": "crush-claw",
        "id": 306,
        "accuracy": 95,
        "priority": 0,
        "max_pp": 10,
        "power": 75,
        "type": "normal",
        "damage_class": "physical",
        "stat_changes": [
            {
                "change": -1,
                "stat": {
                    "name": "Def",
                    "url": "https://pokeapi.co/api/v2/stat/3/"
                }
            }
        ],
        "effect_chance": 50,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage+lower",
                "url": "https://pokeapi.co/api/v2/move-category/6/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 50
        },
        "effect_entries": "Has a 50% chance to lower the target's Defense by one stage.",
        "flavor_text_entry": "Tears at the foe with sharp claws. May lower DEFENSE."
    },
    "tickle": {
        "name": "tickle",
        "id": 321,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 20,
        "power": None,
        "type": "normal",
        "damage_class": "status",
        "stat_changes": [
            {
                "change": -1,
                "stat": {
                    "name": "Atk",
                    "url": "https://pokeapi.co/api/v2/stat/2/"
                }
            },
            {
                "change": -1,
                "stat": {
                    "name": "Def",
                    "url": "https://pokeapi.co/api/v2/stat/3/"
                }
            }
        ],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "net-good-stats",
                "url": "https://pokeapi.co/api/v2/move-category/2/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Lowers the target's Attack and Defense by one stage.",
        "flavor_text_entry": "Makes the foe laugh to lower ATTACK and DEFENSE."
    },
    "sucker-punch": {
        "name": "sucker-punch",
        "id": 389,
        "accuracy": 100,
        "priority": 1,
        "max_pp": 5,
        "power": 70,
        "type": "dark",
        "damage_class": "physical",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Only works if the target is about to use a damaging move.",
        "flavor_text_entry": "This move enables the user to attack first. It fails if the foe is not readying an attack, however."
    },
    "poison-jab": {
        "name": "poison-jab",
        "id": 398,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 20,
        "power": 80,
        "type": "poison",
        "damage_class": "physical",
        "stat_changes": [],
        "effect_chance": 30,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "poison",
                "url": "https://pokeapi.co/api/v2/move-ailment/5/"
            },
            "ailment_chance": 30,
            "category": {
                "name": "damage+ailment",
                "url": "https://pokeapi.co/api/v2/move-category/4/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Has a 30% chance to poison the target.",
        "flavor_text_entry": "The foe is stabbed with a tentacle or arm steeped in poison. It may also poison the foe."
    },
    "x-scissor": {
        "name": "x-scissor",
        "id": 404,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 15,
        "power": 80,
        "type": "bug",
        "damage_class": "physical",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Inflicts regular damage with no additional effect.",
        "flavor_text_entry": "The user slashes at the foe by crossing its scythes or claws as if they were a pair of scissors."
    },
    "after-you": {
        "name": "after-you",
        "id": 495,
        "accuracy": None,
        "priority": 0,
        "max_pp": 15,
        "power": None,
        "type": "normal",
        "damage_class": "status",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "unique",
                "url": "https://pokeapi.co/api/v2/move-category/13/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Makes the target act next this turn.",
        "flavor_text_entry": "The user helps the target and makes it use its move right after the user."
    },
    "incinerate": {
        "name": "incinerate",
        "id": 510,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 15,
        "power": 60,
        "type": "fire",
        "damage_class": "special",
        "stat_changes": [],
        "effect_chance": None,
        "target": "all-opponents",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Destroys the target's held berry.",
        "flavor_text_entry": "The user attacks the target with fire. If the target is holding a Berry, the Berry becomes burnt up and unusable."
    },
    "reversal": {
        "name": "reversal",
        "id": 179,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 15,
        "power": None,
        "type": "fighting",
        "damage_class": "physical",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Inflicts more damage when the user has less HP remaining, with a maximum of 200 power.",
        "flavor_text_entry": "Stronger if the user's HP is low."
    },
    "outrage": {
        "name": "outrage",
        "id": 200,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 10,
        "power": 120,
        "type": "dragon",
        "damage_class": "physical",
        "stat_changes": [],
        "effect_chance": None,
        "target": "random-opponent",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": 3,
            "min_hits": None,
            "min_turns": 2,
            "stat_chance": 0
        },
        "effect_entries": "Hits every turn for 2-3 turns, then confuses the user.",
        "flavor_text_entry": "Works 2-3 turns and confuses user."
    },
    "drain-punch": {
        "name": "drain-punch",
        "id": 409,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 10,
        "power": 75,
        "type": "fighting",
        "damage_class": "physical",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage+heal",
                "url": "https://pokeapi.co/api/v2/move-category/8/"
            },
            "crit_rate": 0,
            "drain": 50,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Drains half the damage inflicted to heal the user.",
        "flavor_text_entry": "An energy-draining punch. The user\u2019s HP is restored by half the damage taken by the target."
    },
    "low-sweep": {
        "name": "low-sweep",
        "id": 490,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 20,
        "power": 65,
        "type": "fighting",
        "damage_class": "physical",
        "stat_changes": [
            {
                "change": -1,
                "stat": {
                    "name": "Speed",
                    "url": "https://pokeapi.co/api/v2/stat/6/"
                }
            }
        ],
        "effect_chance": 100,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage+lower",
                "url": "https://pokeapi.co/api/v2/move-category/6/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 100
        },
        "effect_entries": "Lowers the target's Speed by one stage.",
        "flavor_text_entry": "The user attacks the target\u2019s legs swiftly, reducing the target\u2019s Speed stat."
    },
    "lash-out": {
        "name": "lash-out",
        "id": 808,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 5,
        "power": 75,
        "type": "dark",
        "damage_class": "physical",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Inflicts regular damage with no additional effect.",
        "flavor_text_entry": "The user lashes out to vent its frustration toward the target. If the user\u2019s stats were lowered during this turn, the power of this move is doubled."
    },
    "punishment": {
        "name": "punishment",
        "id": 386,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 5,
        "power": None,
        "type": "dark",
        "damage_class": "physical",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Power increases against targets with more raised stats, up to a maximum of 200.",
        "flavor_text_entry": "This attack\u2019s power increases the more the foe has powered up with stat changes. "
    },
    "quash": {
        "name": "quash",
        "id": 511,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 15,
        "power": None,
        "type": "dark",
        "damage_class": "status",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "unique",
                "url": "https://pokeapi.co/api/v2/move-category/13/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Makes the target act last this turn.",
        "flavor_text_entry": "The user suppresses the target and makes its move go last."
    },
    "pounce": {
        "name": "pounce",
        "id": 884,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 20,
        "power": 50,
        "type": "bug",
        "damage_class": "physical",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": None
    },
    "hard-press": {
        "name": "hard-press",
        "id": 912,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 10,
        "power": 0,
        "type": "steel",
        "damage_class": "physical",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": None
    },
    "absorb": {
        "name": "absorb",
        "id": 71,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 25,
        "power": 20,
        "type": "grass",
        "damage_class": "special",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage+heal",
                "url": "https://pokeapi.co/api/v2/move-category/8/"
            },
            "crit_rate": 0,
            "drain": 50,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Drains half the damage inflicted to heal the user.",
        "flavor_text_entry": "Steals 1/2 of the damage inflicted."
    },
    "mega-drain": {
        "name": "mega-drain",
        "id": 72,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 15,
        "power": 40,
        "type": "grass",
        "damage_class": "special",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage+heal",
                "url": "https://pokeapi.co/api/v2/move-category/8/"
            },
            "crit_rate": 0,
            "drain": 50,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Drains half the damage inflicted to heal the user.",
        "flavor_text_entry": "Steals 1/2 of the damage inflicted."
    },
    "growth": {
        "name": "growth",
        "id": 74,
        "accuracy": None,
        "priority": 0,
        "max_pp": 20,
        "power": None,
        "type": "normal",
        "damage_class": "status",
        "stat_changes": [
            {
                "change": 1,
                "stat": {
                    "name": "Atk",
                    "url": "https://pokeapi.co/api/v2/stat/2/"
                }
            },
            {
                "change": 1,
                "stat": {
                    "name": "SpAtk",
                    "url": "https://pokeapi.co/api/v2/stat/4/"
                }
            }
        ],
        "effect_chance": None,
        "target": "user",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "net-good-stats",
                "url": "https://pokeapi.co/api/v2/move-category/2/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Raises the user's Attack and Special Attack by one stage.",
        "flavor_text_entry": "Raises the SPCL. ATK rating."
    },
    "poison-powder": {
        "name": "poison-powder",
        "id": 77,
        "accuracy": 75,
        "priority": 0,
        "max_pp": 35,
        "power": None,
        "type": "poison",
        "damage_class": "status",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "poison",
                "url": "https://pokeapi.co/api/v2/move-ailment/5/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "ailment",
                "url": "https://pokeapi.co/api/v2/move-category/1/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Poisons the target.",
        "flavor_text_entry": "A move that may poison the foe."
    },
    "stun-spore": {
        "name": "stun-spore",
        "id": 78,
        "accuracy": 75,
        "priority": 0,
        "max_pp": 30,
        "power": None,
        "type": "grass",
        "damage_class": "status",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "paralysis",
                "url": "https://pokeapi.co/api/v2/move-ailment/1/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "ailment",
                "url": "https://pokeapi.co/api/v2/move-category/1/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Paralyzes the target.",
        "flavor_text_entry": "A move that may paralyze the foe."
    },
    "sleep-powder": {
        "name": "sleep-powder",
        "id": 79,
        "accuracy": 75,
        "priority": 0,
        "max_pp": 15,
        "power": None,
        "type": "grass",
        "damage_class": "status",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "sleep",
                "url": "https://pokeapi.co/api/v2/move-ailment/2/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "ailment",
                "url": "https://pokeapi.co/api/v2/move-category/1/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": 4,
            "min_hits": None,
            "min_turns": 2,
            "stat_chance": 0
        },
        "effect_entries": "Puts the target to sleep.",
        "flavor_text_entry": "May cause the foe to fall asleep."
    },
    "string-shot": {
        "name": "string-shot",
        "id": 81,
        "accuracy": 95,
        "priority": 0,
        "max_pp": 40,
        "power": None,
        "type": "bug",
        "damage_class": "status",
        "stat_changes": [
            {
                "change": -2,
                "stat": {
                    "name": "Speed",
                    "url": "https://pokeapi.co/api/v2/stat/6/"
                }
            }
        ],
        "effect_chance": None,
        "target": "all-opponents",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "net-good-stats",
                "url": "https://pokeapi.co/api/v2/move-category/2/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Lowers the target's Speed by two stages.",
        "flavor_text_entry": "A move that lowers the foe's SPEED."
    },
    "screech": {
        "name": "screech",
        "id": 103,
        "accuracy": 85,
        "priority": 0,
        "max_pp": 40,
        "power": None,
        "type": "normal",
        "damage_class": "status",
        "stat_changes": [
            {
                "change": -2,
                "stat": {
                    "name": "Def",
                    "url": "https://pokeapi.co/api/v2/stat/3/"
                }
            }
        ],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "net-good-stats",
                "url": "https://pokeapi.co/api/v2/move-category/2/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Lowers the target's Defense by two stages.",
        "flavor_text_entry": "An earsplitting screech harshly lowers the target\u2019s Defense stat."
    },
    "leech-life": {
        "name": "leech-life",
        "id": 141,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 10,
        "power": 80,
        "type": "bug",
        "damage_class": "physical",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage+heal",
                "url": "https://pokeapi.co/api/v2/move-category/8/"
            },
            "crit_rate": 0,
            "drain": 50,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Drains half the damage inflicted to heal the user.",
        "flavor_text_entry": "Steals 1/2 of the damage inflicted."
    },
    "spore": {
        "name": "spore",
        "id": 147,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 15,
        "power": None,
        "type": "grass",
        "damage_class": "status",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "sleep",
                "url": "https://pokeapi.co/api/v2/move-ailment/2/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "ailment",
                "url": "https://pokeapi.co/api/v2/move-category/1/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": 4,
            "min_hits": None,
            "min_turns": 2,
            "stat_chance": 0
        },
        "effect_entries": "Puts the target to sleep.",
        "flavor_text_entry": "The user scatters bursts of spores that induce sleep."
    },
    "sludge-bomb": {
        "name": "sludge-bomb",
        "id": 188,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 10,
        "power": 90,
        "type": "poison",
        "damage_class": "special",
        "stat_changes": [],
        "effect_chance": 30,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "poison",
                "url": "https://pokeapi.co/api/v2/move-ailment/5/"
            },
            "ailment_chance": 30,
            "category": {
                "name": "damage+ailment",
                "url": "https://pokeapi.co/api/v2/move-category/4/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Has a 30% chance to poison the target.",
        "flavor_text_entry": "An attack that may poison the foe."
    },
    "cross-poison": {
        "name": "cross-poison",
        "id": 440,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 20,
        "power": 70,
        "type": "poison",
        "damage_class": "physical",
        "stat_changes": [],
        "effect_chance": 10,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "poison",
                "url": "https://pokeapi.co/api/v2/move-ailment/5/"
            },
            "ailment_chance": 10,
            "category": {
                "name": "damage+ailment",
                "url": "https://pokeapi.co/api/v2/move-category/4/"
            },
            "crit_rate": 1,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Has an increased chance for a critical hit and a 10% chance to poison the target.",
        "flavor_text_entry": "A slashing attack that may also leave the target poisoned. It has a high critical-hit ratio."
    },
    "bug-bite": {
        "name": "bug-bite",
        "id": 450,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 20,
        "power": 60,
        "type": "bug",
        "damage_class": "physical",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "If target has a berry, inflicts double damage and uses the berry.",
        "flavor_text_entry": "The user bites the foe. If the foe is holding a Berry, the user eats it and gains its effect."
    },
    "venoshock": {
        "name": "venoshock",
        "id": 474,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 10,
        "power": 65,
        "type": "poison",
        "damage_class": "special",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Inflicts double damage if the target is Poisoned.",
        "flavor_text_entry": "The user drenches the target in a special poisonous liquid. Its power is doubled if the target is poisoned."
    },
    "rage-powder": {
        "name": "rage-powder",
        "id": 476,
        "accuracy": None,
        "priority": 2,
        "max_pp": 20,
        "power": None,
        "type": "bug",
        "damage_class": "status",
        "stat_changes": [],
        "effect_chance": None,
        "target": "user",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "unique",
                "url": "https://pokeapi.co/api/v2/move-category/13/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Redirects the target's single-target effects to the user for this turn.",
        "flavor_text_entry": "The user scatters a cloud of irritating powder to draw attention to itself. Opponents aim only at the user."
    },
    "struggle-bug": {
        "name": "struggle-bug",
        "id": 522,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 20,
        "power": 50,
        "type": "bug",
        "damage_class": "special",
        "stat_changes": [
            {
                "change": -1,
                "stat": {
                    "name": "SpAtk",
                    "url": "https://pokeapi.co/api/v2/stat/4/"
                }
            }
        ],
        "effect_chance": 100,
        "target": "all-opponents",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage+lower",
                "url": "https://pokeapi.co/api/v2/move-category/6/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 100
        },
        "effect_entries": "Has a 100% chance to lower the target's Special Attack by one stage.",
        "flavor_text_entry": "While resisting, the user attacks the opposing Pok\u00e9mon. The targets\u2019 Sp. Atk stat is reduced."
    },
    "rototiller": {
        "name": "rototiller",
        "id": 563,
        "accuracy": None,
        "priority": 0,
        "max_pp": 10,
        "power": None,
        "type": "ground",
        "damage_class": "status",
        "stat_changes": [
            {
                "change": 1,
                "stat": {
                    "name": "Atk",
                    "url": "https://pokeapi.co/api/v2/stat/2/"
                }
            },
            {
                "change": 1,
                "stat": {
                    "name": "SpAtk",
                    "url": "https://pokeapi.co/api/v2/stat/4/"
                }
            }
        ],
        "effect_chance": 100,
        "target": "all-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "net-good-stats",
                "url": "https://pokeapi.co/api/v2/move-category/2/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 100
        },
        "effect_entries": "Raises the Attack and Special Attack of all grass Pok\u00e9mon in.",
        "flavor_text_entry": "Tilling the soil, the user makes it easier for plants to grow. This raises the Attack and Sp. Atk stats of Grass-type Pok\u00e9mon."
    },
    "fell-stinger": {
        "name": "fell-stinger",
        "id": 565,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 25,
        "power": 50,
        "type": "bug",
        "damage_class": "physical",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Raises the user's Attack by two stages if it KOs the target.",
        "flavor_text_entry": "When the user knocks out a target with this move, the user\u2019s Attack stat rises sharply."
    },
    "bind": {
        "name": "bind",
        "id": 20,
        "accuracy": 85,
        "priority": 0,
        "max_pp": 20,
        "power": 15,
        "type": "normal",
        "damage_class": "physical",
        "stat_changes": [],
        "effect_chance": 100,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "trap",
                "url": "https://pokeapi.co/api/v2/move-ailment/8/"
            },
            "ailment_chance": 100,
            "category": {
                "name": "damage+ailment",
                "url": "https://pokeapi.co/api/v2/move-category/4/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": 6,
            "min_hits": None,
            "min_turns": 5,
            "stat_chance": 0
        },
        "effect_entries": "Prevents the target from fleeing and inflicts damage for 2-5 turns.",
        "flavor_text_entry": "Binds the target for 2-5 turns."
    },
    "disable": {
        "name": "disable",
        "id": 50,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 20,
        "power": None,
        "type": "normal",
        "damage_class": "status",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "disable",
                "url": "https://pokeapi.co/api/v2/move-ailment/13/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "unique",
                "url": "https://pokeapi.co/api/v2/move-category/13/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": 4,
            "min_hits": None,
            "min_turns": 4,
            "stat_chance": 0
        },
        "effect_entries": "Disables the target's last used move for 1-8 turns.",
        "flavor_text_entry": "For four turns, this move prevents the target from using the move it last used."
    },
    "dizzy-punch": {
        "name": "dizzy-punch",
        "id": 146,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 10,
        "power": 70,
        "type": "normal",
        "damage_class": "physical",
        "stat_changes": [],
        "effect_chance": 20,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "confusion",
                "url": "https://pokeapi.co/api/v2/move-ailment/6/"
            },
            "ailment_chance": 20,
            "category": {
                "name": "damage+ailment",
                "url": "https://pokeapi.co/api/v2/move-category/4/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": 5,
            "min_hits": None,
            "min_turns": 2,
            "stat_chance": 0
        },
        "effect_entries": "Has a 20% chance to confuse the target.",
        "flavor_text_entry": "An attack that may cause confusion."
    },
    "detect": {
        "name": "detect",
        "id": 197,
        "accuracy": None,
        "priority": 4,
        "max_pp": 5,
        "power": None,
        "type": "fighting",
        "damage_class": "status",
        "stat_changes": [],
        "effect_chance": None,
        "target": "user",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "unique",
                "url": "https://pokeapi.co/api/v2/move-category/13/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Prevents any moves from hitting the user this turn.",
        "flavor_text_entry": "Evades attack that turn. It may fail."
    },
    "ancient-power": {
        "name": "ancient-power",
        "id": 246,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 5,
        "power": 60,
        "type": "rock",
        "damage_class": "special",
        "stat_changes": [
            {
                "change": 1,
                "stat": {
                    "name": "Atk",
                    "url": "https://pokeapi.co/api/v2/stat/2/"
                }
            },
            {
                "change": 1,
                "stat": {
                    "name": "Def",
                    "url": "https://pokeapi.co/api/v2/stat/3/"
                }
            },
            {
                "change": 1,
                "stat": {
                    "name": "SpAtk",
                    "url": "https://pokeapi.co/api/v2/stat/4/"
                }
            },
            {
                "change": 1,
                "stat": {
                    "name": "SpDef",
                    "url": "https://pokeapi.co/api/v2/stat/5/"
                }
            },
            {
                "change": 1,
                "stat": {
                    "name": "Speed",
                    "url": "https://pokeapi.co/api/v2/stat/6/"
                }
            }
        ],
        "effect_chance": 10,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage+raise",
                "url": "https://pokeapi.co/api/v2/move-category/7/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 10
        },
        "effect_entries": "Has a 10% chance to raise all of the user's stats by one stage.",
        "flavor_text_entry": "An attack that may raise all stats."
    },
    "fake-out": {
        "name": "fake-out",
        "id": 252,
        "accuracy": 100,
        "priority": 3,
        "max_pp": 10,
        "power": 40,
        "type": "normal",
        "damage_class": "physical",
        "stat_changes": [],
        "effect_chance": 100,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 100,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Can only be used as the first move after the user enters battle.  Causes the target to flinch.",
        "flavor_text_entry": "A 1st-turn, 1st-strike move that causes flinching."
    },
    "role-play": {
        "name": "role-play",
        "id": 272,
        "accuracy": None,
        "priority": 0,
        "max_pp": 10,
        "power": None,
        "type": "psychic",
        "damage_class": "status",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "unique",
                "url": "https://pokeapi.co/api/v2/move-category/13/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Copies the target's ability.",
        "flavor_text_entry": "Mimics the target and copies its special ability."
    },
    "snatch": {
        "name": "snatch",
        "id": 289,
        "accuracy": None,
        "priority": 4,
        "max_pp": 10,
        "power": None,
        "type": "dark",
        "damage_class": "status",
        "stat_changes": [],
        "effect_chance": None,
        "target": "user",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "unique",
                "url": "https://pokeapi.co/api/v2/move-category/13/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Steals the target's move, if it's self-targeted.",
        "flavor_text_entry": "Steals the effects of the move the foe uses next."
    },
    "astonish": {
        "name": "astonish",
        "id": 310,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 15,
        "power": 30,
        "type": "ghost",
        "damage_class": "physical",
        "stat_changes": [],
        "effect_chance": 30,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 30,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Has a 30% chance to make the target flinch.",
        "flavor_text_entry": "An attack that may shock the foe into flinching."
    },
    "feint": {
        "name": "feint",
        "id": 364,
        "accuracy": 100,
        "priority": 2,
        "max_pp": 10,
        "power": 30,
        "type": "normal",
        "damage_class": "physical",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Hits through Protect and Detect.",
        "flavor_text_entry": "An attack that hits a foe using Protect or Detect. It also lifts the effects of those moves."
    },
    "nasty-plot": {
        "name": "nasty-plot",
        "id": 417,
        "accuracy": None,
        "priority": 0,
        "max_pp": 20,
        "power": None,
        "type": "dark",
        "damage_class": "status",
        "stat_changes": [
            {
                "change": 2,
                "stat": {
                    "name": "SpAtk",
                    "url": "https://pokeapi.co/api/v2/stat/4/"
                }
            }
        ],
        "effect_chance": None,
        "target": "user",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "net-good-stats",
                "url": "https://pokeapi.co/api/v2/move-category/2/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Raises the user's Special Attack by two stages.",
        "flavor_text_entry": "The user stimulates its brain by thinking bad thoughts. It sharply raises the user\u2019s Sp. Atk."
    },
    "shadow-sneak": {
        "name": "shadow-sneak",
        "id": 425,
        "accuracy": 100,
        "priority": 1,
        "max_pp": 30,
        "power": 40,
        "type": "ghost",
        "damage_class": "physical",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Inflicts regular damage with no additional effect.",
        "flavor_text_entry": "The user extends its shadow and attacks the foe from behind. This move always goes first."
    },
    "stealth-rock": {
        "name": "stealth-rock",
        "id": 446,
        "accuracy": None,
        "priority": 0,
        "max_pp": 20,
        "power": None,
        "type": "rock",
        "damage_class": "status",
        "stat_changes": [],
        "effect_chance": None,
        "target": "opponents-field",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "field-effect",
                "url": "https://pokeapi.co/api/v2/move-category/11/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Causes damage when opposing Pok\u00e9mon switch in.",
        "flavor_text_entry": "The user lays a trap of levitating stones around the foe. The trap hurts foes that switch into battle."
    },
    "synchronoise": {
        "name": "synchronoise",
        "id": 485,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 10,
        "power": 120,
        "type": "psychic",
        "damage_class": "special",
        "stat_changes": [],
        "effect_chance": None,
        "target": "all-other-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Hits any Pok\u00e9mon that shares a type with the user.",
        "flavor_text_entry": "Using an odd shock wave, the user inflicts damage on any Pok\u00e9mon of the same type in the area around it."
    },
    "foul-play": {
        "name": "foul-play",
        "id": 492,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 15,
        "power": 95,
        "type": "dark",
        "damage_class": "physical",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Calculates damage with the target's attacking stat.",
        "flavor_text_entry": "The user turns the target\u2019s power against it. The higher the target\u2019s Attack stat, the greater the damage."
    },
    "sonic-boom": {
        "name": "sonic-boom",
        "id": 49,
        "accuracy": 90,
        "priority": 0,
        "max_pp": 20,
        "power": None,
        "type": "normal",
        "damage_class": "special",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Inflicts 20 points of damage.",
        "flavor_text_entry": "Always inflicts 20HP damage."
    },
    "explosion": {
        "name": "explosion",
        "id": 153,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 5,
        "power": 250,
        "type": "normal",
        "damage_class": "physical",
        "stat_changes": [],
        "effect_chance": None,
        "target": "all-other-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "User faints.",
        "flavor_text_entry": "Inflicts severe damage but makes the user faint."
    },
    "lock-on": {
        "name": "lock-on",
        "id": 199,
        "accuracy": None,
        "priority": 0,
        "max_pp": 5,
        "power": None,
        "type": "normal",
        "damage_class": "status",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "unique",
                "url": "https://pokeapi.co/api/v2/move-category/13/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Ensures that the user's next move will hit the target.",
        "flavor_text_entry": "Ensures the next attack will hit."
    },
    "sandstorm": {
        "name": "sandstorm",
        "id": 201,
        "accuracy": None,
        "priority": 0,
        "max_pp": 10,
        "power": None,
        "type": "rock",
        "damage_class": "status",
        "stat_changes": [],
        "effect_chance": None,
        "target": "entire-field",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "whole-field-effect",
                "url": "https://pokeapi.co/api/v2/move-category/10/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Changes the weather to a sandstorm for five turns.",
        "flavor_text_entry": "Inflicts damage every turn."
    },
    "metal-sound": {
        "name": "metal-sound",
        "id": 319,
        "accuracy": 85,
        "priority": 0,
        "max_pp": 40,
        "power": None,
        "type": "steel",
        "damage_class": "status",
        "stat_changes": [
            {
                "change": -2,
                "stat": {
                    "name": "SpDef",
                    "url": "https://pokeapi.co/api/v2/stat/5/"
                }
            }
        ],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "net-good-stats",
                "url": "https://pokeapi.co/api/v2/move-category/2/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Lowers the target's Special Defense by two stages.",
        "flavor_text_entry": "Emits a horrible screech that sharply lowers SP. DEF."
    },
    "iron-defense": {
        "name": "iron-defense",
        "id": 334,
        "accuracy": None,
        "priority": 0,
        "max_pp": 15,
        "power": None,
        "type": "steel",
        "damage_class": "status",
        "stat_changes": [
            {
                "change": 2,
                "stat": {
                    "name": "Def",
                    "url": "https://pokeapi.co/api/v2/stat/3/"
                }
            }
        ],
        "effect_chance": None,
        "target": "user",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "net-good-stats",
                "url": "https://pokeapi.co/api/v2/move-category/2/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Raises the user's Defense by two stages.",
        "flavor_text_entry": "Hardens the body\u2019s surface to sharply raise DEFENSE."
    },
    "mirror-shot": {
        "name": "mirror-shot",
        "id": 429,
        "accuracy": 85,
        "priority": 0,
        "max_pp": 10,
        "power": 65,
        "type": "steel",
        "damage_class": "special",
        "stat_changes": [
            {
                "change": -1,
                "stat": {
                    "name": "accuracy",
                    "url": "https://pokeapi.co/api/v2/stat/7/"
                }
            }
        ],
        "effect_chance": 30,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage+lower",
                "url": "https://pokeapi.co/api/v2/move-category/6/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 30
        },
        "effect_entries": "Has a 30% chance to lower the target's accuracy by one stage.",
        "flavor_text_entry": "The user looses a flash of energy from its polished body. It may also lower the target\u2019s accuracy."
    },
    "magnet-bomb": {
        "name": "magnet-bomb",
        "id": 443,
        "accuracy": None,
        "priority": 0,
        "max_pp": 20,
        "power": 60,
        "type": "steel",
        "damage_class": "physical",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Never misses.",
        "flavor_text_entry": "The user launches a steel bomb that sticks to the target. This attack will not miss."
    },
    "steel-beam": {
        "name": "steel-beam",
        "id": 796,
        "accuracy": 95,
        "priority": 0,
        "max_pp": 5,
        "power": 140,
        "type": "steel",
        "damage_class": "special",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Inflicts damage, and the user takes damage equal to half of its max HP, rounded up.",
        "flavor_text_entry": "The user fires a beam of steel that it collected from its entire body. This also damages the user."
    },
    "rising-voltage": {
        "name": "rising-voltage",
        "id": 804,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 20,
        "power": 70,
        "type": "electric",
        "damage_class": "special",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Inflicts regular damage with no additional effect.",
        "flavor_text_entry": "The user attacks with electric voltage rising from the ground. This move\u2019s power doubles when the target is on Electric Terrain."
    },
    "self-destruct": {
        "name": "self-destruct",
        "id": 120,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 5,
        "power": 200,
        "type": "normal",
        "damage_class": "physical",
        "stat_changes": [],
        "effect_chance": None,
        "target": "all-other-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "User faints.",
        "flavor_text_entry": "Powerful but makes the user faint."
    },
    "mirror-coat": {
        "name": "mirror-coat",
        "id": 243,
        "accuracy": 100,
        "priority": -5,
        "max_pp": 20,
        "power": None,
        "type": "psychic",
        "damage_class": "special",
        "stat_changes": [],
        "effect_chance": None,
        "target": "specific-move",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Inflicts twice the damage the user received from the last special hit it took.",
        "flavor_text_entry": "Counters a SPCL. ATK. move double."
    },
    "magnetic-flux": {
        "name": "magnetic-flux",
        "id": 602,
        "accuracy": None,
        "priority": 0,
        "max_pp": 20,
        "power": None,
        "type": "electric",
        "damage_class": "status",
        "stat_changes": [
            {
                "change": 1,
                "stat": {
                    "name": "Def",
                    "url": "https://pokeapi.co/api/v2/stat/3/"
                }
            },
            {
                "change": 1,
                "stat": {
                    "name": "SpDef",
                    "url": "https://pokeapi.co/api/v2/stat/5/"
                }
            }
        ],
        "effect_chance": None,
        "target": "user-and-allies",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "net-good-stats",
                "url": "https://pokeapi.co/api/v2/move-category/2/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Raises the Defense and Special Defense of all friendly Pok\u00e9mon with plus or minus by one stage.",
        "flavor_text_entry": "The user manipulates magnetic fields, which raises the Defense and Sp. Def stats of ally Pok\u00e9mon with the Plus or Minus Ability."
    },
    "supercell-slam": {
        "name": "supercell-slam",
        "id": 916,
        "accuracy": 95,
        "priority": 0,
        "max_pp": 15,
        "power": 100,
        "type": "electric",
        "damage_class": "physical",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": None
    },
    "pound": {
        "name": "pound",
        "id": 1,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 35,
        "power": 40,
        "type": "normal",
        "damage_class": "physical",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Inflicts regular damage with no additional effect.",
        "flavor_text_entry": "Pounds with fore\u00ad legs or tail."
    },
    "double-slap": {
        "name": "double-slap",
        "id": 3,
        "accuracy": 85,
        "priority": 0,
        "max_pp": 10,
        "power": 15,
        "type": "normal",
        "damage_class": "physical",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": 5,
            "max_turns": None,
            "min_hits": 2,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Hits 2-5 times in one turn.",
        "flavor_text_entry": "Repeatedly slaps 2-5 times."
    },
    "haze": {
        "name": "haze",
        "id": 114,
        "accuracy": None,
        "priority": 0,
        "max_pp": 30,
        "power": None,
        "type": "ice",
        "damage_class": "status",
        "stat_changes": [],
        "effect_chance": None,
        "target": "entire-field",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "whole-field-effect",
                "url": "https://pokeapi.co/api/v2/move-category/10/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Resets all Pok\u00e9mon's stats, accuracy, and evasion.",
        "flavor_text_entry": "Eliminates all stat changes."
    },
    "sludge": {
        "name": "sludge",
        "id": 124,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 20,
        "power": 65,
        "type": "poison",
        "damage_class": "special",
        "stat_changes": [],
        "effect_chance": 30,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "poison",
                "url": "https://pokeapi.co/api/v2/move-ailment/5/"
            },
            "ailment_chance": 30,
            "category": {
                "name": "damage+ailment",
                "url": "https://pokeapi.co/api/v2/move-category/4/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Has a 30% chance to poison the target.",
        "flavor_text_entry": "An attack that may poison the foe."
    },
    "poison-gas": {
        "name": "poison-gas",
        "id": 139,
        "accuracy": 90,
        "priority": 0,
        "max_pp": 40,
        "power": None,
        "type": "poison",
        "damage_class": "status",
        "stat_changes": [],
        "effect_chance": None,
        "target": "all-opponents",
        "meta": {
            "ailment": {
                "name": "poison",
                "url": "https://pokeapi.co/api/v2/move-ailment/5/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "ailment",
                "url": "https://pokeapi.co/api/v2/move-category/1/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Poisons the target.",
        "flavor_text_entry": "A move that may poison the foe."
    },
    "spite": {
        "name": "spite",
        "id": 180,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 10,
        "power": None,
        "type": "ghost",
        "damage_class": "status",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "unique",
                "url": "https://pokeapi.co/api/v2/move-category/13/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Lowers the PP of the target's last used move by 4.",
        "flavor_text_entry": "Cuts the PP of the foe's last move."
    },
    "spikes": {
        "name": "spikes",
        "id": 191,
        "accuracy": None,
        "priority": 0,
        "max_pp": 20,
        "power": None,
        "type": "ground",
        "damage_class": "status",
        "stat_changes": [],
        "effect_chance": None,
        "target": "opponents-field",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "field-effect",
                "url": "https://pokeapi.co/api/v2/move-category/11/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Scatters Spikes, hurting opposing Pok\u00e9mon that switch in.",
        "flavor_text_entry": "Hurts foes when they switch out."
    },
    "mud-sport": {
        "name": "mud-sport",
        "id": 300,
        "accuracy": None,
        "priority": 0,
        "max_pp": 15,
        "power": None,
        "type": "ground",
        "damage_class": "status",
        "stat_changes": [],
        "effect_chance": None,
        "target": "entire-field",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "whole-field-effect",
                "url": "https://pokeapi.co/api/v2/move-category/10/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Halves all Electric-type damage.",
        "flavor_text_entry": "Covers the user in mud to raise electrical resistance."
    },
    "rock-blast": {
        "name": "rock-blast",
        "id": 350,
        "accuracy": 90,
        "priority": 0,
        "max_pp": 10,
        "power": 25,
        "type": "rock",
        "damage_class": "physical",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": 5,
            "max_turns": None,
            "min_hits": 2,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Hits 2-5 times in one turn.",
        "flavor_text_entry": "Hurls boulders at the foe 2 to 5 times in a row."
    },
    "toxic-spikes": {
        "name": "toxic-spikes",
        "id": 390,
        "accuracy": None,
        "priority": 0,
        "max_pp": 20,
        "power": None,
        "type": "poison",
        "damage_class": "status",
        "stat_changes": [],
        "effect_chance": None,
        "target": "opponents-field",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "field-effect",
                "url": "https://pokeapi.co/api/v2/move-category/11/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Scatters poisoned spikes, poisoning opposing Pok\u00e9mon that switch in.",
        "flavor_text_entry": "The user lays a trap of poison spikes at the foe\u2019s feet. They poison foes that switch into battle."
    },
    "dark-pulse": {
        "name": "dark-pulse",
        "id": 399,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 15,
        "power": 80,
        "type": "dark",
        "damage_class": "special",
        "stat_changes": [],
        "effect_chance": 20,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 20,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Has a 20% chance to make the target flinch.",
        "flavor_text_entry": "The user releases a horrible aura imbued with dark thoughts. It may also make the target flinch."
    },
    "autotomize": {
        "name": "autotomize",
        "id": 475,
        "accuracy": None,
        "priority": 0,
        "max_pp": 15,
        "power": None,
        "type": "steel",
        "damage_class": "status",
        "stat_changes": [
            {
                "change": 2,
                "stat": {
                    "name": "Speed",
                    "url": "https://pokeapi.co/api/v2/stat/6/"
                }
            }
        ],
        "effect_chance": None,
        "target": "user",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "net-good-stats",
                "url": "https://pokeapi.co/api/v2/move-category/2/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Raises the user's Speed by two stages and halves the user's weight.",
        "flavor_text_entry": "The user sheds part of its body to make itself lighter and sharply raise its Speed stat."
    },
    "sludge-wave": {
        "name": "sludge-wave",
        "id": 482,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 10,
        "power": 95,
        "type": "poison",
        "damage_class": "special",
        "stat_changes": [],
        "effect_chance": 10,
        "target": "all-other-pokemon",
        "meta": {
            "ailment": {
                "name": "poison",
                "url": "https://pokeapi.co/api/v2/move-ailment/5/"
            },
            "ailment_chance": 10,
            "category": {
                "name": "damage+ailment",
                "url": "https://pokeapi.co/api/v2/move-category/4/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Has a 10% chance to poison the target.",
        "flavor_text_entry": "It swamps the area around the user with a giant sludge wave. It may also poison those hit."
    },
    "acid-spray": {
        "name": "acid-spray",
        "id": 491,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 20,
        "power": 40,
        "type": "poison",
        "damage_class": "special",
        "stat_changes": [
            {
                "change": -2,
                "stat": {
                    "name": "SpDef",
                    "url": "https://pokeapi.co/api/v2/stat/5/"
                }
            }
        ],
        "effect_chance": 100,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage+lower",
                "url": "https://pokeapi.co/api/v2/move-category/6/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 100
        },
        "effect_entries": "Lowers the target's Special Defense by two stages.",
        "flavor_text_entry": "The user spits fluid that works to melt the target. This harshly reduces the target\u2019s Sp. Def stat."
    },
    "clear-smog": {
        "name": "clear-smog",
        "id": 499,
        "accuracy": None,
        "priority": 0,
        "max_pp": 15,
        "power": 50,
        "type": "poison",
        "damage_class": "special",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Removes all of the target's stat modifiers.",
        "flavor_text_entry": "The user attacks by throwing a clump of special mud. All status changes are returned to normal."
    },
    "belch": {
        "name": "belch",
        "id": 562,
        "accuracy": 90,
        "priority": 0,
        "max_pp": 10,
        "power": 120,
        "type": "poison",
        "damage_class": "special",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Can only be used after the user has eaten a berry.",
        "flavor_text_entry": "The user lets out a damaging belch at the target. The user must eat a held Berry to use this move."
    },
    "venom-drench": {
        "name": "venom-drench",
        "id": 599,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 20,
        "power": None,
        "type": "poison",
        "damage_class": "status",
        "stat_changes": [
            {
                "change": -1,
                "stat": {
                    "name": "Atk",
                    "url": "https://pokeapi.co/api/v2/stat/2/"
                }
            },
            {
                "change": -1,
                "stat": {
                    "name": "SpAtk",
                    "url": "https://pokeapi.co/api/v2/stat/4/"
                }
            },
            {
                "change": -1,
                "stat": {
                    "name": "Speed",
                    "url": "https://pokeapi.co/api/v2/stat/6/"
                }
            }
        ],
        "effect_chance": 100,
        "target": "all-opponents",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "net-good-stats",
                "url": "https://pokeapi.co/api/v2/move-category/2/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 100
        },
        "effect_entries": "Lowers the target's Attack, Special Attack, and Speed by one stage if it is poisoned.",
        "flavor_text_entry": "Opposing Pok\u00e9mon are drenched in an odd poisonous liquid. This lowers the Attack, Sp. Atk, and Speed stats of a poisoned target."
    },
    "infestation": {
        "name": "infestation",
        "id": 611,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 20,
        "power": 20,
        "type": "bug",
        "damage_class": "special",
        "stat_changes": [],
        "effect_chance": 100,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "trap",
                "url": "https://pokeapi.co/api/v2/move-ailment/8/"
            },
            "ailment_chance": 100,
            "category": {
                "name": "damage+ailment",
                "url": "https://pokeapi.co/api/v2/move-category/4/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": 6,
            "min_hits": None,
            "min_turns": 5,
            "stat_chance": 0
        },
        "effect_entries": "Prevents the target from fleeing and inflicts damage for 2-5 turns.",
        "flavor_text_entry": "The target is infested and attacked for four to five turns. The target can\u2019t flee during this time."
    },
    "corrosive-gas": {
        "name": "corrosive-gas",
        "id": 810,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 40,
        "power": None,
        "type": "poison",
        "damage_class": "status",
        "stat_changes": [],
        "effect_chance": None,
        "target": "all-other-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "unique",
                "url": "https://pokeapi.co/api/v2/move-category/13/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Inflicts regular damage with no additional effect.",
        "flavor_text_entry": "The user surrounds everything around it with highly acidic gas and melts away items they hold."
    },
    "rock-polish": {
        "name": "rock-polish",
        "id": 397,
        "accuracy": None,
        "priority": 0,
        "max_pp": 20,
        "power": None,
        "type": "rock",
        "damage_class": "status",
        "stat_changes": [
            {
                "change": 2,
                "stat": {
                    "name": "Speed",
                    "url": "https://pokeapi.co/api/v2/stat/6/"
                }
            }
        ],
        "effect_chance": None,
        "target": "user",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "net-good-stats",
                "url": "https://pokeapi.co/api/v2/move-category/2/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Raises the user's Speed by two stages.",
        "flavor_text_entry": "The user polishes its body to reduce drag. It can sharply raise the Speed stat. "
    },
    "sharpen": {
        "name": "sharpen",
        "id": 159,
        "accuracy": None,
        "priority": 0,
        "max_pp": 30,
        "power": None,
        "type": "normal",
        "damage_class": "status",
        "stat_changes": [
            {
                "change": 1,
                "stat": {
                    "name": "Atk",
                    "url": "https://pokeapi.co/api/v2/stat/2/"
                }
            }
        ],
        "effect_chance": None,
        "target": "user",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "net-good-stats",
                "url": "https://pokeapi.co/api/v2/move-category/2/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Raises the user's Attack by one stage.",
        "flavor_text_entry": "Reduces the polygon count and raises ATTACK."
    },
    "conversion": {
        "name": "conversion",
        "id": 160,
        "accuracy": None,
        "priority": 0,
        "max_pp": 30,
        "power": None,
        "type": "normal",
        "damage_class": "status",
        "stat_changes": [],
        "effect_chance": None,
        "target": "user",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "unique",
                "url": "https://pokeapi.co/api/v2/move-category/13/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "User's type changes to the type of one of its moves at random.",
        "flavor_text_entry": "Change user's type to a move's type."
    },
    "conversion-2": {
        "name": "conversion-2",
        "id": 176,
        "accuracy": None,
        "priority": 0,
        "max_pp": 30,
        "power": None,
        "type": "normal",
        "damage_class": "status",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "unique",
                "url": "https://pokeapi.co/api/v2/move-category/13/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Changes the user's type to a random type either resistant or immune to the last move used against it.",
        "flavor_text_entry": "The user's type is made resistant."
    },
    "power-swap": {
        "name": "power-swap",
        "id": 384,
        "accuracy": None,
        "priority": 0,
        "max_pp": 10,
        "power": None,
        "type": "psychic",
        "damage_class": "status",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "unique",
                "url": "https://pokeapi.co/api/v2/move-category/13/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "User swaps Attack and Special Attack changes with the target.",
        "flavor_text_entry": "The user employs its psychic power to switch changes to its Attack and Sp. Atk with the foe."
    },
    "guard-swap": {
        "name": "guard-swap",
        "id": 385,
        "accuracy": None,
        "priority": 0,
        "max_pp": 10,
        "power": None,
        "type": "psychic",
        "damage_class": "status",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "unique",
                "url": "https://pokeapi.co/api/v2/move-category/13/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "User swaps Defense and Special Defense changes with the target.",
        "flavor_text_entry": "The user employs its psychic power to switch changes to its Defense and Sp. Def with the foe."
    },
    "speed-swap": {
        "name": "speed-swap",
        "id": 683,
        "accuracy": None,
        "priority": 0,
        "max_pp": 10,
        "power": None,
        "type": "psychic",
        "damage_class": "status",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "unique",
                "url": "https://pokeapi.co/api/v2/move-category/13/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Exchanges the user's Speed with the target's.",
        "flavor_text_entry": "The user exchanges Speed stats with the target."
    },
    "embargo": {
        "name": "embargo",
        "id": 373,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 15,
        "power": None,
        "type": "dark",
        "damage_class": "status",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "embargo",
                "url": "https://pokeapi.co/api/v2/move-ailment/19/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "ailment",
                "url": "https://pokeapi.co/api/v2/move-category/1/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": 5,
            "min_hits": None,
            "min_turns": 5,
            "stat_chance": 0
        },
        "effect_entries": "Target cannot use held items.",
        "flavor_text_entry": "It prevents the foe from using its held item. Its Trainer is also prevented from using items on it."
    },
    "stomp": {
        "name": "stomp",
        "id": 23,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 20,
        "power": 65,
        "type": "normal",
        "damage_class": "physical",
        "stat_changes": [],
        "effect_chance": 30,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 30,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Has a 30% chance to make the target flinch.",
        "flavor_text_entry": "An attack that may cause flinching."
    },
    "milk-drink": {
        "name": "milk-drink",
        "id": 208,
        "accuracy": None,
        "priority": 0,
        "max_pp": 5,
        "power": None,
        "type": "normal",
        "damage_class": "status",
        "stat_changes": [],
        "effect_chance": None,
        "target": "user",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "heal",
                "url": "https://pokeapi.co/api/v2/move-category/3/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 50,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Heals the user by half its max HP.",
        "flavor_text_entry": "Restores HP by 1/2 the max HP."
    },
    "heal-bell": {
        "name": "heal-bell",
        "id": 215,
        "accuracy": None,
        "priority": 0,
        "max_pp": 5,
        "power": None,
        "type": "normal",
        "damage_class": "status",
        "stat_changes": [],
        "effect_chance": None,
        "target": "user-and-allies",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "unique",
                "url": "https://pokeapi.co/api/v2/move-category/13/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Cures the entire party of major status effects.",
        "flavor_text_entry": "The user makes a soothing bell chime to heal the status problems of all the party Pok\u00e9mon."
    },
    "present": {
        "name": "present",
        "id": 217,
        "accuracy": 90,
        "priority": 0,
        "max_pp": 15,
        "power": None,
        "type": "normal",
        "damage_class": "physical",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Randomly inflicts damage with power from 40 to 120 or heals the target for 1/4 its max HP.",
        "flavor_text_entry": "A bomb that may restore HP."
    },
    "wake-up-slap": {
        "name": "wake-up-slap",
        "id": 358,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 10,
        "power": 70,
        "type": "fighting",
        "damage_class": "physical",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "If the target is asleep, has double power and wakes it up.",
        "flavor_text_entry": "This attack inflicts high damage on a sleeping foe. It also wakes the foe up, however."
    },
    "heart-stamp": {
        "name": "heart-stamp",
        "id": 531,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 25,
        "power": 60,
        "type": "psychic",
        "damage_class": "physical",
        "stat_changes": [],
        "effect_chance": 30,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 30,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Has a 30% chance to make the target flinch.",
        "flavor_text_entry": "The user unleashes a vicious blow after its cute act makes the target less wary. It may also make the target flinch."
    },
    "bug-buzz": {
        "name": "bug-buzz",
        "id": 405,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 10,
        "power": 90,
        "type": "bug",
        "damage_class": "special",
        "stat_changes": [
            {
                "change": -1,
                "stat": {
                    "name": "SpDef",
                    "url": "https://pokeapi.co/api/v2/stat/5/"
                }
            }
        ],
        "effect_chance": 10,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage+lower",
                "url": "https://pokeapi.co/api/v2/move-category/6/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 10
        },
        "effect_entries": "Has a 10% chance to lower the target's Special Defense by one stage.",
        "flavor_text_entry": "The user vibrates its wings to generate a damaging sound wave. It may also lower the foe\u2019s Sp. Def stat."
    },
    "lunge": {
        "name": "lunge",
        "id": 679,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 15,
        "power": 80,
        "type": "bug",
        "damage_class": "physical",
        "stat_changes": [
            {
                "change": -1,
                "stat": {
                    "name": "Atk",
                    "url": "https://pokeapi.co/api/v2/stat/2/"
                }
            }
        ],
        "effect_chance": 100,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage+lower",
                "url": "https://pokeapi.co/api/v2/move-category/6/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 100
        },
        "effect_entries": "Lowers the target's Attack by one stage after inflicting damage.",
        "flavor_text_entry": "The user makes a lunge at the target, attacking with full force. This also lowers the target\u2019s Attack stat."
    },
    "skitter-smack": {
        "name": "skitter-smack",
        "id": 806,
        "accuracy": 90,
        "priority": 0,
        "max_pp": 10,
        "power": 70,
        "type": "bug",
        "damage_class": "physical",
        "stat_changes": [
            {
                "change": -1,
                "stat": {
                    "name": "SpAtk",
                    "url": "https://pokeapi.co/api/v2/stat/4/"
                }
            }
        ],
        "effect_chance": 100,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage+lower",
                "url": "https://pokeapi.co/api/v2/move-category/6/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 100
        },
        "effect_entries": "Inflicts regular damage with no additional effect.",
        "flavor_text_entry": "The user skitters behind the target to attack. This also lowers the target\u2019s Sp. Atk stat."
    },
    "poison-sting": {
        "name": "poison-sting",
        "id": 40,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 35,
        "power": 15,
        "type": "poison",
        "damage_class": "physical",
        "stat_changes": [],
        "effect_chance": 30,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "poison",
                "url": "https://pokeapi.co/api/v2/move-ailment/5/"
            },
            "ailment_chance": 30,
            "category": {
                "name": "damage+ailment",
                "url": "https://pokeapi.co/api/v2/move-category/4/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Has a 30% chance to poison the target.",
        "flavor_text_entry": "An attack that may poison the target."
    },
    "pin-missile": {
        "name": "pin-missile",
        "id": 42,
        "accuracy": 95,
        "priority": 0,
        "max_pp": 20,
        "power": 25,
        "type": "bug",
        "damage_class": "physical",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": 5,
            "max_turns": None,
            "min_hits": 2,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Hits 2-5 times in one turn.",
        "flavor_text_entry": "Fires pins that strike 2-5 times."
    },
    "destiny-bond": {
        "name": "destiny-bond",
        "id": 194,
        "accuracy": None,
        "priority": 0,
        "max_pp": 5,
        "power": None,
        "type": "ghost",
        "damage_class": "status",
        "stat_changes": [],
        "effect_chance": None,
        "target": "user",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "unique",
                "url": "https://pokeapi.co/api/v2/move-category/13/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "If the user faints this turn, the target automatically will, too.",
        "flavor_text_entry": "The foe faints if the user does."
    },
    "beat-up": {
        "name": "beat-up",
        "id": 251,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 10,
        "power": None,
        "type": "dark",
        "damage_class": "physical",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": 6,
            "max_turns": None,
            "min_hits": 6,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Hits once for every conscious Pok\u00e9mon the trainer has.",
        "flavor_text_entry": "Party POK\u00e9MON join in the attack. "
    },
    "revenge": {
        "name": "revenge",
        "id": 279,
        "accuracy": 100,
        "priority": -4,
        "max_pp": 10,
        "power": 60,
        "type": "fighting",
        "damage_class": "physical",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Inflicts double damage if the user takes damage before attacking this turn.",
        "flavor_text_entry": "An attack that gains power if injured by the foe."
    },
    "silver-wind": {
        "name": "silver-wind",
        "id": 318,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 5,
        "power": 60,
        "type": "bug",
        "damage_class": "special",
        "stat_changes": [
            {
                "change": 1,
                "stat": {
                    "name": "Atk",
                    "url": "https://pokeapi.co/api/v2/stat/2/"
                }
            },
            {
                "change": 1,
                "stat": {
                    "name": "Def",
                    "url": "https://pokeapi.co/api/v2/stat/3/"
                }
            },
            {
                "change": 1,
                "stat": {
                    "name": "SpAtk",
                    "url": "https://pokeapi.co/api/v2/stat/4/"
                }
            },
            {
                "change": 1,
                "stat": {
                    "name": "SpDef",
                    "url": "https://pokeapi.co/api/v2/stat/5/"
                }
            },
            {
                "change": 1,
                "stat": {
                    "name": "Speed",
                    "url": "https://pokeapi.co/api/v2/stat/6/"
                }
            }
        ],
        "effect_chance": 10,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage+raise",
                "url": "https://pokeapi.co/api/v2/move-category/7/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 10
        },
        "effect_entries": "Has a 10% chance to raise all of the user's stats by one stage.",
        "flavor_text_entry": "A powdery attack that may raise abilities."
    },
    "assurance": {
        "name": "assurance",
        "id": 372,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 10,
        "power": 60,
        "type": "dark",
        "damage_class": "physical",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Power is doubled if the target has already received damage this turn.",
        "flavor_text_entry": "If the foe has already taken some damage in the same turn, this attack\u2019s power is doubled."
    },
    "attack-order": {
        "name": "attack-order",
        "id": 454,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 15,
        "power": 90,
        "type": "bug",
        "damage_class": "physical",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 1,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Has an increased chance for a critical hit.",
        "flavor_text_entry": "The user calls out its underlings to pummel the foe. It has a high critical-hit ratio."
    },
    "defend-order": {
        "name": "defend-order",
        "id": 455,
        "accuracy": None,
        "priority": 0,
        "max_pp": 10,
        "power": None,
        "type": "bug",
        "damage_class": "status",
        "stat_changes": [
            {
                "change": 1,
                "stat": {
                    "name": "Def",
                    "url": "https://pokeapi.co/api/v2/stat/3/"
                }
            },
            {
                "change": 1,
                "stat": {
                    "name": "SpDef",
                    "url": "https://pokeapi.co/api/v2/stat/5/"
                }
            }
        ],
        "effect_chance": None,
        "target": "user",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "net-good-stats",
                "url": "https://pokeapi.co/api/v2/move-category/2/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Raises the user's Defense and Special Defense by one stage.",
        "flavor_text_entry": "The user calls out its underlings to make a living shield, raising its Defense and Sp. Def stats."
    },
    "heal-order": {
        "name": "heal-order",
        "id": 456,
        "accuracy": None,
        "priority": 0,
        "max_pp": 10,
        "power": None,
        "type": "bug",
        "damage_class": "status",
        "stat_changes": [],
        "effect_chance": None,
        "target": "user",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "heal",
                "url": "https://pokeapi.co/api/v2/move-category/3/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 50,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Heals the user by half its max HP.",
        "flavor_text_entry": "The user calls out its underlings to heal it. The user regains up to half of its max HP."
    },
    "hex": {
        "name": "hex",
        "id": 506,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 10,
        "power": 65,
        "type": "ghost",
        "damage_class": "special",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Has double power if the target has a major status ailment.",
        "flavor_text_entry": "This relentless attack does massive damage to a target affected by status problems."
    },
    "aromatic-mist": {
        "name": "aromatic-mist",
        "id": 597,
        "accuracy": None,
        "priority": 0,
        "max_pp": 20,
        "power": None,
        "type": "fairy",
        "damage_class": "status",
        "stat_changes": [
            {
                "change": 1,
                "stat": {
                    "name": "SpDef",
                    "url": "https://pokeapi.co/api/v2/stat/5/"
                }
            }
        ],
        "effect_chance": None,
        "target": "ally",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "net-good-stats",
                "url": "https://pokeapi.co/api/v2/move-category/2/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Raises a selected ally's Special Defense by one stage.",
        "flavor_text_entry": "The user raises the Sp. Def stat of an ally Pok\u00e9mon by using a mysterious aroma."
    },
    "pollen-puff": {
        "name": "pollen-puff",
        "id": 676,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 15,
        "power": 90,
        "type": "bug",
        "damage_class": "special",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Damages opponents, but heals allies for 50% of their max HP.",
        "flavor_text_entry": "The user attacks the enemy with a pollen puff that explodes. If the target is an ally, it gives the ally a pollen puff that restores its HP instead."
    },
    "psychic-noise": {
        "name": "psychic-noise",
        "id": 917,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 10,
        "power": 75,
        "type": "psychic",
        "damage_class": "special",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": None
    },
    "razor-leaf": {
        "name": "razor-leaf",
        "id": 75,
        "accuracy": 95,
        "priority": 0,
        "max_pp": 25,
        "power": 55,
        "type": "grass",
        "damage_class": "physical",
        "stat_changes": [],
        "effect_chance": None,
        "target": "all-opponents",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 1,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Has an increased chance for a critical hit.",
        "flavor_text_entry": "Has a high criti\u00ad cal hit ratio."
    },
    "mind-reader": {
        "name": "mind-reader",
        "id": 170,
        "accuracy": None,
        "priority": 0,
        "max_pp": 5,
        "power": None,
        "type": "normal",
        "damage_class": "status",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "unique",
                "url": "https://pokeapi.co/api/v2/move-category/13/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Ensures that the user's next move will hit the target.",
        "flavor_text_entry": "Ensures the next attack will hit."
    },
    "cotton-spore": {
        "name": "cotton-spore",
        "id": 178,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 40,
        "power": None,
        "type": "grass",
        "damage_class": "status",
        "stat_changes": [
            {
                "change": -2,
                "stat": {
                    "name": "Speed",
                    "url": "https://pokeapi.co/api/v2/stat/6/"
                }
            }
        ],
        "effect_chance": None,
        "target": "all-opponents",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "net-good-stats",
                "url": "https://pokeapi.co/api/v2/move-category/2/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Lowers the target's Speed by two stages.",
        "flavor_text_entry": "Sharply reduces the foe's SPEED."
    },
    "extrasensory": {
        "name": "extrasensory",
        "id": 326,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 20,
        "power": 80,
        "type": "psychic",
        "damage_class": "special",
        "stat_changes": [],
        "effect_chance": 10,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 10,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Has a 10% chance to make the target flinch.",
        "flavor_text_entry": "Attacks with a peculiar power. May cause flinching."
    },
    "life-dew": {
        "name": "life-dew",
        "id": 791,
        "accuracy": None,
        "priority": 0,
        "max_pp": 10,
        "power": None,
        "type": "water",
        "damage_class": "status",
        "stat_changes": [],
        "effect_chance": None,
        "target": "user-and-allies",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "heal",
                "url": "https://pokeapi.co/api/v2/move-category/3/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 25,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "flavor_text_entry": "The user scatters mysterious water around and restores the HP of itself and its ally Pok\u00e9mon in the battle."
    },
    "petal-dance": {
        "name": "petal-dance",
        "id": 80,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 10,
        "power": 120,
        "type": "grass",
        "damage_class": "special",
        "stat_changes": [],
        "effect_chance": None,
        "target": "random-opponent",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Hits every turn for 2-3 turns, then confuses the user.",
        "flavor_text_entry": "Works 2-3 turns and confuses user."
    },
    "ingrain": {
        "name": "ingrain",
        "id": 275,
        "accuracy": None,
        "priority": 0,
        "max_pp": 20,
        "power": None,
        "type": "grass",
        "damage_class": "status",
        "stat_changes": [],
        "effect_chance": None,
        "target": "user",
        "meta": {
            "ailment": {
                "name": "ingrain",
                "url": "https://pokeapi.co/api/v2/move-ailment/21/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "ailment",
                "url": "https://pokeapi.co/api/v2/move-category/1/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Prevents the user from leaving battle.  User regains 1/16 of its max HP every turn.",
        "flavor_text_entry": "Lays roots that restore HP. The user can\u2019t switch out."
    },
    "power-whip": {
        "name": "power-whip",
        "id": 438,
        "accuracy": 85,
        "priority": 0,
        "max_pp": 10,
        "power": 120,
        "type": "grass",
        "damage_class": "physical",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Inflicts regular damage with no additional effect.",
        "flavor_text_entry": "The user violently whirls its vines or tentacles to harshly lash the foe. "
    },
    "splash": {
        "name": "splash",
        "id": 150,
        "accuracy": None,
        "priority": 0,
        "max_pp": 40,
        "power": None,
        "type": "normal",
        "damage_class": "status",
        "stat_changes": [],
        "effect_chance": None,
        "target": "user",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "unique",
                "url": "https://pokeapi.co/api/v2/move-category/13/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Does nothing.",
        "flavor_text_entry": "Has no effect whatsoever."
    },
    "teeter-dance": {
        "name": "teeter-dance",
        "id": 298,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 20,
        "power": None,
        "type": "normal",
        "damage_class": "status",
        "stat_changes": [],
        "effect_chance": None,
        "target": "all-other-pokemon",
        "meta": {
            "ailment": {
                "name": "confusion",
                "url": "https://pokeapi.co/api/v2/move-ailment/6/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "ailment",
                "url": "https://pokeapi.co/api/v2/move-category/1/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": 5,
            "min_hits": None,
            "min_turns": 2,
            "stat_chance": 0
        },
        "effect_entries": "Confuses the target.",
        "flavor_text_entry": "Confuses all POK\u00e9MON on the scene."
    },
    "acupressure": {
        "name": "acupressure",
        "id": 367,
        "accuracy": None,
        "priority": 0,
        "max_pp": 30,
        "power": None,
        "type": "normal",
        "damage_class": "status",
        "stat_changes": [],
        "effect_chance": None,
        "target": "user-or-ally",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "unique",
                "url": "https://pokeapi.co/api/v2/move-category/13/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Raises one of a friendly Pok\u00e9mon's stats at random by two stages.",
        "flavor_text_entry": "The user applies pressure to stress points, sharply boosting one of its stats."
    },
    "draining-kiss": {
        "name": "draining-kiss",
        "id": 577,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 10,
        "power": 50,
        "type": "fairy",
        "damage_class": "special",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage+heal",
                "url": "https://pokeapi.co/api/v2/move-category/8/"
            },
            "crit_rate": 0,
            "drain": 75,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Drains 75% of the damage inflicted to heal the user.",
        "flavor_text_entry": "The user steals the target\u2019s energy with a kiss. The user\u2019s HP is restored by over half of the damage taken by the target."
    },
    "triple-axel": {
        "name": "triple-axel",
        "id": 813,
        "accuracy": 90,
        "priority": 0,
        "max_pp": 10,
        "power": 20,
        "type": "ice",
        "damage_class": "physical",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": 3,
            "max_turns": None,
            "min_hits": 3,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Inflicts regular damage with no additional effect.",
        "flavor_text_entry": "A consecutive three-kick attack that becomes more powerful with each successful hit."
    },
    "high-jump-kick": {
        "name": "high-jump-kick",
        "id": 136,
        "accuracy": 90,
        "priority": 0,
        "max_pp": 10,
        "power": 130,
        "type": "fighting",
        "damage_class": "physical",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "If the user misses, it takes half the damage it would have inflicted in recoil.",
        "flavor_text_entry": "May miss and hurt the user."
    },
    "solar-blade": {
        "name": "solar-blade",
        "id": 669,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 10,
        "power": 125,
        "type": "grass",
        "damage_class": "physical",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Requires a turn to charge before attacking.",
        "flavor_text_entry": "In this two-turn attack, the user gathers light and fills a blade with the light\u2019s energy, attacking the target on the next turn."
    },
    "trop-kick": {
        "name": "trop-kick",
        "id": 688,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 15,
        "power": 70,
        "type": "grass",
        "damage_class": "physical",
        "stat_changes": [
            {
                "change": -1,
                "stat": {
                    "name": "Atk",
                    "url": "https://pokeapi.co/api/v2/stat/2/"
                }
            }
        ],
        "effect_chance": 100,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage+lower",
                "url": "https://pokeapi.co/api/v2/move-category/6/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 100
        },
        "effect_entries": "Lowers the target's Attack by one stage after inflicting damage.",
        "flavor_text_entry": "The user lands an intense kick of tropical origins on the target. This also lowers the target\u2019s Attack stat."
    },
    "sand-tomb": {
        "name": "sand-tomb",
        "id": 328,
        "accuracy": 85,
        "priority": 0,
        "max_pp": 15,
        "power": 35,
        "type": "ground",
        "damage_class": "physical",
        "stat_changes": [],
        "effect_chance": 100,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "trap",
                "url": "https://pokeapi.co/api/v2/move-ailment/8/"
            },
            "ailment_chance": 100,
            "category": {
                "name": "damage+ailment",
                "url": "https://pokeapi.co/api/v2/move-category/4/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": 6,
            "min_hits": None,
            "min_turns": 5,
            "stat_chance": 0
        },
        "effect_entries": "Prevents the target from fleeing and inflicts damage for 2-5 turns.",
        "flavor_text_entry": "The user traps the target inside a harshly raging sandstorm for four to five turns."
    },
    "power-trick": {
        "name": "power-trick",
        "id": 379,
        "accuracy": None,
        "priority": 0,
        "max_pp": 10,
        "power": None,
        "type": "psychic",
        "damage_class": "status",
        "stat_changes": [],
        "effect_chance": None,
        "target": "user",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "unique",
                "url": "https://pokeapi.co/api/v2/move-category/13/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "User swaps Attack and Defense.",
        "flavor_text_entry": "The user employs its psychic power to switch its Attack with its Defense stat."
    },
    "drill-run": {
        "name": "drill-run",
        "id": 529,
        "accuracy": 95,
        "priority": 0,
        "max_pp": 10,
        "power": 80,
        "type": "ground",
        "damage_class": "physical",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 1,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Has an increased chance for a critical hit.",
        "flavor_text_entry": "The user crashes into its target while rotating its body like a drill. Critical hits land more easily."
    },
    "ice-spinner": {
        "name": "ice-spinner",
        "id": 861,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 15,
        "power": 80,
        "type": "ice",
        "damage_class": "physical",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": None
    },
    "earth-power": {
        "name": "earth-power",
        "id": 414,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 10,
        "power": 90,
        "type": "ground",
        "damage_class": "special",
        "stat_changes": [
            {
                "change": -1,
                "stat": {
                    "name": "SpDef",
                    "url": "https://pokeapi.co/api/v2/stat/5/"
                }
            }
        ],
        "effect_chance": 10,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage+lower",
                "url": "https://pokeapi.co/api/v2/move-category/6/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 10
        },
        "effect_entries": "Has a 10% chance to lower the target's Special Defense by one stage.",
        "flavor_text_entry": "The user makes the ground under the foe erupt with power. It may also lower the target\u2019s Sp. Def."
    },
    "slam": {
        "name": "slam",
        "id": 21,
        "accuracy": 75,
        "priority": 0,
        "max_pp": 20,
        "power": 80,
        "type": "normal",
        "damage_class": "physical",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Inflicts regular damage with no additional effect.",
        "flavor_text_entry": "Slams the foe with a tail, vine, etc."
    },
    "wrap": {
        "name": "wrap",
        "id": 35,
        "accuracy": 90,
        "priority": 0,
        "max_pp": 20,
        "power": 15,
        "type": "normal",
        "damage_class": "physical",
        "stat_changes": [],
        "effect_chance": 100,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "trap",
                "url": "https://pokeapi.co/api/v2/move-ailment/8/"
            },
            "ailment_chance": 100,
            "category": {
                "name": "damage+ailment",
                "url": "https://pokeapi.co/api/v2/move-category/4/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": 6,
            "min_hits": None,
            "min_turns": 5,
            "stat_chance": 0
        },
        "effect_entries": "Prevents the target from fleeing and inflicts damage for 2-5 turns.",
        "flavor_text_entry": "Squeezes the foe for 2-5 turns."
    },
    "dragon-rage": {
        "name": "dragon-rage",
        "id": 82,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 10,
        "power": None,
        "type": "dragon",
        "damage_class": "special",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Inflicts 40 points of damage.",
        "flavor_text_entry": "Always inflicts 40HP damage."
    },
    "fire-spin": {
        "name": "fire-spin",
        "id": 83,
        "accuracy": 85,
        "priority": 0,
        "max_pp": 15,
        "power": 35,
        "type": "fire",
        "damage_class": "special",
        "stat_changes": [],
        "effect_chance": 100,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "trap",
                "url": "https://pokeapi.co/api/v2/move-ailment/8/"
            },
            "ailment_chance": 100,
            "category": {
                "name": "damage+ailment",
                "url": "https://pokeapi.co/api/v2/move-category/4/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": 6,
            "min_hits": None,
            "min_turns": 5,
            "stat_chance": 0
        },
        "effect_entries": "Prevents the target from fleeing and inflicts damage for 2-5 turns.",
        "flavor_text_entry": "Traps foe in fire for 2-5 turns."
    },
    "dragon-breath": {
        "name": "dragon-breath",
        "id": 225,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 20,
        "power": 60,
        "type": "dragon",
        "damage_class": "special",
        "stat_changes": [],
        "effect_chance": 30,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "paralysis",
                "url": "https://pokeapi.co/api/v2/move-ailment/1/"
            },
            "ailment_chance": 30,
            "category": {
                "name": "damage+ailment",
                "url": "https://pokeapi.co/api/v2/move-category/4/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Has a 30% chance to paralyze the target.",
        "flavor_text_entry": "A strong breath attack."
    },
    "extreme-speed": {
        "name": "extreme-speed",
        "id": 245,
        "accuracy": 100,
        "priority": 2,
        "max_pp": 5,
        "power": 80,
        "type": "normal",
        "damage_class": "physical",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Inflicts regular damage with no additional effect.",
        "flavor_text_entry": "A powerful first- strike move."
    },
    "dragon-dance": {
        "name": "dragon-dance",
        "id": 349,
        "accuracy": None,
        "priority": 0,
        "max_pp": 20,
        "power": None,
        "type": "dragon",
        "damage_class": "status",
        "stat_changes": [
            {
                "change": 1,
                "stat": {
                    "name": "Atk",
                    "url": "https://pokeapi.co/api/v2/stat/2/"
                }
            },
            {
                "change": 1,
                "stat": {
                    "name": "Speed",
                    "url": "https://pokeapi.co/api/v2/stat/6/"
                }
            }
        ],
        "effect_chance": None,
        "target": "user",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "net-good-stats",
                "url": "https://pokeapi.co/api/v2/move-category/2/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Raises the user's Attack and Speed by one stage.",
        "flavor_text_entry": "A mystical dance that ups ATTACK and SPEED."
    },
    "dragon-pulse": {
        "name": "dragon-pulse",
        "id": 406,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 10,
        "power": 85,
        "type": "dragon",
        "damage_class": "special",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Inflicts regular damage with no additional effect.",
        "flavor_text_entry": "The foe is attacked with a shock wave generated by the user\u2019s gaping mouth. "
    },
    "dragon-rush": {
        "name": "dragon-rush",
        "id": 407,
        "accuracy": 75,
        "priority": 0,
        "max_pp": 10,
        "power": 100,
        "type": "dragon",
        "damage_class": "physical",
        "stat_changes": [],
        "effect_chance": 20,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 20,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Has a 20% chance to make the target flinch.",
        "flavor_text_entry": "The user tackles the foe while exhibiting overwhelming menace. It may also make the target flinch."
    },
    "draco-meteor": {
        "name": "draco-meteor",
        "id": 434,
        "accuracy": 90,
        "priority": 0,
        "max_pp": 5,
        "power": 130,
        "type": "dragon",
        "damage_class": "special",
        "stat_changes": [
            {
                "change": -2,
                "stat": {
                    "name": "SpAtk",
                    "url": "https://pokeapi.co/api/v2/stat/4/"
                }
            }
        ],
        "effect_chance": 100,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage+raise",
                "url": "https://pokeapi.co/api/v2/move-category/7/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 100
        },
        "effect_entries": "Lowers the user's Special Attack by two stages after inflicting damage.",
        "flavor_text_entry": "Comets are summoned down from the sky. The attack\u2019s recoil sharply reduces the user\u2019s Sp. Atk stat."
    },
    "aqua-jet": {
        "name": "aqua-jet",
        "id": 453,
        "accuracy": 100,
        "priority": 1,
        "max_pp": 20,
        "power": 40,
        "type": "water",
        "damage_class": "physical",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Inflicts regular damage with no additional effect.",
        "flavor_text_entry": "The user lunges at the foe at a speed that makes it almost invisible. It is sure to strike first."
    },
    "dragon-tail": {
        "name": "dragon-tail",
        "id": 525,
        "accuracy": 90,
        "priority": -6,
        "max_pp": 10,
        "power": 60,
        "type": "dragon",
        "damage_class": "physical",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Ends wild battles.  Forces trainers to switch Pok\u00e9mon.",
        "flavor_text_entry": "The user knocks away the target and drags out another Pok\u00e9mon in its party. In the wild, the battle ends."
    },
    "brutal-swing": {
        "name": "brutal-swing",
        "id": 693,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 20,
        "power": 60,
        "type": "dark",
        "damage_class": "physical",
        "stat_changes": [],
        "effect_chance": None,
        "target": "all-other-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Inflicts regular damage with no additional effect.",
        "flavor_text_entry": "The user swings its body around violently to inflict damage on everything in its vicinity."
    },
    "breaking-swipe": {
        "name": "breaking-swipe",
        "id": 784,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 15,
        "power": 60,
        "type": "dragon",
        "damage_class": "physical",
        "stat_changes": [
            {
                "change": -1,
                "stat": {
                    "name": "Atk",
                    "url": "https://pokeapi.co/api/v2/stat/2/"
                }
            }
        ],
        "effect_chance": 100,
        "target": "all-opponents",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage+lower",
                "url": "https://pokeapi.co/api/v2/move-category/6/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 100
        },
        "effect_entries": "Lowers the target's Attack by one stage after inflicting damage.",
        "flavor_text_entry": "The user swings its tough tail wildly and attacks opposing Pok\u00e9mon. This also lowers their Attack stats."
    },
    "scale-shot": {
        "name": "scale-shot",
        "id": 799,
        "accuracy": 90,
        "priority": 0,
        "max_pp": 20,
        "power": 25,
        "type": "dragon",
        "damage_class": "physical",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": 5,
            "max_turns": None,
            "min_hits": 2,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Boosts the user's Speed and lowers their Defense by one stage after inflicting damage two to five times in a row.",
        "flavor_text_entry": "The user attacks by shooting scales two to five times in a row. This move boosts the user\u2019s Speed stat but lowers its Defense stat."
    },
    "dragon-cheer": {
        "name": "dragon-cheer",
        "id": 913,
        "accuracy": 0,
        "priority": 0,
        "max_pp": 15,
        "power": 0,
        "type": "dragon",
        "damage_class": "status",
        "stat_changes": [],
        "effect_chance": None,
        "target": "all-allies",
        "meta": None
    },
    "horn-drill": {
        "name": "horn-drill",
        "id": 32,
        "accuracy": 30,
        "priority": 0,
        "max_pp": 5,
        "power": None,
        "type": "normal",
        "damage_class": "physical",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "ohko",
                "url": "https://pokeapi.co/api/v2/move-category/9/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Causes a one-hit KO.",
        "flavor_text_entry": "A one-hit KO, drill attack."
    },
    "razor-wind": {
        "name": "razor-wind",
        "id": 13,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 10,
        "power": 80,
        "type": "normal",
        "damage_class": "special",
        "stat_changes": [],
        "effect_chance": None,
        "target": "all-opponents",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 1,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Requires a turn to charge before attacking.",
        "flavor_text_entry": "1st turn: Prepare 2nd turn: Attack"
    },
    "heat-wave": {
        "name": "heat-wave",
        "id": 257,
        "accuracy": 90,
        "priority": 0,
        "max_pp": 10,
        "power": 95,
        "type": "fire",
        "damage_class": "special",
        "stat_changes": [],
        "effect_chance": 10,
        "target": "all-opponents",
        "meta": {
            "ailment": {
                "name": "burn",
                "url": "https://pokeapi.co/api/v2/move-ailment/4/"
            },
            "ailment_chance": 10,
            "category": {
                "name": "damage+ailment",
                "url": "https://pokeapi.co/api/v2/move-category/4/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Has a 10% chance to burn the target.",
        "flavor_text_entry": "Exhales a hot breath on the foe. May inflict a burn."
    },
    "dragon-claw": {
        "name": "dragon-claw",
        "id": 337,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 15,
        "power": 80,
        "type": "dragon",
        "damage_class": "physical",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Inflicts regular damage with no additional effect.",
        "flavor_text_entry": "Slashes the foe with sharp claws."
    },
    "ember": {
        "name": "ember",
        "id": 52,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 25,
        "power": 40,
        "type": "fire",
        "damage_class": "special",
        "stat_changes": [],
        "effect_chance": 10,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "burn",
                "url": "https://pokeapi.co/api/v2/move-ailment/4/"
            },
            "ailment_chance": 10,
            "category": {
                "name": "damage+ailment",
                "url": "https://pokeapi.co/api/v2/move-category/4/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Has a 10% chance to burn the target.",
        "flavor_text_entry": "An attack that may inflict a burn."
    },
    "fire-fang": {
        "name": "fire-fang",
        "id": 424,
        "accuracy": 95,
        "priority": 0,
        "max_pp": 15,
        "power": 65,
        "type": "fire",
        "damage_class": "physical",
        "stat_changes": [],
        "effect_chance": 10,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "burn",
                "url": "https://pokeapi.co/api/v2/move-ailment/4/"
            },
            "ailment_chance": 10,
            "category": {
                "name": "damage+ailment",
                "url": "https://pokeapi.co/api/v2/move-category/4/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 10,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Has a 10% chance to burn the target and a 10% chance to make the target flinch.",
        "flavor_text_entry": "The user bites with flame-cloaked fangs. It may also make the foe flinch or sustain a burn."
    },
    "temper-flare": {
        "name": "temper-flare",
        "id": 915,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 10,
        "power": 75,
        "type": "fire",
        "damage_class": "physical",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": None
    },
    "psychic-fangs": {
        "name": "psychic-fangs",
        "id": 706,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 10,
        "power": 85,
        "type": "psychic",
        "damage_class": "physical",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Destroys Reflect and Light Screen.",
        "flavor_text_entry": "The user bites the target with its psychic capabilities. This can also destroy Light Screen and Reflect."
    },
    "smelling-salts": {
        "name": "smelling-salts",
        "id": 265,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 10,
        "power": 70,
        "type": "normal",
        "damage_class": "physical",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "If the target is paralyzed, inflicts double damage and cures the paralysis.",
        "flavor_text_entry": "Powerful against paralyzed foes, but also heals them."
    },
    "overheat": {
        "name": "overheat",
        "id": 315,
        "accuracy": 90,
        "priority": 0,
        "max_pp": 5,
        "power": 130,
        "type": "fire",
        "damage_class": "special",
        "stat_changes": [
            {
                "change": -2,
                "stat": {
                    "name": "SpAtk",
                    "url": "https://pokeapi.co/api/v2/stat/4/"
                }
            }
        ],
        "effect_chance": 100,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage+raise",
                "url": "https://pokeapi.co/api/v2/move-category/7/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 100
        },
        "effect_entries": "Lowers the user's Special Attack by two stages after inflicting damage.",
        "flavor_text_entry": "Allows a full-power attack, but sharply lowers SP. ATK."
    },
    "snarl": {
        "name": "snarl",
        "id": 555,
        "accuracy": 95,
        "priority": 0,
        "max_pp": 15,
        "power": 55,
        "type": "dark",
        "damage_class": "special",
        "stat_changes": [
            {
                "change": -1,
                "stat": {
                    "name": "SpAtk",
                    "url": "https://pokeapi.co/api/v2/stat/4/"
                }
            }
        ],
        "effect_chance": 100,
        "target": "all-opponents",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage+lower",
                "url": "https://pokeapi.co/api/v2/move-category/6/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 100
        },
        "effect_entries": "Has a 100% chance to lower the target's Special Attack by one stage.",
        "flavor_text_entry": "The user yells as if it is ranting about something, making the target\u2019s Sp. Atk stat decrease."
    },
    "smog": {
        "name": "smog",
        "id": 123,
        "accuracy": 70,
        "priority": 0,
        "max_pp": 20,
        "power": 30,
        "type": "poison",
        "damage_class": "special",
        "stat_changes": [],
        "effect_chance": 40,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "poison",
                "url": "https://pokeapi.co/api/v2/move-ailment/5/"
            },
            "ailment_chance": 40,
            "category": {
                "name": "damage+ailment",
                "url": "https://pokeapi.co/api/v2/move-category/4/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Has a 40% chance to poison the target.",
        "flavor_text_entry": "An attack that may poison the foe."
    },
    "acid-armor": {
        "name": "acid-armor",
        "id": 151,
        "accuracy": None,
        "priority": 0,
        "max_pp": 20,
        "power": None,
        "type": "poison",
        "damage_class": "status",
        "stat_changes": [
            {
                "change": 2,
                "stat": {
                    "name": "Def",
                    "url": "https://pokeapi.co/api/v2/stat/3/"
                }
            }
        ],
        "effect_chance": None,
        "target": "user",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "net-good-stats",
                "url": "https://pokeapi.co/api/v2/move-category/2/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Raises the user's Defense by two stages.",
        "flavor_text_entry": "Sharply raises the user's DEFENSE."
    },
    "mean-look": {
        "name": "mean-look",
        "id": 212,
        "accuracy": None,
        "priority": 0,
        "max_pp": 5,
        "power": None,
        "type": "normal",
        "damage_class": "status",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "unique",
                "url": "https://pokeapi.co/api/v2/move-category/13/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Prevents the target from leaving battle.",
        "flavor_text_entry": "Prevents fleeing or switching."
    },
    "memento": {
        "name": "memento",
        "id": 262,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 10,
        "power": None,
        "type": "dark",
        "damage_class": "status",
        "stat_changes": [
            {
                "change": -2,
                "stat": {
                    "name": "Atk",
                    "url": "https://pokeapi.co/api/v2/stat/2/"
                }
            },
            {
                "change": -2,
                "stat": {
                    "name": "SpAtk",
                    "url": "https://pokeapi.co/api/v2/stat/4/"
                }
            }
        ],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "unique",
                "url": "https://pokeapi.co/api/v2/move-category/13/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Lowers the target's Attack and Special Attack by two stages.  User faints.",
        "flavor_text_entry": "The user faints and lowers the foe\u2019s abilities."
    },
    "imprison": {
        "name": "imprison",
        "id": 286,
        "accuracy": None,
        "priority": 0,
        "max_pp": 10,
        "power": None,
        "type": "psychic",
        "damage_class": "status",
        "stat_changes": [],
        "effect_chance": None,
        "target": "user",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "unique",
                "url": "https://pokeapi.co/api/v2/move-category/13/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Prevents the target from using any moves that the user also knows.",
        "flavor_text_entry": "Prevents foes from using moves known by the user."
    },
    "shadow-punch": {
        "name": "shadow-punch",
        "id": 325,
        "accuracy": None,
        "priority": 0,
        "max_pp": 20,
        "power": 60,
        "type": "ghost",
        "damage_class": "physical",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Never misses.",
        "flavor_text_entry": "An unavoidable punch that is thrown from shadows."
    },
    "mud-bomb": {
        "name": "mud-bomb",
        "id": 426,
        "accuracy": 85,
        "priority": 0,
        "max_pp": 10,
        "power": 65,
        "type": "ground",
        "damage_class": "special",
        "stat_changes": [
            {
                "change": -1,
                "stat": {
                    "name": "accuracy",
                    "url": "https://pokeapi.co/api/v2/stat/7/"
                }
            }
        ],
        "effect_chance": 30,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage+lower",
                "url": "https://pokeapi.co/api/v2/move-category/6/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 30
        },
        "effect_entries": "Has a 30% chance to lower the target's accuracy by one stage.",
        "flavor_text_entry": "The user launches a hard-packed mud ball to attack. It may also lower the target\u2019s accuracy."
    },
    "moonblast": {
        "name": "moonblast",
        "id": 585,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 15,
        "power": 95,
        "type": "fairy",
        "damage_class": "special",
        "stat_changes": [
            {
                "change": -1,
                "stat": {
                    "name": "SpAtk",
                    "url": "https://pokeapi.co/api/v2/stat/4/"
                }
            }
        ],
        "effect_chance": 30,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage+lower",
                "url": "https://pokeapi.co/api/v2/move-category/6/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 30
        },
        "effect_entries": "Has a 30% chance to lower the target's Special Attack by one stage.",
        "flavor_text_entry": "Borrowing the power of the moon, the user attacks the target. This may also lower the target\u2019s Sp. Atk stat."
    },
    "smokescreen": {
        "name": "smokescreen",
        "id": 108,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 20,
        "power": None,
        "type": "normal",
        "damage_class": "status",
        "stat_changes": [
            {
                "change": -1,
                "stat": {
                    "name": "accuracy",
                    "url": "https://pokeapi.co/api/v2/stat/7/"
                }
            }
        ],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "net-good-stats",
                "url": "https://pokeapi.co/api/v2/move-category/2/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Lowers the target's accuracy by one stage.",
        "flavor_text_entry": "Lowers the foe's accuracy."
    },
    "will-o-wisp": {
        "name": "will-o-wisp",
        "id": 261,
        "accuracy": 85,
        "priority": 0,
        "max_pp": 15,
        "power": None,
        "type": "fire",
        "damage_class": "status",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "burn",
                "url": "https://pokeapi.co/api/v2/move-ailment/4/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "ailment",
                "url": "https://pokeapi.co/api/v2/move-category/1/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Burns the target.",
        "flavor_text_entry": "Inflicts a burn on the foe with intense fire."
    },
    "grudge": {
        "name": "grudge",
        "id": 288,
        "accuracy": None,
        "priority": 0,
        "max_pp": 5,
        "power": None,
        "type": "ghost",
        "damage_class": "status",
        "stat_changes": [],
        "effect_chance": None,
        "target": "user",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "unique",
                "url": "https://pokeapi.co/api/v2/move-category/13/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "If the user faints this turn, the PP of the move that fainted it drops to 0.",
        "flavor_text_entry": "If the user faints, deletes the PP of the final move."
    },
    "double-hit": {
        "name": "double-hit",
        "id": 458,
        "accuracy": 90,
        "priority": 0,
        "max_pp": 10,
        "power": 35,
        "type": "normal",
        "damage_class": "physical",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": 2,
            "max_turns": None,
            "min_hits": 2,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Hits twice in one turn.",
        "flavor_text_entry": "The user slams the foe with a tail, etc. The target is hit twice in a row. "
    },
    "transform": {
        "name": "transform",
        "id": 144,
        "accuracy": None,
        "priority": 0,
        "max_pp": 10,
        "power": None,
        "type": "normal",
        "damage_class": "status",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "unique",
                "url": "https://pokeapi.co/api/v2/move-category/13/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "User becomes a copy of the target until it leaves battle.",
        "flavor_text_entry": "The user assumes the foe's guise."
    },
    "pay-day": {
        "name": "pay-day",
        "id": 6,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 20,
        "power": 40,
        "type": "normal",
        "damage_class": "physical",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Scatters money on the ground worth five times the user's level.",
        "flavor_text_entry": "Throws coins. Gets them back later."
    },
    "wish": {
        "name": "wish",
        "id": 273,
        "accuracy": None,
        "priority": 0,
        "max_pp": 10,
        "power": None,
        "type": "normal",
        "damage_class": "status",
        "stat_changes": [],
        "effect_chance": None,
        "target": "user",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "unique",
                "url": "https://pokeapi.co/api/v2/move-category/13/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "User will recover half its max HP at the end of the next turn.",
        "flavor_text_entry": "A wish that restores HP. It takes time to work."
    },
    "refresh": {
        "name": "refresh",
        "id": 287,
        "accuracy": None,
        "priority": 0,
        "max_pp": 20,
        "power": None,
        "type": "normal",
        "damage_class": "status",
        "stat_changes": [],
        "effect_chance": None,
        "target": "user",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "unique",
                "url": "https://pokeapi.co/api/v2/move-category/13/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Cleanses the user of a burn, paralysis, or poison.",
        "flavor_text_entry": "Heals poisoning, paralysis, or a burn."
    },
    "calm-mind": {
        "name": "calm-mind",
        "id": 347,
        "accuracy": None,
        "priority": 0,
        "max_pp": 20,
        "power": None,
        "type": "psychic",
        "damage_class": "status",
        "stat_changes": [
            {
                "change": 1,
                "stat": {
                    "name": "SpAtk",
                    "url": "https://pokeapi.co/api/v2/stat/4/"
                }
            },
            {
                "change": 1,
                "stat": {
                    "name": "SpDef",
                    "url": "https://pokeapi.co/api/v2/stat/5/"
                }
            }
        ],
        "effect_chance": None,
        "target": "user",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "net-good-stats",
                "url": "https://pokeapi.co/api/v2/move-category/2/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Raises the user's Special Attack and Special Defense by one stage.",
        "flavor_text_entry": "Raises SP. ATK and SP. DEF by focusing the mind."
    },
    "trump-card": {
        "name": "trump-card",
        "id": 376,
        "accuracy": None,
        "priority": 0,
        "max_pp": 5,
        "power": None,
        "type": "normal",
        "damage_class": "special",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Power increases when this move has less PP, up to a maximum of 200.",
        "flavor_text_entry": "The fewer PP this move has, the greater its attack power."
    },
    "copycat": {
        "name": "copycat",
        "id": 383,
        "accuracy": None,
        "priority": 0,
        "max_pp": 20,
        "power": None,
        "type": "normal",
        "damage_class": "status",
        "stat_changes": [],
        "effect_chance": None,
        "target": "user",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "unique",
                "url": "https://pokeapi.co/api/v2/move-category/13/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Uses the target's last used move.",
        "flavor_text_entry": "The user mimics the move used immediately before it. The move fails if no other move has been used yet."
    },
    "stored-power": {
        "name": "stored-power",
        "id": 500,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 10,
        "power": 20,
        "type": "psychic",
        "damage_class": "special",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Power is higher the more the user's stats have been raised, to a maximum of 31\u00d7.",
        "flavor_text_entry": "The user attacks the target with stored power. The more the user\u2019s stats are raised, the greater the damage."
    },
    "moonlight": {
        "name": "moonlight",
        "id": 236,
        "accuracy": None,
        "priority": 0,
        "max_pp": 5,
        "power": None,
        "type": "fairy",
        "damage_class": "status",
        "stat_changes": [],
        "effect_chance": None,
        "target": "user",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "heal",
                "url": "https://pokeapi.co/api/v2/move-category/3/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 50,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Heals the user by half its max HP.  Affected by weather.",
        "flavor_text_entry": "Restores HP (varies by time)."
    },
    "rock-throw": {
        "name": "rock-throw",
        "id": 88,
        "accuracy": 90,
        "priority": 0,
        "max_pp": 15,
        "power": 50,
        "type": "rock",
        "damage_class": "physical",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Inflicts regular damage with no additional effect.",
        "flavor_text_entry": "Drops rocks on the enemy."
    },
    "tearful-look": {
        "name": "tearful-look",
        "id": 715,
        "accuracy": None,
        "priority": 0,
        "max_pp": 20,
        "power": None,
        "type": "normal",
        "damage_class": "status",
        "stat_changes": [
            {
                "change": -1,
                "stat": {
                    "name": "Atk",
                    "url": "https://pokeapi.co/api/v2/stat/2/"
                }
            },
            {
                "change": -1,
                "stat": {
                    "name": "SpAtk",
                    "url": "https://pokeapi.co/api/v2/stat/4/"
                }
            }
        ],
        "effect_chance": 100,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "net-good-stats",
                "url": "https://pokeapi.co/api/v2/move-category/2/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 100
        },
        "effect_entries": "Lowers the target's Attack and Special Attack by one stage.",
        "flavor_text_entry": "The user gets teary eyed to make the target lose its combative spirit. This lowers the target\u2019s Attack and Sp. Atk stats."
    },
    "wood-hammer": {
        "name": "wood-hammer",
        "id": 452,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 15,
        "power": 120,
        "type": "grass",
        "damage_class": "physical",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 0,
            "drain": -33,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "User receives 1/3 the damage inflicted in recoil.",
        "flavor_text_entry": "The user slams its rugged body into the foe to attack. The user also sustains serious damage."
    },
    "head-smash": {
        "name": "head-smash",
        "id": 457,
        "accuracy": 80,
        "priority": 0,
        "max_pp": 5,
        "power": 150,
        "type": "rock",
        "damage_class": "physical",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 0,
            "drain": -50,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "User receives 1/2 the damage inflicted in recoil.",
        "flavor_text_entry": "The user delivers a life-endangering head butt at full power. The user also takes terrible damage."
    },
    "water-pledge": {
        "name": "water-pledge",
        "id": 518,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 10,
        "power": 80,
        "type": "water",
        "damage_class": "special",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "With Grass Pledge, halves opposing Pok\u00e9mon's Speed for four turns.",
        "flavor_text_entry": "A column of water strikes the target. When combined with its fire equivalent, the damage increases and a rainbow appears."
    },
    "hydro-cannon": {
        "name": "hydro-cannon",
        "id": 308,
        "accuracy": 90,
        "priority": 0,
        "max_pp": 5,
        "power": 150,
        "type": "water",
        "damage_class": "special",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "User foregoes its next turn to recharge.",
        "flavor_text_entry": "Powerful, but leaves the user immobile the next turn."
    },
    "whirlwind": {
        "name": "whirlwind",
        "id": 18,
        "accuracy": None,
        "priority": -6,
        "max_pp": 20,
        "power": None,
        "type": "normal",
        "damage_class": "status",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "force-switch",
                "url": "https://pokeapi.co/api/v2/move-category/12/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Immediately ends wild battles.  Forces trainers to switch Pok\u00e9mon.",
        "flavor_text_entry": "Blows away the foe & ends battle."
    },
    "peck": {
        "name": "peck",
        "id": 64,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 35,
        "power": 35,
        "type": "flying",
        "damage_class": "physical",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Inflicts regular damage with no additional effect.",
        "flavor_text_entry": "Jabs the foe with a beak, etc."
    },
    "confusion": {
        "name": "confusion",
        "id": 93,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 25,
        "power": 50,
        "type": "psychic",
        "damage_class": "special",
        "stat_changes": [],
        "effect_chance": 10,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "confusion",
                "url": "https://pokeapi.co/api/v2/move-ailment/6/"
            },
            "ailment_chance": 10,
            "category": {
                "name": "damage+ailment",
                "url": "https://pokeapi.co/api/v2/move-category/4/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": 5,
            "min_hits": None,
            "min_turns": 2,
            "stat_chance": 0
        },
        "effect_entries": "Has a 10% chance to confuse the target.",
        "flavor_text_entry": "An attack that may cause confusion."
    },
    "hypnosis": {
        "name": "hypnosis",
        "id": 95,
        "accuracy": 60,
        "priority": 0,
        "max_pp": 20,
        "power": None,
        "type": "psychic",
        "damage_class": "status",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "sleep",
                "url": "https://pokeapi.co/api/v2/move-ailment/2/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "ailment",
                "url": "https://pokeapi.co/api/v2/move-category/1/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": 4,
            "min_hits": None,
            "min_turns": 2,
            "stat_chance": 0
        },
        "effect_entries": "Puts the target to sleep.",
        "flavor_text_entry": "May put the foe to sleep."
    },
    "night-shade": {
        "name": "night-shade",
        "id": 101,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 15,
        "power": None,
        "type": "ghost",
        "damage_class": "special",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Inflicts damage equal to the user's level.",
        "flavor_text_entry": "The user's level equals damage HP."
    },
    "mirror-move": {
        "name": "mirror-move",
        "id": 119,
        "accuracy": None,
        "priority": 0,
        "max_pp": 20,
        "power": None,
        "type": "flying",
        "damage_class": "status",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "unique",
                "url": "https://pokeapi.co/api/v2/move-category/13/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Uses the target's last used move.",
        "flavor_text_entry": "Counters with the same move."
    },
    "foresight": {
        "name": "foresight",
        "id": 193,
        "accuracy": None,
        "priority": 0,
        "max_pp": 40,
        "power": None,
        "type": "normal",
        "damage_class": "status",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "no-type-immunity",
                "url": "https://pokeapi.co/api/v2/move-ailment/17/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "ailment",
                "url": "https://pokeapi.co/api/v2/move-category/1/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Forces the target to have no Evade, and allows it to be hit by Normal and Fighting moves even if it's a Ghost.",
        "flavor_text_entry": "Negates accuracy reduction moves."
    },
    "psycho-shift": {
        "name": "psycho-shift",
        "id": 375,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 10,
        "power": None,
        "type": "psychic",
        "damage_class": "status",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "unique",
                "url": "https://pokeapi.co/api/v2/move-category/13/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Transfers the user's major status effect to the target.",
        "flavor_text_entry": "Using its psychic power of suggestion, the user transfers its status problems to the target."
    },
    "future-sight": {
        "name": "future-sight",
        "id": 248,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 10,
        "power": 120,
        "type": "psychic",
        "damage_class": "special",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "unique",
                "url": "https://pokeapi.co/api/v2/move-category/13/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Hits the target two turns later.",
        "flavor_text_entry": "An attack that hits on 3rd turn."
    },
    "sing": {
        "name": "sing",
        "id": 47,
        "accuracy": 55,
        "priority": 0,
        "max_pp": 15,
        "power": None,
        "type": "normal",
        "damage_class": "status",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "sleep",
                "url": "https://pokeapi.co/api/v2/move-ailment/2/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "ailment",
                "url": "https://pokeapi.co/api/v2/move-category/1/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": 4,
            "min_hits": None,
            "min_turns": 2,
            "stat_chance": 0
        },
        "effect_entries": "Puts the target to sleep.",
        "flavor_text_entry": "May cause the foe to fall asleep."
    },
    "bubble": {
        "name": "bubble",
        "id": 145,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 30,
        "power": 40,
        "type": "water",
        "damage_class": "special",
        "stat_changes": [
            {
                "change": -1,
                "stat": {
                    "name": "Speed",
                    "url": "https://pokeapi.co/api/v2/stat/6/"
                }
            }
        ],
        "effect_chance": 10,
        "target": "all-opponents",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage+lower",
                "url": "https://pokeapi.co/api/v2/move-category/6/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 10
        },
        "effect_entries": "Has a 10% chance to lower the target's Speed by one stage.",
        "flavor_text_entry": "An attack that may reduce SPEED."
    },
    "perish-song": {
        "name": "perish-song",
        "id": 195,
        "accuracy": None,
        "priority": 0,
        "max_pp": 5,
        "power": None,
        "type": "normal",
        "damage_class": "status",
        "stat_changes": [],
        "effect_chance": None,
        "target": "all-pokemon",
        "meta": {
            "ailment": {
                "name": "perish-song",
                "url": "https://pokeapi.co/api/v2/move-ailment/20/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "ailment",
                "url": "https://pokeapi.co/api/v2/move-category/1/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": 4,
            "min_hits": None,
            "min_turns": 4,
            "stat_chance": 0
        },
        "effect_entries": "User and target both faint after three turns.",
        "flavor_text_entry": "Both user and foe faint in 3 turns."
    },
    "disarming-voice": {
        "name": "disarming-voice",
        "id": 574,
        "accuracy": None,
        "priority": 0,
        "max_pp": 15,
        "power": 40,
        "type": "fairy",
        "damage_class": "special",
        "stat_changes": [],
        "effect_chance": None,
        "target": "all-opponents",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Never misses.",
        "flavor_text_entry": "Letting out a charming cry, the user does emotional damage to opposing Pok\u00e9mon. This attack never misses."
    },
    "misty-terrain": {
        "name": "misty-terrain",
        "id": 581,
        "accuracy": None,
        "priority": 0,
        "max_pp": 10,
        "power": None,
        "type": "fairy",
        "damage_class": "status",
        "stat_changes": [],
        "effect_chance": None,
        "target": "entire-field",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "whole-field-effect",
                "url": "https://pokeapi.co/api/v2/move-category/10/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "For five turns, protects all Pok\u00e9mon on the ground from major status ailments and confusion, and halves the power of incoming dragon moves.",
        "flavor_text_entry": "The user covers the ground under everyone\u2019s feet with mist for five turns. This protects Pok\u00e9mon on the ground from status conditions."
    },
    "misty-explosion": {
        "name": "misty-explosion",
        "id": 802,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 5,
        "power": 100,
        "type": "fairy",
        "damage_class": "special",
        "stat_changes": [],
        "effect_chance": None,
        "target": "all-other-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Inflicts regular damage with no additional effect.",
        "flavor_text_entry": "The user attacks everything around it and faints upon using this move. This move\u2019s power is increased on Misty Terrain."
    },
    "ice-shard": {
        "name": "ice-shard",
        "id": 420,
        "accuracy": 100,
        "priority": 1,
        "max_pp": 30,
        "power": 40,
        "type": "ice",
        "damage_class": "physical",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Inflicts regular damage with no additional effect.",
        "flavor_text_entry": "The user flash freezes chunks of ice and hurls them. This move always goes first."
    },
    "icicle-crash": {
        "name": "icicle-crash",
        "id": 556,
        "accuracy": 90,
        "priority": 0,
        "max_pp": 10,
        "power": 85,
        "type": "ice",
        "damage_class": "physical",
        "stat_changes": [],
        "effect_chance": 30,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 30,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Has a 30% chance to make the target flinch.",
        "flavor_text_entry": "The user attacks by harshly dropping an icicle onto the target. It may also make the target flinch."
    },
    "freeze-dry": {
        "name": "freeze-dry",
        "id": 573,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 20,
        "power": 70,
        "type": "ice",
        "damage_class": "special",
        "stat_changes": [],
        "effect_chance": 10,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "freeze",
                "url": "https://pokeapi.co/api/v2/move-ailment/3/"
            },
            "ailment_chance": 10,
            "category": {
                "name": "damage+ailment",
                "url": "https://pokeapi.co/api/v2/move-category/4/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Super-effective against water.",
        "flavor_text_entry": "The user rapidly cools the target. This may also leave the target frozen. This move is super effective on Water types."
    },
    "horn-attack": {
        "name": "horn-attack",
        "id": 30,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 25,
        "power": 65,
        "type": "normal",
        "damage_class": "physical",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Inflicts regular damage with no additional effect.",
        "flavor_text_entry": "An attack using a horn to jab."
    },
    "fury-attack": {
        "name": "fury-attack",
        "id": 31,
        "accuracy": 85,
        "priority": 0,
        "max_pp": 20,
        "power": 15,
        "type": "normal",
        "damage_class": "physical",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": 5,
            "max_turns": None,
            "min_hits": 2,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Hits 2-5 times in one turn.",
        "flavor_text_entry": "Jabs the target 2-5 times."
    },
    "mach-punch": {
        "name": "mach-punch",
        "id": 183,
        "accuracy": 100,
        "priority": 1,
        "max_pp": 30,
        "power": 40,
        "type": "fighting",
        "damage_class": "physical",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Inflicts regular damage with no additional effect.",
        "flavor_text_entry": "A fast punch that lands first."
    },
    "vacuum-wave": {
        "name": "vacuum-wave",
        "id": 410,
        "accuracy": 100,
        "priority": 1,
        "max_pp": 30,
        "power": 40,
        "type": "fighting",
        "damage_class": "special",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Inflicts regular damage with no additional effect.",
        "flavor_text_entry": "The user whirls its fists to send a wave of pure vacuum at the foe. This move always goes first."
    },
    "bullet-punch": {
        "name": "bullet-punch",
        "id": 418,
        "accuracy": 100,
        "priority": 1,
        "max_pp": 30,
        "power": 40,
        "type": "steel",
        "damage_class": "physical",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Inflicts regular damage with no additional effect.",
        "flavor_text_entry": "The user strikes with a tough punch as fast as a bullet. This move always goes first."
    },
    "upper-hand": {
        "name": "upper-hand",
        "id": 918,
        "accuracy": 100,
        "priority": 3,
        "max_pp": 15,
        "power": 65,
        "type": "fighting",
        "damage_class": "physical",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": None
    },
    "darkest-lariat": {
        "name": "darkest-lariat",
        "id": 663,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 10,
        "power": 85,
        "type": "dark",
        "damage_class": "physical",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Ignores the target's stat modifiers.",
        "flavor_text_entry": "The user swings both arms and hits the target. The target\u2019s stat changes don\u2019t affect this attack\u2019s damage."
    },
    "lucky-chant": {
        "name": "lucky-chant",
        "id": 381,
        "accuracy": None,
        "priority": 0,
        "max_pp": 30,
        "power": None,
        "type": "normal",
        "damage_class": "status",
        "stat_changes": [],
        "effect_chance": None,
        "target": "users-field",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "field-effect",
                "url": "https://pokeapi.co/api/v2/move-category/11/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Prevents the target from scoring critical hits for five turns.",
        "flavor_text_entry": "The user chants an incantation toward the sky, preventing the foe from landing critical hits."
    },
    "simple-beam": {
        "name": "simple-beam",
        "id": 493,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 15,
        "power": None,
        "type": "normal",
        "damage_class": "status",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "unique",
                "url": "https://pokeapi.co/api/v2/move-category/13/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Changes the target's ability to Simple.",
        "flavor_text_entry": "The user\u2019s mysterious psychic wave changes the target\u2019s Ability to Simple."
    },
    "psychic-terrain": {
        "name": "psychic-terrain",
        "id": 678,
        "accuracy": None,
        "priority": 0,
        "max_pp": 10,
        "power": None,
        "type": "psychic",
        "damage_class": "status",
        "stat_changes": [],
        "effect_chance": None,
        "target": "entire-field",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "whole-field-effect",
                "url": "https://pokeapi.co/api/v2/move-category/10/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Protects Pok\u00e9mon on the ground from priority moves and increases the power of their  Psychic moves by 50%.",
        "flavor_text_entry": "This protects Pok\u00e9mon on the ground from priority moves and powers up Psychic-type moves for five turns."
    },
    "acid": {
        "name": "acid",
        "id": 51,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 30,
        "power": 40,
        "type": "poison",
        "damage_class": "special",
        "stat_changes": [
            {
                "change": -1,
                "stat": {
                    "name": "SpDef",
                    "url": "https://pokeapi.co/api/v2/stat/5/"
                }
            }
        ],
        "effect_chance": 10,
        "target": "all-opponents",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage+lower",
                "url": "https://pokeapi.co/api/v2/move-category/6/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 10
        },
        "effect_entries": "Has a 10% chance to lower the target's Special Defense by one stage.",
        "flavor_text_entry": "An attack that may lower DEFENSE."
    },
    "needle-arm": {
        "name": "needle-arm",
        "id": 302,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 15,
        "power": 60,
        "type": "grass",
        "damage_class": "physical",
        "stat_changes": [],
        "effect_chance": 30,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 30,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Has a 30% chance to make the target flinch.",
        "flavor_text_entry": "Attacks with thorny arms. May cause flinching."
    },
    "switcheroo": {
        "name": "switcheroo",
        "id": 415,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 10,
        "power": None,
        "type": "dark",
        "damage_class": "status",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "unique",
                "url": "https://pokeapi.co/api/v2/move-category/13/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "User and target swap items.",
        "flavor_text_entry": "The user trades held items with the foe faster than the eye can follow. "
    },
    "power-trip": {
        "name": "power-trip",
        "id": 681,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 10,
        "power": 20,
        "type": "dark",
        "damage_class": "physical",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Power is higher the more the user's stats have been raised, to a maximum of 31\u00d7.",
        "flavor_text_entry": "The user boasts its strength and attacks the target. The more the user\u2019s stats are raised, the greater the move\u2019s power."
    },
    "spiky-shield": {
        "name": "spiky-shield",
        "id": 596,
        "accuracy": None,
        "priority": 4,
        "max_pp": 10,
        "power": None,
        "type": "grass",
        "damage_class": "status",
        "stat_changes": [],
        "effect_chance": None,
        "target": "user",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "unique",
                "url": "https://pokeapi.co/api/v2/move-category/13/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Blocks damaging attacks and damages attacking Pok\u00e9mon for 1/8 their max HP.",
        "flavor_text_entry": "In addition to protecting the user from attacks, this move also damages any attacker who makes direct contact."
    },
    "vice-grip": {
        "name": "vice-grip",
        "id": 11,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 30,
        "power": 55,
        "type": "normal",
        "damage_class": "physical",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Inflicts regular damage with no additional effect.",
        "flavor_text_entry": "Grips with power\u00ad ful pincers."
    },
    "guillotine": {
        "name": "guillotine",
        "id": 12,
        "accuracy": 30,
        "priority": 0,
        "max_pp": 5,
        "power": None,
        "type": "normal",
        "damage_class": "physical",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "ohko",
                "url": "https://pokeapi.co/api/v2/move-category/9/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Causes a one-hit KO.",
        "flavor_text_entry": "A one-hit KO, pincer attack."
    },
    "crabhammer": {
        "name": "crabhammer",
        "id": 152,
        "accuracy": 90,
        "priority": 0,
        "max_pp": 10,
        "power": 100,
        "type": "water",
        "damage_class": "physical",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 1,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Has an increased chance for a critical hit.",
        "flavor_text_entry": "Has a high criti\u00ad cal hit ratio."
    },
    "razor-shell": {
        "name": "razor-shell",
        "id": 534,
        "accuracy": 95,
        "priority": 0,
        "max_pp": 10,
        "power": 75,
        "type": "water",
        "damage_class": "physical",
        "stat_changes": [
            {
                "change": -1,
                "stat": {
                    "name": "Def",
                    "url": "https://pokeapi.co/api/v2/stat/3/"
                }
            }
        ],
        "effect_chance": 50,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage+lower",
                "url": "https://pokeapi.co/api/v2/move-category/6/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 50
        },
        "effect_entries": "Has a 50% chance to lower the target's Defense by one stage.",
        "flavor_text_entry": "The user cuts its target with sharp shells. This attack may also lower the target\u2019s Defense stat."
    },
    "coil": {
        "name": "coil",
        "id": 489,
        "accuracy": None,
        "priority": 0,
        "max_pp": 20,
        "power": None,
        "type": "poison",
        "damage_class": "status",
        "stat_changes": [
            {
                "change": 1,
                "stat": {
                    "name": "Atk",
                    "url": "https://pokeapi.co/api/v2/stat/2/"
                }
            },
            {
                "change": 1,
                "stat": {
                    "name": "Def",
                    "url": "https://pokeapi.co/api/v2/stat/3/"
                }
            },
            {
                "change": 1,
                "stat": {
                    "name": "accuracy",
                    "url": "https://pokeapi.co/api/v2/stat/7/"
                }
            }
        ],
        "effect_chance": None,
        "target": "user",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "net-good-stats",
                "url": "https://pokeapi.co/api/v2/move-category/2/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Raises the user's Attack, Defense, and accuracy by one stage each.",
        "flavor_text_entry": "The user coils up and concentrates. This raises its Attack and Defense stats as well as its accuracy."
    },
    "withdraw": {
        "name": "withdraw",
        "id": 110,
        "accuracy": None,
        "priority": 0,
        "max_pp": 40,
        "power": None,
        "type": "water",
        "damage_class": "status",
        "stat_changes": [
            {
                "change": 1,
                "stat": {
                    "name": "Def",
                    "url": "https://pokeapi.co/api/v2/stat/3/"
                }
            }
        ],
        "effect_chance": None,
        "target": "user",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "net-good-stats",
                "url": "https://pokeapi.co/api/v2/move-category/2/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Raises the user's Defense by one stage.",
        "flavor_text_entry": "Heightens the user's DEFENSE."
    },
    "shell-smash": {
        "name": "shell-smash",
        "id": 504,
        "accuracy": None,
        "priority": 0,
        "max_pp": 15,
        "power": None,
        "type": "normal",
        "damage_class": "status",
        "stat_changes": [
            {
                "change": -1,
                "stat": {
                    "name": "Def",
                    "url": "https://pokeapi.co/api/v2/stat/3/"
                }
            },
            {
                "change": -1,
                "stat": {
                    "name": "SpDef",
                    "url": "https://pokeapi.co/api/v2/stat/5/"
                }
            },
            {
                "change": 2,
                "stat": {
                    "name": "Atk",
                    "url": "https://pokeapi.co/api/v2/stat/2/"
                }
            },
            {
                "change": 2,
                "stat": {
                    "name": "SpAtk",
                    "url": "https://pokeapi.co/api/v2/stat/4/"
                }
            },
            {
                "change": 2,
                "stat": {
                    "name": "Speed",
                    "url": "https://pokeapi.co/api/v2/stat/6/"
                }
            }
        ],
        "effect_chance": None,
        "target": "user",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "unique",
                "url": "https://pokeapi.co/api/v2/move-category/13/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Raises user's Attack, Special Attack, and Speed by two stages.  Lower user's Defense and Special Defense by one stage.",
        "flavor_text_entry": "The user breaks its shell, lowering its Defense and Sp. Def stats but sharply raising Attack, Sp. Atk, and Speed stats."
    },
    "grass-pledge": {
        "name": "grass-pledge",
        "id": 520,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 10,
        "power": 80,
        "type": "grass",
        "damage_class": "special",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "With Fire Pledge, damages opposing Pok\u00e9mon for 1/8 their max HP every turn for four turns.",
        "flavor_text_entry": "A column of grass hits opposing Pok\u00e9mon. When used with its water equivalent, its damage increases into a vast swamp."
    },
    "leafage": {
        "name": "leafage",
        "id": 670,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 40,
        "power": 40,
        "type": "grass",
        "damage_class": "physical",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Inflicts regular damage with no additional effect.",
        "flavor_text_entry": "The user attacks by pelting the target with leaves."
    },
    "frenzy-plant": {
        "name": "frenzy-plant",
        "id": 338,
        "accuracy": 90,
        "priority": 0,
        "max_pp": 5,
        "power": 150,
        "type": "grass",
        "damage_class": "special",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "User foregoes its next turn to recharge.",
        "flavor_text_entry": "Powerful, but leaves the user immobile the next turn."
    },
    "scorching-sands": {
        "name": "scorching-sands",
        "id": 815,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 10,
        "power": 70,
        "type": "ground",
        "damage_class": "special",
        "stat_changes": [],
        "effect_chance": 30,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "burn",
                "url": "https://pokeapi.co/api/v2/move-ailment/4/"
            },
            "ailment_chance": 30,
            "category": {
                "name": "damage+ailment",
                "url": "https://pokeapi.co/api/v2/move-category/4/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Inflicts regular damage with no additional effect.",
        "flavor_text_entry": "The user throws scorching sand at the target to attack. This may also leave the target with a burn."
    },
    "headlong-rush": {
        "name": "headlong-rush",
        "id": 838,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 5,
        "power": 120,
        "type": "ground",
        "damage_class": "physical",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": None
    },
    "me-first": {
        "name": "me-first",
        "id": 382,
        "accuracy": None,
        "priority": 0,
        "max_pp": 20,
        "power": None,
        "type": "normal",
        "damage_class": "status",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon-me-first",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Uses the target's move against it before it attacks, with power increased by half.",
        "flavor_text_entry": "The user tries to cut ahead of the foe to steal and use the foe\u2019s intended move with greater power."
    },
    "tail-slap": {
        "name": "tail-slap",
        "id": 541,
        "accuracy": 85,
        "priority": 0,
        "max_pp": 10,
        "power": 25,
        "type": "normal",
        "damage_class": "physical",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": 5,
            "max_turns": None,
            "min_hits": 2,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Hits 2-5 times in one turn.",
        "flavor_text_entry": "The user attacks by striking the target with its hard tail. It hits the target two to five times in a row."
    },
    "wave-crash": {
        "name": "wave-crash",
        "id": 834,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 10,
        "power": 120,
        "type": "water",
        "damage_class": "physical",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": None
    },
    "constrict": {
        "name": "constrict",
        "id": 132,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 35,
        "power": 10,
        "type": "normal",
        "damage_class": "physical",
        "stat_changes": [
            {
                "change": -1,
                "stat": {
                    "name": "Speed",
                    "url": "https://pokeapi.co/api/v2/stat/6/"
                }
            }
        ],
        "effect_chance": 10,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage+lower",
                "url": "https://pokeapi.co/api/v2/move-category/6/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 10
        },
        "effect_entries": "Has a 10% chance to lower the target's Speed by one stage.",
        "flavor_text_entry": "An attack that may lower SPEED."
    },
    "phantom-force": {
        "name": "phantom-force",
        "id": 566,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 10,
        "power": 90,
        "type": "ghost",
        "damage_class": "physical",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "User vanishes, dodging all attacks, and hits next turn.  Hits through Protect and Detect.",
        "flavor_text_entry": "The user vanishes somewhere, then strikes the target on the next turn. This move hits even if the target protects itself."
    },
    "strength-sap": {
        "name": "strength-sap",
        "id": 668,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 10,
        "power": None,
        "type": "grass",
        "damage_class": "status",
        "stat_changes": [
            {
                "change": -1,
                "stat": {
                    "name": "Atk",
                    "url": "https://pokeapi.co/api/v2/stat/2/"
                }
            }
        ],
        "effect_chance": 100,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "unique",
                "url": "https://pokeapi.co/api/v2/move-category/13/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 100
        },
        "effect_entries": "Heals the user by the target's current Attack stat and lowers the target's Attack by one stage.",
        "flavor_text_entry": "The user restores its HP by the same amount as the target\u2019s Attack stat. It also lowers the target\u2019s Attack stat."
    },
    "sky-uppercut": {
        "name": "sky-uppercut",
        "id": 327,
        "accuracy": 90,
        "priority": 0,
        "max_pp": 15,
        "power": 85,
        "type": "fighting",
        "damage_class": "physical",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Inflicts regular damage and can hit Bounce and Fly users.",
        "flavor_text_entry": "An uppercut thrown as if leaping into the sky."
    },
    "healing-wish": {
        "name": "healing-wish",
        "id": 361,
        "accuracy": None,
        "priority": 0,
        "max_pp": 10,
        "power": None,
        "type": "psychic",
        "damage_class": "status",
        "stat_changes": [],
        "effect_chance": None,
        "target": "user",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "unique",
                "url": "https://pokeapi.co/api/v2/move-category/13/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "User faints.  Its replacement has its HP fully restored and any major status effect removed.",
        "flavor_text_entry": "The user faints. In return, the Pok\u00e9mon taking its place will have its HP restored and status cured."
    },
    "entrainment": {
        "name": "entrainment",
        "id": 494,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 15,
        "power": None,
        "type": "normal",
        "damage_class": "status",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "unique",
                "url": "https://pokeapi.co/api/v2/move-category/13/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Copies the user's ability onto the target.",
        "flavor_text_entry": "The user dances with an odd rhythm that compels the target to mimic it, making the target\u2019s Ability the same as the user\u2019s."
    },
    "circle-throw": {
        "name": "circle-throw",
        "id": 509,
        "accuracy": 90,
        "priority": -6,
        "max_pp": 10,
        "power": 60,
        "type": "fighting",
        "damage_class": "physical",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Ends wild battles.  Forces trainers to switch Pok\u00e9mon.",
        "flavor_text_entry": "The user throws the target and drags out another Pok\u00e9mon in its party. In the wild, the battle ends."
    },
    "aura-sphere": {
        "name": "aura-sphere",
        "id": 396,
        "accuracy": None,
        "priority": 0,
        "max_pp": 20,
        "power": 80,
        "type": "fighting",
        "damage_class": "special",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Never misses.",
        "flavor_text_entry": "The user looses a blast of aura power from deep within its body. This move is certain to hit."
    },
    "poltergeist": {
        "name": "poltergeist",
        "id": 809,
        "accuracy": 90,
        "priority": 0,
        "max_pp": 5,
        "power": 110,
        "type": "ghost",
        "damage_class": "physical",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Inflicts regular damage with no additional effect.",
        "flavor_text_entry": "The user attacks the target by controlling the target\u2019s item. The move fails if the target doesn\u2019t have an item."
    },
    "magnitude": {
        "name": "magnitude",
        "id": 222,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 30,
        "power": None,
        "type": "ground",
        "damage_class": "physical",
        "stat_changes": [],
        "effect_chance": None,
        "target": "all-other-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Power varies randomly from 10 to 150.",
        "flavor_text_entry": "A ground attack with random power."
    },
    "submission": {
        "name": "submission",
        "id": 66,
        "accuracy": 80,
        "priority": 0,
        "max_pp": 20,
        "power": 80,
        "type": "fighting",
        "damage_class": "physical",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 0,
            "drain": -25,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "User receives 1/4 the damage it inflicts in recoil.",
        "flavor_text_entry": "An attack that al\u00ad so hurts the user."
    },
    "cotton-guard": {
        "name": "cotton-guard",
        "id": 538,
        "accuracy": None,
        "priority": 0,
        "max_pp": 10,
        "power": None,
        "type": "grass",
        "damage_class": "status",
        "stat_changes": [
            {
                "change": 3,
                "stat": {
                    "name": "Def",
                    "url": "https://pokeapi.co/api/v2/stat/3/"
                }
            }
        ],
        "effect_chance": None,
        "target": "user",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "net-good-stats",
                "url": "https://pokeapi.co/api/v2/move-category/2/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Raises the user's Defense by three stages.",
        "flavor_text_entry": "The user protects itself by wrapping its body in soft cotton, drastically raising the user\u2019s Defense stat."
    },
    "fairy-wind": {
        "name": "fairy-wind",
        "id": 584,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 30,
        "power": 40,
        "type": "fairy",
        "damage_class": "special",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Inflicts regular damage with no additional effect.",
        "flavor_text_entry": "The user stirs up a fairy wind and strikes the target with it."
    },
    "final-gambit": {
        "name": "final-gambit",
        "id": 515,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 5,
        "power": None,
        "type": "fighting",
        "damage_class": "special",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Inflicts damage equal to the user's remaining HP.  User faints.",
        "flavor_text_entry": "The user risks everything to attack its target. The user faints but does damage equal to the user\u2019s HP."
    },
    "quick-guard": {
        "name": "quick-guard",
        "id": 501,
        "accuracy": None,
        "priority": 3,
        "max_pp": 15,
        "power": None,
        "type": "fighting",
        "damage_class": "status",
        "stat_changes": [],
        "effect_chance": None,
        "target": "users-field",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "field-effect",
                "url": "https://pokeapi.co/api/v2/move-category/11/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Prevents any priority moves from hitting friendly Pok\u00e9mon this turn.",
        "flavor_text_entry": "The user protects itself and its allies from priority moves. If used in succession, its chance of failing rises."
    },
    "dual-chop": {
        "name": "dual-chop",
        "id": 530,
        "accuracy": 90,
        "priority": 0,
        "max_pp": 15,
        "power": 40,
        "type": "dragon",
        "damage_class": "physical",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": 2,
            "max_turns": None,
            "min_hits": 2,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Hits twice in one turn.",
        "flavor_text_entry": "The user attacks its target by hitting it with brutal strikes. The target is hit twice in a row."
    },
    "coaching": {
        "name": "coaching",
        "id": 811,
        "accuracy": None,
        "priority": 0,
        "max_pp": 10,
        "power": None,
        "type": "fighting",
        "damage_class": "status",
        "stat_changes": [
            {
                "change": 1,
                "stat": {
                    "name": "Atk",
                    "url": "https://pokeapi.co/api/v2/stat/2/"
                }
            },
            {
                "change": 1,
                "stat": {
                    "name": "Def",
                    "url": "https://pokeapi.co/api/v2/stat/3/"
                }
            }
        ],
        "effect_chance": 100,
        "target": "user-and-allies",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "net-good-stats",
                "url": "https://pokeapi.co/api/v2/move-category/2/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 100
        },
        "effect_entries": "Inflicts regular damage with no additional effect.",
        "flavor_text_entry": "The user properly coaches its ally Pok\u00e9mon, boosting their Attack and Defense stats."
    },
    "head-charge": {
        "name": "head-charge",
        "id": 543,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 15,
        "power": 120,
        "type": "normal",
        "damage_class": "physical",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 0,
            "drain": -25,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "User receives 1/4 the damage it inflicts in recoil.",
        "flavor_text_entry": "The user charges its head into its target, using its powerful guard hair. It also damages the user a little."
    },
    "terrain-pulse": {
        "name": "terrain-pulse",
        "id": 805,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 10,
        "power": 50,
        "type": "normal",
        "damage_class": "special",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Inflicts regular damage with no additional effect.",
        "flavor_text_entry": "The user utilizes the power of the terrain to attack. This move\u2019s type and power changes depending on the terrain when it\u2019s used."
    },
    "heal-pulse": {
        "name": "heal-pulse",
        "id": 505,
        "accuracy": None,
        "priority": 0,
        "max_pp": 10,
        "power": None,
        "type": "psychic",
        "damage_class": "status",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "heal",
                "url": "https://pokeapi.co/api/v2/move-category/3/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 50,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Heals the target for half its max HP.",
        "flavor_text_entry": "The user emits a healing pulse which restores the target\u2019s HP by up to half of its max HP."
    },
    "karate-chop": {
        "name": "karate-chop",
        "id": 2,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 25,
        "power": 50,
        "type": "fighting",
        "damage_class": "physical",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 1,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Has an increased chance for a critical hit.",
        "flavor_text_entry": "Has a high criti\u00ad cal hit ratio."
    },
    "flying-press": {
        "name": "flying-press",
        "id": 560,
        "accuracy": 95,
        "priority": 0,
        "max_pp": 10,
        "power": 100,
        "type": "fighting",
        "damage_class": "physical",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Deals both fighting and flying-type damage.",
        "flavor_text_entry": "The user dives down onto the target from the sky. This move is Fighting and Flying type simultaneously."
    },
    "heal-block": {
        "name": "heal-block",
        "id": 377,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 15,
        "power": None,
        "type": "psychic",
        "damage_class": "status",
        "stat_changes": [],
        "effect_chance": None,
        "target": "all-opponents",
        "meta": {
            "ailment": {
                "name": "heal-block",
                "url": "https://pokeapi.co/api/v2/move-ailment/15/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "ailment",
                "url": "https://pokeapi.co/api/v2/move-category/1/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": 5,
            "min_hits": None,
            "min_turns": 5,
            "stat_chance": 0
        },
        "effect_entries": "Prevents target from restoring its HP for five turns.",
        "flavor_text_entry": "The user prevents the foe from using any HP-recovery moves for five turns. "
    },
    "magic-room": {
        "name": "magic-room",
        "id": 478,
        "accuracy": None,
        "priority": 0,
        "max_pp": 10,
        "power": None,
        "type": "psychic",
        "damage_class": "status",
        "stat_changes": [],
        "effect_chance": None,
        "target": "entire-field",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "whole-field-effect",
                "url": "https://pokeapi.co/api/v2/move-category/10/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Negates held items for five turns.",
        "flavor_text_entry": "The user creates a bizarre area in which Pok\u00e9mon\u2019s held items lose their effects for five turns."
    },
    "crafty-shield": {
        "name": "crafty-shield",
        "id": 578,
        "accuracy": None,
        "priority": 3,
        "max_pp": 10,
        "power": None,
        "type": "fairy",
        "damage_class": "status",
        "stat_changes": [],
        "effect_chance": None,
        "target": "users-field",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "field-effect",
                "url": "https://pokeapi.co/api/v2/move-category/11/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Protects all friendly Pok\u00e9mon from non-damaging moves.",
        "flavor_text_entry": "The user protects itself and its allies from status moves with a mysterious power. This does not stop moves that do damage."
    },
    "fairy-lock": {
        "name": "fairy-lock",
        "id": 587,
        "accuracy": None,
        "priority": 0,
        "max_pp": 10,
        "power": None,
        "type": "fairy",
        "damage_class": "status",
        "stat_changes": [],
        "effect_chance": None,
        "target": "entire-field",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "whole-field-effect",
                "url": "https://pokeapi.co/api/v2/move-category/10/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Prevents all Pok\u00e9mon from fleeing or switching out during the next turn.",
        "flavor_text_entry": "By locking down the battlefield, the user keeps all Pok\u00e9mon from fleeing during the next turn."
    },
    "leaf-blade": {
        "name": "leaf-blade",
        "id": 348,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 15,
        "power": 90,
        "type": "grass",
        "damage_class": "physical",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 1,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Has an increased chance for a critical hit.",
        "flavor_text_entry": "Slashes with a sharp leaf. High critical-hit ratio."
    },
    "spirit-shackle": {
        "name": "spirit-shackle",
        "id": 662,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 10,
        "power": 80,
        "type": "ghost",
        "damage_class": "physical",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Traps the target.",
        "flavor_text_entry": "The user attacks while simultaneously stitching the target\u2019s shadow to the ground to prevent the target from escaping."
    },
    "force-palm": {
        "name": "force-palm",
        "id": 395,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 10,
        "power": 60,
        "type": "fighting",
        "damage_class": "physical",
        "stat_changes": [],
        "effect_chance": 30,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "paralysis",
                "url": "https://pokeapi.co/api/v2/move-ailment/1/"
            },
            "ailment_chance": 30,
            "category": {
                "name": "damage+ailment",
                "url": "https://pokeapi.co/api/v2/move-category/4/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Has a 30% chance to paralyze the target.",
        "flavor_text_entry": "The foe is attacked with a shock wave. It may also leave the target paralyzed. "
    },
    "shore-up": {
        "name": "shore-up",
        "id": 659,
        "accuracy": None,
        "priority": 0,
        "max_pp": 5,
        "power": None,
        "type": "ground",
        "damage_class": "status",
        "stat_changes": [],
        "effect_chance": None,
        "target": "user",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "heal",
                "url": "https://pokeapi.co/api/v2/move-category/3/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 50,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Heals the user for \u00bd its max HP, or \u2154 during a sandstorm.",
        "flavor_text_entry": "The user regains up to half of its max HP. It restores more HP in a sandstorm."
    },
    "twineedle": {
        "name": "twineedle",
        "id": 41,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 20,
        "power": 25,
        "type": "bug",
        "damage_class": "physical",
        "stat_changes": [],
        "effect_chance": 20,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "poison",
                "url": "https://pokeapi.co/api/v2/move-ailment/5/"
            },
            "ailment_chance": 20,
            "category": {
                "name": "damage+ailment",
                "url": "https://pokeapi.co/api/v2/move-category/4/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": 2,
            "max_turns": None,
            "min_hits": 2,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Hits twice in the same turn.  Has a 20% chance to poison the target.",
        "flavor_text_entry": "Jabs the foe twice using stingers."
    },
    "zing-zap": {
        "name": "zing-zap",
        "id": 716,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 10,
        "power": 80,
        "type": "electric",
        "damage_class": "physical",
        "stat_changes": [],
        "effect_chance": 30,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 30,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Has a 30% chance to make the target flinch.",
        "flavor_text_entry": "A strong electric blast crashes down on the target, giving it an electric shock. This may also make the target flinch."
    },
    "howl": {
        "name": "howl",
        "id": 336,
        "accuracy": None,
        "priority": 0,
        "max_pp": 40,
        "power": None,
        "type": "normal",
        "damage_class": "status",
        "stat_changes": [
            {
                "change": 1,
                "stat": {
                    "name": "Atk",
                    "url": "https://pokeapi.co/api/v2/stat/2/"
                }
            }
        ],
        "effect_chance": None,
        "target": "user-and-allies",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "net-good-stats",
                "url": "https://pokeapi.co/api/v2/move-category/2/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Raises the user's Attack by one stage.",
        "flavor_text_entry": "Howls to raise the spirit and boosts ATTACK."
    },
    "flare-blitz": {
        "name": "flare-blitz",
        "id": 394,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 15,
        "power": 120,
        "type": "fire",
        "damage_class": "physical",
        "stat_changes": [],
        "effect_chance": 10,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "burn",
                "url": "https://pokeapi.co/api/v2/move-ailment/4/"
            },
            "ailment_chance": 10,
            "category": {
                "name": "damage+ailment",
                "url": "https://pokeapi.co/api/v2/move-category/4/"
            },
            "crit_rate": 0,
            "drain": -33,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "User takes 1/3 the damage inflicted in recoil.  Has a 10% chance to burn the target.",
        "flavor_text_entry": "The user cloaks itself in fire and charges at the foe. The user sustains serious damage, too."
    },
    "flame-burst": {
        "name": "flame-burst",
        "id": 481,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 15,
        "power": 70,
        "type": "fire",
        "damage_class": "special",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Deals splash damage to Pok\u00e9mon next to the target.",
        "flavor_text_entry": "The user attacks the target with a bursting flame. The bursting flame damages Pok\u00e9mon next to the target as well."
    },
    "flame-charge": {
        "name": "flame-charge",
        "id": 488,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 20,
        "power": 50,
        "type": "fire",
        "damage_class": "physical",
        "stat_changes": [
            {
                "change": 1,
                "stat": {
                    "name": "Speed",
                    "url": "https://pokeapi.co/api/v2/stat/6/"
                }
            }
        ],
        "effect_chance": 100,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage+raise",
                "url": "https://pokeapi.co/api/v2/move-category/7/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 100
        },
        "effect_entries": "Inflicts regular damage.  Raises the user's Speed by one stage.",
        "flavor_text_entry": "The user cloaks itself with flame and attacks. Building up more power, it raises the user\u2019s Speed stat."
    },
    "inferno": {
        "name": "inferno",
        "id": 517,
        "accuracy": 50,
        "priority": 0,
        "max_pp": 5,
        "power": 100,
        "type": "fire",
        "damage_class": "special",
        "stat_changes": [],
        "effect_chance": 100,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "burn",
                "url": "https://pokeapi.co/api/v2/move-ailment/4/"
            },
            "ailment_chance": 100,
            "category": {
                "name": "damage+ailment",
                "url": "https://pokeapi.co/api/v2/move-category/4/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Has a 100% chance to burn the target.",
        "flavor_text_entry": "The user attacks by engulfing the target in an intense fire. It leaves the target with a burn."
    },
    "mystical-fire": {
        "name": "mystical-fire",
        "id": 595,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 10,
        "power": 75,
        "type": "fire",
        "damage_class": "special",
        "stat_changes": [
            {
                "change": -1,
                "stat": {
                    "name": "SpAtk",
                    "url": "https://pokeapi.co/api/v2/stat/4/"
                }
            }
        ],
        "effect_chance": 100,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage+lower",
                "url": "https://pokeapi.co/api/v2/move-category/6/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 100
        },
        "effect_entries": "Has a 100% chance to lower the target's Special Attack by one stage.",
        "flavor_text_entry": "The user attacks by breathing a special, hot fire. This also lowers the target\u2019s Sp. Atk stat."
    },
    "burning-jealousy": {
        "name": "burning-jealousy",
        "id": 807,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 5,
        "power": 70,
        "type": "fire",
        "damage_class": "special",
        "stat_changes": [],
        "effect_chance": 100,
        "target": "all-opponents",
        "meta": {
            "ailment": {
                "name": "burn",
                "url": "https://pokeapi.co/api/v2/move-ailment/4/"
            },
            "ailment_chance": 100,
            "category": {
                "name": "damage+ailment",
                "url": "https://pokeapi.co/api/v2/move-category/4/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Inflicts regular damage with no additional effect.",
        "flavor_text_entry": "The user attacks with energy from jealousy. This leaves all opposing Pok\u00e9mon that have had their stats boosted during the turn with a burn."
    },
    "flame-wheel": {
        "name": "flame-wheel",
        "id": 172,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 25,
        "power": 60,
        "type": "fire",
        "damage_class": "physical",
        "stat_changes": [],
        "effect_chance": 10,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "burn",
                "url": "https://pokeapi.co/api/v2/move-ailment/4/"
            },
            "ailment_chance": 10,
            "category": {
                "name": "damage+ailment",
                "url": "https://pokeapi.co/api/v2/move-category/4/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Has a 10% chance to burn the target.  Lets frozen Pok\u00e9mon thaw themselves.",
        "flavor_text_entry": "An attack that may cause a burn."
    },
    "eruption": {
        "name": "eruption",
        "id": 284,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 5,
        "power": 150,
        "type": "fire",
        "damage_class": "special",
        "stat_changes": [],
        "effect_chance": None,
        "target": "all-opponents",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Inflicts more damage when the user has more HP remaining, with a maximum of 150 power.",
        "flavor_text_entry": "The higher the user\u2019s HP, the more damage caused."
    },
    "lava-plume": {
        "name": "lava-plume",
        "id": 436,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 15,
        "power": 80,
        "type": "fire",
        "damage_class": "special",
        "stat_changes": [],
        "effect_chance": 30,
        "target": "all-other-pokemon",
        "meta": {
            "ailment": {
                "name": "burn",
                "url": "https://pokeapi.co/api/v2/move-ailment/4/"
            },
            "ailment_chance": 30,
            "category": {
                "name": "damage+ailment",
                "url": "https://pokeapi.co/api/v2/move-category/4/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Has a 30% chance to burn the target.",
        "flavor_text_entry": "An inferno of scarlet flames washes over all Pok\u00e9mon in battle. It may also inflict burns."
    },
    "heat-crash": {
        "name": "heat-crash",
        "id": 535,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 10,
        "power": None,
        "type": "fire",
        "damage_class": "physical",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Power is higher when the user weighs more than the target, up to a maximum of 120.",
        "flavor_text_entry": "The user slams its target with its flame- covered body. The more the user outweighs the target, the greater the damage."
    },
    "poison-fang": {
        "name": "poison-fang",
        "id": 305,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 15,
        "power": 50,
        "type": "poison",
        "damage_class": "physical",
        "stat_changes": [],
        "effect_chance": 50,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "poison",
                "url": "https://pokeapi.co/api/v2/move-ailment/5/"
            },
            "ailment_chance": 50,
            "category": {
                "name": "damage+ailment",
                "url": "https://pokeapi.co/api/v2/move-category/4/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Has a 50% chance to badly poison the target.",
        "flavor_text_entry": "A sharp-fanged attack. May badly poison the foe."
    },
    "morning-sun": {
        "name": "morning-sun",
        "id": 234,
        "accuracy": None,
        "priority": 0,
        "max_pp": 5,
        "power": None,
        "type": "normal",
        "damage_class": "status",
        "stat_changes": [],
        "effect_chance": None,
        "target": "user",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "heal",
                "url": "https://pokeapi.co/api/v2/move-category/3/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 50,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Heals the user by half its max HP.  Affected by weather.",
        "flavor_text_entry": "Restores HP (varies by time)."
    },
    "burn-up": {
        "name": "burn-up",
        "id": 682,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 5,
        "power": 130,
        "type": "fire",
        "damage_class": "special",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Removes the user's fire type after inflicting damage.",
        "flavor_text_entry": "To inflict massive damage, the user burns itself out. After using this move, the user will no longer be Fire type."
    },
    "raging-fury": {
        "name": "raging-fury",
        "id": 833,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 10,
        "power": 120,
        "type": "fire",
        "damage_class": "physical",
        "stat_changes": [],
        "effect_chance": None,
        "target": "random-opponent",
        "meta": None
    },
    "spider-web": {
        "name": "spider-web",
        "id": 169,
        "accuracy": None,
        "priority": 0,
        "max_pp": 10,
        "power": None,
        "type": "bug",
        "damage_class": "status",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "unique",
                "url": "https://pokeapi.co/api/v2/move-category/13/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Prevents the target from leaving battle.",
        "flavor_text_entry": "Prevents fleeing or switching."
    },
    "gastro-acid": {
        "name": "gastro-acid",
        "id": 380,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 10,
        "power": None,
        "type": "poison",
        "damage_class": "status",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "unique",
                "url": "https://pokeapi.co/api/v2/move-category/13/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Nullifies target's ability until it leaves battle.",
        "flavor_text_entry": "The user hurls up its stomach acids on the foe. The fluid eliminates the effect of the foe\u2019s ability."
    },
    "sticky-web": {
        "name": "sticky-web",
        "id": 564,
        "accuracy": None,
        "priority": 0,
        "max_pp": 20,
        "power": None,
        "type": "bug",
        "damage_class": "status",
        "stat_changes": [],
        "effect_chance": None,
        "target": "opponents-field",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "field-effect",
                "url": "https://pokeapi.co/api/v2/move-category/11/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Covers the opposing field, lowering opponents' Speed by one stage upon switching in.",
        "flavor_text_entry": "The user weaves a sticky net around the opposing team, which lowers their Speed stat upon switching into battle."
    },
    "drill-peck": {
        "name": "drill-peck",
        "id": 65,
        "accuracy": 100,
        "priority": 0,
        "max_pp": 20,
        "power": 80,
        "type": "flying",
        "damage_class": "physical",
        "stat_changes": [],
        "effect_chance": None,
        "target": "selected-pokemon",
        "meta": {
            "ailment": {
                "name": "none",
                "url": "https://pokeapi.co/api/v2/move-ailment/0/"
            },
            "ailment_chance": 0,
            "category": {
                "name": "damage",
                "url": "https://pokeapi.co/api/v2/move-category/0/"
            },
            "crit_rate": 0,
            "drain": 0,
            "flinch_chance": 0,
            "healing": 0,
            "max_hits": None,
            "max_turns": None,
            "min_hits": None,
            "min_turns": None,
            "stat_chance": 0
        },
        "effect_entries": "Inflicts regular damage with no additional effect.",
        "flavor_text_entry": "A strong, spin\u00ad ning-peck attack."
    }
}
