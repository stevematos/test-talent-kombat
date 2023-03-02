from config.constants import DEFAULT_POINTS_OF_LIFE, PLAYER_1_TYPE_OF_ATTACKS, PLAYER_2_TYPE_OF_ATTACKS
from game.character import Character
from utils.game import merge_list


def start_game(player_movements: dict[str, dict[str, list]]) -> list[str]:
    player_1 = Character("player 1", DEFAULT_POINTS_OF_LIFE, PLAYER_1_TYPE_OF_ATTACKS)
    player_2 = Character("player 2", DEFAULT_POINTS_OF_LIFE, PLAYER_2_TYPE_OF_ATTACKS)

    player_1_actions = player_movements.get('player1')
    player_2_actions = player_movements.get('player2')

    player_1_movements = merge_list(player_1_actions.get('movimientos'), player_1_actions.get('golpes'))
    player_2_movements = merge_list(player_2_actions.get('movimientos'), player_2_actions.get('golpes'))

    print(player_1_movements)
    print(player_2_movements)

    len_player_1_movements = len(player_1_movements)
    len_player_2_movements = len(player_2_movements)
    len_movements = max(len_player_1_movements, len_player_2_movements)

    life_points_player_1 = 0
    life_points_player_2 = 0

    for i in range(len_movements):

        if i < len_player_1_movements:
            attack_player_1 = player_1.attack(player_1_movements[i])
            print(attack_player_1)
            life_points_player_2 = player_2.receive_damage(attack_player_1['damage'])

            if life_points_player_2 == 0:
                break

        if i < len_player_2_movements:
            attack_player_2 = player_2.attack(player_2_movements[i])
            print(attack_player_2)
            life_points_player_1 = player_1.receive_damage(attack_player_2['damage'])

            if life_points_player_1 == 0:
                break

    message_final = ""

    if life_points_player_1 > 0 and life_points_player_2 > 0:
        message_final = "Empate"
    elif life_points_player_1 == 0 and life_points_player_2 > 0:
        message_final = "Gano Player 2"
    elif life_points_player_1 > 0 and life_points_player_2 == 0:
        message_final = "Gano Player 1"

    return [message_final]
