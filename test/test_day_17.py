import pytest
from resources import file_exists, read_as_string

from day_17 import Day17

local_test = file_exists("res/day17.in")
aoc_input = Day17(read_as_string("res/day17.in")) if local_test else None


@pytest.mark.parametrize(
    "test_input, expected",
    [
        ("ihgpwlah", "DDRRRD"),
        ("kglvqrro", "DDUDRLRRUDRD"),
        ("ulqzkmiv", "DRURDRUDDLLDLUURRDULRLDUUDDDRR"),
    ],
)
def test_solve_1_examples(test_input: str, expected: str):
    assert Day17(test_input).solve1() == expected


@pytest.mark.skipif(not local_test, reason="Input files can not be shared")
def test_solve_1_input():
    assert aoc_input.solve1() == "DUDDRLRRRD"
