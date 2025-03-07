TRAINER_DATA = {
    'dad intro': {
        'dialog': {
            'default': ["Almost there, champ!", "You feeling ok back there?"]
        }
    },
    'professor intro': {
        'dialog': {
            'default': ["Settle down."],
            'default 1': ["First off, I'd like to extend my gratitude\nfor taking this module.", "Let's take the register."],
            'default 2': [
                "My name is Arthur Pine. For the duration of this\n"
                "class, you will refer to me as 'professor'.",
                "I'm a researcher who specialises in the very\n"
                "monsters being sighted in Forks recently.",
                "I've studied them extensively for most of my life.",
                "These are not monsters, they are Pokemon.",
                "Through my research into villages and tribes\n"
                "that have learnt to co-exist with Pokemon...",
                "I have observed a powerful bond between them\n"
                "and their human companions.",
                "In my class, for this year, you will learn to\n"
                "train, research and battle Pokemon.",
                "To start... I've selected a few starting\n"
                "Pokemon for each of you to begin your trainer\n"
                "journey.",
                "Come up and select your starter, then file outside\n"
                "to the high-school court."
            ]
        }
    },
    'cheren classmate 1': {
        'dialog': {
            'default': ["I'm kind of nervous..."]
        },
        'defeated': False
    },
    'lass classmate 1': {
        'dialog': {
            'default': ["Go on! Pick!", "Everyone's waiting!"]
        },
        'defeated': False
    },
    'lady classmate 1': {
        'dialog': {
            'default': ["Pokemon are so pretty!", "You better not take the cute starter!\nShe's mine!"]
        },
        'defeated': False
    },
    'edward 1': {
        'dialog': {
            'default': ["...", "What are you looking at?"]
        },
        'defeated': False
    },
    'collector classmate 1': {
        'dialog': {
            'default': ["The optimal choice is obvious.", "Don't you agree?"]
        },
        'defeated': False
    },
    'professor 1': {
        'dialog': {
            'default': ["Your first pokemon is the most important\nmoment in a trainer's career.", "So don't rush it."]
        },
        'defeated': False
    },
    'cheren classmate 2': {
        'dialog': {
            'default': ["Oh boy! This is it!", "I better not cry if I lose!"]
        },
        'defeated': False
    },
    'lass classmate 2': {
        'dialog': {
            'default': ["Huh?", "Oh! You're my first opponent!"]
        },
        'defeated': False
    },
    'lady classmate 2': {
        'dialog': {
            'default': ["In those shoes?", "Yeah, right!"]
        },
        'defeated': False
    },
    'collector classmate 2': {
        'dialog': {
            'default': ["Back away!", "I'm busy calculating all possible outcomes to this\nbattle!"]
        },
        'defeated': False
    },
    'edward 2': {
        'pokemon': {
            0: ['vulpix', 25, None, None, ['peck', 'growl', 'leech-life', 'psychic'], None, None, None, None, None],
            1: ['azurill', 10, None, None, ['tackle', 'water-gun', 'dazzling-gleam', None], None, None, None, None, None]
        },
        'dialog': {
            'default': ["...", "Whatever."],
            'defeated': ["...", "I guess you're not as bad as I thought."]
        },
        'defeated': False
    },
    'professor 2': {
        'dialog': {
            'default': ["You'll be battling that weird brooding kid\nover there, Edward.", "Good luck."],
            'defeated': ["", ""]
        },
        'defeated': False
    }
}

EFFECTIVE_DATA = {
    "normal": {
        "rock": 0.5, "ghost": 0, "steel": 0.5
    },
    "fire": {
        "fire": 0.5, "water": 0.5, "grass": 2.0, "ice": 2.0, "bug": 2.0, "rock": 0.5, "dragon": 0.5, "steel": 2.0
    },
    "water": {
        "fire": 2.0, "water": 0.5, "grass": 0.5, "ground": 2.0, "rock": 2.0, "dragon": 0.5
    },
    "electric": {
        "water": 2.0, "electric": 0.5, "grass": 0.5, "ground": 0, "flying": 2.0, "dragon": 0.5
    },
    "grass": {
        "fire": 0.5, "water": 2.0, "grass": 0.5, "poison": 0.5, "ground": 2.0, "flying": 0.5, "bug": 0.5, "rock": 2.0, "dragon": 0.5, "steel": 0.5
    },
    "ice": {
        "fire": 0.5, "water": 0.5, "grass": 2.0, "ice": 0.5, "ground": 2.0, "flying": 2.0, "dragon": 2.0, "steel": 0.5
    },
    "fighting": {
        "normal": 2.0, "ice": 2.0, "poison": 0.5, "flying": 0.5, "psychic": 0.5, "bug": 0.5, "rock": 2.0, "ghost": 0, "dark": 2.0, "steel": 2.0, "fairy": 0.5
    },
    "poison": {
        "grass": 2.0, "poison": 0.5, "ground": 0.5, "rock": 0.5, "ghost": 0.5, "steel": 0, "fairy": 2.0
    },
    "ground": {
        "fire": 2.0, "electric": 2.0, "grass": 0.5, "poison": 2.0, "flying": 0, "bug": 0.5, "rock": 2.0, "steel": 2.0
    },
    "flying": {
        "electric": 0.5, "grass": 2.0, "fighting": 2.0, "bug": 2.0, "rock": 0.5, "steel": 0.5
    },
    "psychic": {
        "fighting": 2.0, "poison": 2.0, "psychic": 0.5, "dark": 0, "steel": 0.5
    },
    "bug": {
        "fire": 0.5, "grass": 2.0, "fighting": 0.5, "poison": 0.5, "flying": 0.5, "psychic": 2.0, "ghost": 0.5, "dark": 2.0, "steel": 0.5, "fairy": 0.5
    },
    "rock": {
        "fire": 2.0, "ice": 2.0, "fighting": 0.5, "ground": 0.5, "flying": 2.0, "bug": 2.0, "steel": 0.5
    },
    "ghost": {
        "normal": 0, "psychic": 2.0, "ghost": 2.0, "dark": 0.5
    },
    "dragon": {
        "dragon": 2.0, "steel": 0.5, "fairy": 0
    },
    "dark": {
        "fighting": 0.5, "psychic": 2.0, "ghost": 2.0, "dark": 0.5, "fairy": 0.5
    },
    "steel": {
        "fire": 0.5, "water": 0.5, "electric": 0.5, "ice": 2.0, "rock": 2.0, "steel": 0.5, "fairy": 2.0
    },
    "fairy": {
        "fire": 0.5, "fighting": 2.0, "poison": 0.5, "dragon": 2.0, "dark": 2.0, "steel": 0.5
    },
}

