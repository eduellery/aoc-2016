import pytest
from resources import file_exists, read_as_int

from day_19 import Day19

local_test = file_exists("res/day19.in")
aoc_input = Day19(read_as_int("res/day19.in")) if local_test else None


def test_solve_1_examples():
    assert Day19(5).solve1() == 3


@pytest.mark.skipif(not local_test, reason="Input files can not be shared")
def test_solve_1_input():
    assert aoc_input.solve1() == 1841611


@pytest.mark.parametrize(
    "rounds, expected",
    [
        (1, 1),
        (2, 1),
        (3, 3),
        (5, 2),
        (60, 33),
        (100, 19),
    ],
)
def test_solve_2_examples(rounds: int, expected: int):
    assert Day19(rounds).solve2() == expected


@pytest.mark.skipif(not local_test, reason="Input files can not be shared")
def test_solve_2_input():
    assert aoc_input.solve2() == 1423634
