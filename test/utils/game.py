from game.character import Character
from utils.game import get_order_player

TEST_TYPE_OF_ATTACKS = {
    ("DSS", "P"): {
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


def test_get_order_player():
    player_1 = Character("Tonyn", 6, TEST_TYPE_OF_ATTACKS)
    player_2 = Character("Arnaldor", 6, TEST_TYPE_OF_ATTACKS)

    player_1_movements = (('DSD', 'P'), ('S', ''))
    player_2_movements = (('', 'P'), ('ASA', ''), ('DA', 'P'), ('AAA', 'K'), ('', 'K'), ('SA', 'K'))
    first_player, second_player, first_player_movements, second_player_movements = get_order_player(player_1, player_2, player_1_movements, player_2_movements)

    assert first_player == player_1
    assert second_player == player_2
    assert first_player_movements == player_1_movements
    assert second_player_movements == player_2_movements

    player_1_movements = (('DSD', 'P'), ('S', ''))
    player_2_movements = (('', 'P'), ('ASA', ''))
    first_player, second_player, first_player_movements, second_player_movements = get_order_player(player_1, player_2, player_1_movements, player_2_movements)

    assert first_player == player_2
    assert second_player == player_1
    assert first_player_movements == player_2_movements
    assert second_player_movements == player_1_movements

    player_1_movements = (('DSD', 'P'), ('D', ''), ('S', 'P'))
    player_2_movements = (('D', 'P'), ('DSD', 'P'), ('S', ''))
    first_player, second_player, first_player_movements, second_player_movements = get_order_player(player_1, player_2, player_1_movements, player_2_movements)

    assert first_player == player_1
    assert second_player == player_2
    assert first_player_movements == player_1_movements
    assert second_player_movements == player_2_movements
