from config.exceptions import TypeOfAttackNotFound


class Character:

    def __init__(self, name: str, life_point: int, type_of_attacks: dict[tuple, dict[str: str | int]]):
        self._name = name
        self._life_point = life_point
        self._type_of_attacks = type_of_attacks

    def attack(self, type_of_attack: tuple) -> int:
        try:
            result_attack = self._type_of_attacks[type_of_attack]
        except KeyError:
            raise TypeOfAttackNotFound

        return result_attack

    def receive_damage(self, damage: int) -> int:
        self._life_point -= damage

        if self._life_point < 0:
            self._life_point = 0

        return self._life_point

