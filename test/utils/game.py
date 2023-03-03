import pytest
from classes.character import Character
from utils.game import get_order_player, get_message_final

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


@pytest.mark.parametrize(
    ("player_1_damage", "player_2_damage", "expected"),
    (
        (6, 0, "Gano Steve"),
        (0, 7, "Gano Test"),
        (0, 0, "Empate")
    ),
)
def test_get_message_final(player_1_damage, player_2_damage, expected):
    player_1 = Character("Steve", 7, TEST_TYPE_OF_ATTACKS)
    player_2 = Character("Test", 6, TEST_TYPE_OF_ATTACKS)

    player_1.receive_damage(player_2_damage)
    player_2.receive_damage(player_1_damage)
    result = get_message_final(player_1, player_2)
    assert result == expected


def test_get_order_player():
    player_1 = Character("Steve", 6, TEST_TYPE_OF_ATTACKS)
    player_2 = Character("Test", 6, TEST_TYPE_OF_ATTACKS)

    player_1_actions = (('DSD', 'P'), ('S', ''))
    player_2_actions = (('', 'P'), ('ASA', ''), ('DA', 'P'), ('AAA', 'K'), ('', 'K'), ('SA', 'K'))
    first_player, second_player, first_player_movements, second_player_movements = get_order_player(player_1, player_2, player_1_actions, player_2_actions)

    assert first_player == player_1
    assert second_player == player_2
    assert first_player_movements == player_1_actions
    assert second_player_movements == player_2_actions

    player_1_actions = (('DSD', 'P'), ('S', ''))
    player_2_actions = (('', 'P'), ('ASA', ''))
    first_player, second_player, first_player_movements, second_player_movements = get_order_player(player_1, player_2, player_1_actions, player_2_actions)

    assert first_player == player_2
    assert second_player == player_1
    assert first_player_movements == player_2_actions
    assert second_player_movements == player_1_actions

    player_1_actions = (('DSD', 'P'), ('D', ''), ('S', 'P'))
    player_2_actions = (('D', 'P'), ('DSD', 'P'), ('S', ''))
    first_player, second_player, first_player_movements, second_player_movements = get_order_player(player_1, player_2, player_1_actions, player_2_actions)

    assert first_player == player_1
    assert second_player == player_2
    assert first_player_movements == player_1_actions
    assert second_player_movements == player_2_actions
