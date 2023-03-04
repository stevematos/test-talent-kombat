class ActionExceedCharacters(Exception):
    def __init__(self, type_action: str, value: str, max_characters: int) -> None:
        self.type_action = type_action
        self.value = value
        self.max_characters = max_characters

    def __str__(self):
        return f"The {self.type_action} {self.value} exceeds {self.max_characters} character(s)"
