import pytest
from resources import file_exists, read_as_string

from day_18 import Day18

local_test = file_exists("res/day18.in")
aoc_input = Day18(read_as_string("res/day18.in")) if local_test else None


@pytest.mark.parametrize(
    "test_input, rounds, expected",
    [
        ("..^^.", 3, 6),
        (".^^.^.^^^^", 10, 38),
    ],
)
def test_solve_1_examples(test_input: str, rounds: int, expected: int):
    assert Day18(test_input).solve1(rounds) == expected


@pytest.mark.skipif(not local_test, reason="Input files can not be shared")
def test_solve_1_input():
    assert aoc_input.solve1() == 2013


@pytest.mark.skipif(not local_test, reason="Input files can not be shared")
def test_solve_2_input():
    assert aoc_input.solve2() == 20006289
