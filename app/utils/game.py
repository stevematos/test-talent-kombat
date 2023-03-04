from classes.character import Character
from utils.general import join_tuple_of_tuple, join_value_of_tuple


def get_message_final(player_1: Character, player_2: Character):
    message_final = ""

    if player_1.life_point > 0 and player_2.life_point > 0:
        message_final = "Empate"
    elif player_1.life_point == 0 and player_2.life_point > 0:
        message_final = f"Gano {player_2.name} con {player_2.life_point} punto(s) de vida"
    elif player_1.life_point > 0 and player_2.life_point == 0:
        message_final = f"Gano {player_1.name} con {player_1.life_point} punto(s) de vida"

    return message_final


def get_order_player(
    player_1: Character,
    player_2: Character,
    player_1_actions: tuple,
    player_2_actions: tuple,
) -> tuple:

    first_player_order = (player_1, player_2, player_1_actions, player_2_actions)
    second_player_order = (player_2, player_1, player_2_actions, player_1_actions)

    str_player_1_actions = join_tuple_of_tuple(player_1_actions)
    str_player_2_actions = join_tuple_of_tuple(player_2_actions)

    if len(str_player_1_actions) < len(str_player_2_actions):
        return first_player_order
    elif len(str_player_1_actions) > len(str_player_2_actions):
        return second_player_order

    str_player_1_movements = join_value_of_tuple(player_1_actions)
    str_player_2_movements = join_value_of_tuple(player_2_actions)

    if len(str_player_1_movements) < len(str_player_2_movements):
        return first_player_order
    elif len(str_player_1_movements) > len(str_player_2_movements):
        return second_player_order

    str_player_1_hits = join_value_of_tuple(player_1_actions, 1)
    str_player_2_hits = join_value_of_tuple(player_2_actions, 1)

    if len(str_player_1_hits) < len(str_player_2_hits):
        return first_player_order
    elif len(str_player_1_hits) > len(str_player_2_hits):
        return second_player_order

    return first_player_order
