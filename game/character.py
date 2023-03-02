from config.constants import DEFAULT_GENERAL_ATTACKS, DEFAULT_MOVE


class Character:

    def __init__(self, name: str, life_point: int, type_of_attacks: dict[tuple, dict[str, str | int]], general_attacks:  dict[str, dict[str, str | int]] = DEFAULT_GENERAL_ATTACKS):
        self._name = name
        self._life_point = life_point
        self._type_of_attacks = type_of_attacks
        self._general_attacks = general_attacks

    def attack(self, type_of_attack: tuple) -> dict[str, str | int]:
        try:
            result_attack = self._type_of_attacks[type_of_attack]
        except KeyError:
            if type_of_attack[1]:
                result_attack = self._general_attacks[type_of_attack[1]]
            else:
                result_attack = DEFAULT_MOVE

        return result_attack

    def receive_damage(self, damage: int) -> int:
        self._life_point -= damage

        if self._life_point < 0:
            self._life_point = 0

        return self._life_point

