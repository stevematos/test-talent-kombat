from game.character import Character

TEST_TYPE_OF_ATTACKS = {
    ("DSS", "P"): {
        "damage": 3,
        "name": "Taladoken"
    },
    ("SD", "K"): {
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


class TestCharacter:
    def test_attack(self):
        character = Character("Steve", 7, TEST_TYPE_OF_ATTACKS)

        type_of_attack = ("DSS", "P")
        expected = {'damage': 3, 'name': 'Taladoken'}
        result = character.attack(type_of_attack)
        assert result == expected

        type_of_attack = ("DDD", "P")
        expected = {'damage': 1, 'name': 'Puño'}
        result = character.attack(type_of_attack)
        assert result == expected

    def test_receive_damage(self):
        character = Character("Juan", 7, TEST_TYPE_OF_ATTACKS)

        expected = 4
        result = character.receive_damage(3)
        assert result == expected

        expected = 2
        result = character.receive_damage(2)
        assert result == expected

        expected = 0
        result = character.receive_damage(3)
        assert result == expected

