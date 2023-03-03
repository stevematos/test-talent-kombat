from game.character import Character

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


class TestCharacter:
    def test_attack(self):
        character = Character("Steve", 7, TEST_TYPE_OF_ATTACKS)

        type_of_attack = ("DSS", "P")
        expected = {'damage': 3, 'message': 'usa un Taladoken', 'name': 'Taladoken'}
        result = character.attack(type_of_attack)
        assert result == expected

        type_of_attack = ("", "P")
        expected = {'damage': 1, 'message': 'le da un puñetazo', 'name': 'Punch'}
        result = character.attack(type_of_attack)
        assert result == expected

        type_of_attack = ("DDD", "P")
        expected = {'damage': 1, 'message': 'se mueve y le da un puñetazo', 'name': 'Punch'}
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

