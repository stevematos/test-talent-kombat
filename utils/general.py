def merge_list(list1, list2):
    return tuple(zip(list1, list2))


def join_tuple_of_tuple(_tuples: tuple):
    return ''.join([''.join(_tuple) for _tuple in _tuples])


def join_value_of_tuple(_tuples: tuple, i: int = 0):
    return ''.join([_tuple[i] for _tuple in _tuples])