NATURE_DATA = {    
    "Adamant": {"increased": "Atk", "decreased": "SpAtk"},
    "Bashful": {"increased": None, "decreased": None},
    "Bold": {"increased": "Def", "decreased": "Atk"},
    "Brave": {"increased": "Atk", "decreased": "Speed"},
    "Calm": {"increased": "SpDef", "decreased": "Atk"},
    "Careful": {"increased": "SpDef", "decreased": "SpAtk"},
    "Docile": {"increased": None, "decreased": None},
    "Gentle": {"increased": "SpDef", "decreased": "Def"},
    "Hardy": {"increased": None, "decreased": None},
    "Hasty": {"increased": "Speed", "decreased": "Def"},
    "Impish": {"increased": "Def", "decreased": "SpAtk"},
    "Jolly": {"increased": "Speed", "decreased": "SpAtk"},
    "Lax": {"increased": "Def", "decreased": "SpDef"},
    "Lonely": {"increased": "Atk", "decreased": "Def"},
    "Mild": {"increased": "SpAtk", "decreased": "Def"},
    "Modest": {"increased": "SpAtk", "decreased": "Atk"},
    "Naive": {"increased": "Speed", "decreased": "SpDef"},
    "Naughty": {"increased": "Atk", "decreased": "SpDef"},
    "Quiet": {"increased": "SpAtk", "decreased": "Speed"},
    "Quirky": {"increased": None, "decreased": None},
    "Rash": {"increased": "SpAtk", "decreased": "SpDef"},
    "Relaxed": {"increased": "Def", "decreased": "Speed"},
    "Sassy": {"increased": "SpDef", "decreased": "Speed"},
    "Serious": {"increased": None, "decreased": None},
    "Timid": {"increased": "Speed", "decreased": "Atk"}
}

NARRATOR_DATA = {
    'forest_road': [
        "The car's tires hum softly against the wet road as you drive\n"
        "through the dense fog that clings to the landscape of\n"
        "Forks, Washington.",
        "The overcast sky, towering evergreens on either side\n"
        "of the road…",
        "It's a fresh start in a new town, far away from\n"
        "the bustling life you once knew.",
        "Your lax vision watches the pine trees fly by.",
        "But in the shadows of that seemingly endless maze,\n"
        "a silhouette briefly darts between the trunks.",
        "But you quickly forget as you turn into a side-road.",
        "As you pull up to your new home, a sense of apprehension stirs\n"
        "within you.",
        "It looks old...",
        "...and damp.",
        "You can clearly see the peeling paint-job and rotting wood on\n"
        "its walls.",
        "Your dad says the house's mouldy smell is an acquired taste.",
        "You sit in bed, it's already late.",
        "Tomorrow...",
        "Tomorrow, you'll walk the halls of Forks High School,\n"
        "a nobody in a sea of somebodies."
    ],
    'classroom': [
        "The moment you step into the classroom, it's as if an\n"
        "invisible spotlight has settled on you.",
        "You took a module for the first year that had just been\n"
        "added. 'Pokemon Trainer 101'...",
        "What the hell is a Pokemon?",
        "You figured it could be an easy grade.",
        "But as you file into class, everyone around you seems to\n"
        "be just as uncertain about this class as you are.",
        "You found a seat just as the door opened...",
        "A man whose presence seems to command immediate attention.",
        "'Prof. Pine', his lanyard reads...",
        "His demeanour suggests he's walked through these motions\n"
        "far more times than he cares to count."
    ]
}