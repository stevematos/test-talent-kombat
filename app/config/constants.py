DEFAULT_POINTS_OF_LIFE = 6

DEFAULT_MOVE = {
    "damage": 0,
    "name": "Move",
    "message": "se mueve",
}


DEFAULT_GENERAL_ATTACKS = {
    "P": {
        "damage": 1,
        "name": "Punch",
        "message": "le da un puñetazo",
    },
    "K": {
        "damage": 1,
        "name": "Kick",
        "message": "le da una patada",
    },
}


PLAYER_1_TYPE_OF_ATTACKS = {
    ("DSD", "P"): {
        "damage": 3,
        "name": "Taladoken",
        "message": "usa un Taladoken",
    },
    ("SD", "K"): {
        "damage": 2,
        "name": "Remuyuken",
        "message": "conecta un Remuyuken",
    },
}


PLAYER_2_TYPE_OF_ATTACKS = {
    ("ASA", "P"): {
        "damage": 3,
        "name": "Taladoken",
        "message": "usa un Taladoken",
    },
    ("SA", "K"): {
        "damage": 2,
        "name": "Remuyuken",
        "message": "conecta un Remuyuken",
    },
}
