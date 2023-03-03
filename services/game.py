from config.constants import DEFAULT_POINTS_OF_LIFE, PLAYER_1_TYPE_OF_ATTACKS, PLAYER_2_TYPE_OF_ATTACKS
from game.character import Character
from utils.game import merge_list


def _get_message_final(player_1: Character, player_2: Character):
    message_final = ""

    if player_1.life_point > 0 and player_2.life_point > 0:
        message_final = "Empate"
    elif player_1.life_point == 0 and player_2.life_point > 0:
        message_final = f"Gano {player_2.name}"
    elif player_1.life_point > 0 and player_2.life_point == 0:
        message_final = f"Gano {player_1.name}"

    return message_final


def start_game(player_movements: dict[str, dict[str, list]]) -> list[str]:
    player_1 = Character("Tonyn", DEFAULT_POINTS_OF_LIFE, PLAYER_1_TYPE_OF_ATTACKS)
    player_2 = Character("Arnaldor", DEFAULT_POINTS_OF_LIFE, PLAYER_2_TYPE_OF_ATTACKS)

    player_1_actions = player_movements.get('player1')
    player_2_actions = player_movements.get('player2')

    player_1_movements = merge_list(player_1_actions.get('movimientos'), player_1_actions.get('golpes'))
    player_2_movements = merge_list(player_2_actions.get('movimientos'), player_2_actions.get('golpes'))

    len_player_1_movements = len(player_1_movements)
    len_player_2_movements = len(player_2_movements)
    len_movements = max(len_player_1_movements, len_player_2_movements)

    history_messages = []

    # todo: encapsulate in a funcion execute_actions
    for i in range(len_movements):

        if i < len_player_1_movements:
            attack_player_1 = player_1.attack(player_1_movements[i])
            history_messages.append(f'{player_1.name} {attack_player_1["message"]}')

            life_points_player_2 = player_2.receive_damage(attack_player_1['damage'])
            if life_points_player_2 == 0:
                break

        if i < len_player_2_movements:
            attack_player_2 = player_2.attack(player_2_movements[i])
            history_messages.append(f'{player_2.name} {attack_player_2["message"]}')

            life_points_player_1 = player_1.receive_damage(attack_player_2['damage'])
            if life_points_player_1 == 0:
                break

    history_messages.append(_get_message_final(player_1, player_2))

    return history_messages
