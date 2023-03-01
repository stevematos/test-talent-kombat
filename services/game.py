from config.constants import DEFAULT_POINTS_OF_LIFE, PLAYER_1_TYPE_OF_ATTACKS, PLAYER_2_TYPE_OF_ATTACKS
from game.character import Character


def start_game(player_movements: dict[str, dict[str, list]]):
    player_1 = Character("player 1", DEFAULT_POINTS_OF_LIFE, PLAYER_1_TYPE_OF_ATTACKS)
    player_2 = Character("player 2", DEFAULT_POINTS_OF_LIFE, PLAYER_2_TYPE_OF_ATTACKS)


