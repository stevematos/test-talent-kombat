DEFAULT_POINTS_OF_LIFE = 6

DEFAULT_MOVE = {"name": "Se mueve pero no ataca", "damage": 0}

DEFAULT_GENERAL_ATTACKS = {
    "P": {
        "damage": 1,
        "name": "Puño"
    },
    "K": {
        "damage": 1,
        "name": "Patada"
    },
}


PLAYER_1_TYPE_OF_ATTACKS = {
    ("DSD", "P"): {
        "damage": 3,
        "name": "Taladoken"
    },
    ("SD", "K"): {
        "damage": 2,
        "name": "Remuyuken"
    },
}


PLAYER_2_TYPE_OF_ATTACKS = {
    ("SA", "K"): {
        "damage": 3,
        "name": "Taladoken"
    },
    ("ASA", "P"): {
        "damage": 2,
        "name": "Remuyuken"
    },
    ("", "P"): {
        "damage": 1,
        "name": "Puño"
    },
    ("", "K"): {
        "damage": 1,
        "name": "Patada"
    },
}