import pytest
from classes.character import Character
from config.exceptions import ActionExceedCharacters
from services.game import _execute_actions, _verify_actions

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
    ("first_player_actions", "second_player_actions", "expected"),
    (
            (
                (('DSD', 'P'), ('S', '')),
                (('', 'P'), ('ASA', ''), ('DA', 'P'), ('AAA', 'K'), ('', 'K'), ('SA', 'K')),
                ['Steve se mueve y le da un puñetazo', 'Test le da un puñetazo', 'Steve se mueve', 'Test se mueve', 'Test se mueve y le da un puñetazo', 'Test se mueve y le da una patada', 'Test le da una patada', 'Test se mueve y le da una patada', 'Empate']
            ),
            (
                (('DSS', 'P'), ('DSS', 'P'), ('DSS', 'P'), ('S', '')),
                (('', 'P'), ('ASA', ''), ('DA', 'P'), ('AAA', 'K'), ('', 'K'), ('SA', 'K')),
                ['Steve usa un Taladoken', 'Test le da un puñetazo', 'Steve usa un Taladoken', 'Gano Steve']
            ),
            (
                (('DSS', 'P'), ('S', 'P'), ('S', 'P')),
                (('DSS', 'P'), ('DSS', 'P'), ('DSS', 'P')),
                ['Steve usa un Taladoken', 'Test usa un Taladoken', 'Steve se mueve y le da un puñetazo', 'Test usa un Taladoken', 'Gano Test']
            )
    ),
)
def test__execute_actions(first_player_actions, second_player_actions, expected):
    first_player = Character("Steve", 6, TEST_TYPE_OF_ATTACKS)
    second_player = Character("Test", 6, TEST_TYPE_OF_ATTACKS)

    result = _execute_actions(first_player, second_player, first_player_actions, second_player_actions)
    assert result == expected


@pytest.mark.parametrize(
    ("player_actions", "raise_exception"),
    (
            (
                {
                    "movimientos": [
                        "DSD",
                        "S"
                    ],
                    "golpes": [
                        "P",
                        ""
                    ]
                },
                None
            ),
            (
                {
                    "movimientos": [
                        "DSD",
                        "SSSSSS"
                    ],
                    "golpes": [
                        "P",
                        ""
                    ]
                },
                ActionExceedCharacters
            ),
    ),
)
def test___verify_actions(player_actions, raise_exception):
    if raise_exception:
        with pytest.raises(raise_exception):
            _verify_actions(player_actions)
    else:
        _verify_actions(player_actions)
