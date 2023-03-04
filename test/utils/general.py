import pytest
from utils.general import get_value_exceed_max_characters, merge_list, join_tuple_of_tuple, join_value_of_tuple


@pytest.mark.parametrize(
    ("list_1", "list_2", "expected"),
    (
        (['', 'ASA', 'DA', 'AAA', '', 'SA'], ['P', '', 'P', 'K', 'K', 'K'], (('', 'P'), ('ASA', ''), ('DA', 'P'), ('AAA', 'K'), ('', 'K'), ('SA', 'K'))),
        (['', 'ASA'], ['P', ''], (('', 'P'), ('ASA', ''))),
    )
)
def test_merge_list(list_1, list_2, expected):
    result = merge_list(list_1, list_2)
    assert result == expected


@pytest.mark.parametrize(
    ("tuple_input", "expected"),
    (
        ((('', 'P'), ('ASA', ''), ('DA', 'P'), ('AAA', 'K'), ('', 'K'), ('SA', 'K')), "PASADAPAAAKKSAK"),
        ((('', 'P'), ('ASA', '')), "PASA"),
    )
)
def test_join_tuple_of_tuple(tuple_input, expected):
    result = join_tuple_of_tuple(tuple_input)
    assert result == expected


@pytest.mark.parametrize(
    ("tuple_input", "i_value" ,"expected"),
    (
        ((('', 'P'), ('ASA', ''), ('DA', 'P'), ('AAA', 'K'), ('', 'K'), ('SA', 'K')), 0, "ASADAAAASA"),
        ((('', 'P'), ('ASA', '')), 1, "P"),
    )
)
def test_join_value_of_tuple(tuple_input, i_value,expected):
    result = join_value_of_tuple(tuple_input, i_value)
    assert result == expected


@pytest.mark.parametrize(
    ("tuple_input", "expected"),
    (
        (('SSDD', 'SSA', 'SSSS', 'SSSA', 'AAAAWW'), "AAAAWW"),
        (('SSDD', 'SSA', 'SS', 'SWSSA'), None)
    )
)
def test_get_value_exceed_max_characters(tuple_input, expected):
    result = get_value_exceed_max_characters(tuple_input, 5)
    assert result == expected

