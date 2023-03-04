def merge_list(list1: list, list2: list) -> tuple:
    return tuple(zip(list1, list2))


def join_tuple_of_tuple(_tuples: tuple) -> str:
    return ''.join([''.join(_tuple) for _tuple in _tuples])


def join_value_of_tuple(_tuples: tuple, i: int = 0) -> str:
    return ''.join([_tuple[i] for _tuple in _tuples])


def get_value_exceed_max_characters(_tuple: tuple, max_characters: int) -> str | None:
    for value in _tuple:
        if len(value) > max_characters:
            return value
    return None
