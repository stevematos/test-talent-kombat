from config.constants import DEFAULT_POINTS_OF_LIFE, PLAYER_1_TYPE_OF_ATTACKS, PLAYER_2_TYPE_OF_ATTACKS
from classes.character import Character
from config.exceptions import ActionExceedCharacters
from utils.game import get_message_final, get_order_player
from utils.general import merge_list, get_value_exceed_max_characters


def _execute_actions(
    first_player: Character,
    second_player: Character,
    first_player_actions: tuple,
    second_player_actions:  tuple,
) -> list[str]:
    len_first_player_actions = len(first_player_actions)
    len_second_player_actions = len(second_player_actions)
    len_actions = max(len_first_player_actions, len_second_player_actions)

    history_messages = []

    for i in range(len_actions):

        if i < len_first_player_actions:
            attack_first_player = first_player.attack(first_player_actions[i])
            history_messages.append(f'{first_player.name} {attack_first_player["message"]}')

            life_points_second_player = second_player.receive_damage(attack_first_player['damage'])
            if life_points_second_player == 0:
                break

        if i < len_second_player_actions:
            attack_second_player = second_player.attack(second_player_actions[i])
            history_messages.append(f'{second_player.name} {attack_second_player["message"]}')

            life_points_first_player = first_player.receive_damage(attack_second_player['damage'])
            if life_points_first_player == 0:
                break

    history_messages.append(get_message_final(first_player, second_player))

    return history_messages


def _verify_actions(player_actions: dict[str, list]):
    movements = player_actions.get('movimientos', ())
    attacks = player_actions.get('golpes', ())

    if exceed_value := get_value_exceed_max_characters(movements, 5):
        raise ActionExceedCharacters('move', exceed_value, 5)
    if exceed_value := get_value_exceed_max_characters(attacks, 1):
        raise ActionExceedCharacters('attack', exceed_value, 1)


def start_game(player_actions: dict[str, dict[str, list]]) -> list[str]:
    player_1 = Character("Tonyn", DEFAULT_POINTS_OF_LIFE, PLAYER_1_TYPE_OF_ATTACKS)
    player_2 = Character("Arnaldor", DEFAULT_POINTS_OF_LIFE, PLAYER_2_TYPE_OF_ATTACKS)

    player_1_actions = player_actions.get('player1')
    player_2_actions = player_actions.get('player2')

    # verify max characters in movements y hits
    _verify_actions(player_1_actions)
    _verify_actions(player_2_actions)

    player_1_tuple_actions = merge_list(player_1_actions.get('movimientos'), player_1_actions.get('golpes'))
    player_2_tuple_actions = merge_list(player_2_actions.get('movimientos'), player_2_actions.get('golpes'))

    first_player, second_player, first_player_actions, second_player_actions = get_order_player(player_1, player_2, player_1_tuple_actions, player_2_tuple_actions)

    history_messages = _execute_actions(first_player, second_player, first_player_actions, second_player_actions)

    return history_messages
