import pytest
from resources import file_exists, read_as_string_list

from day_15 import Day15

local_test = file_exists("res/day15.in")
aoc_input = Day15(read_as_string_list("res/day15.in")) if local_test else None
test_input = Day15(read_as_string_list("res/day15.example"))


def test_solve_1_examples():
    assert test_input.solve1() == 5


@pytest.mark.skipif(not local_test, reason="Input files can not be shared")
def test_solve_1_input():
    assert aoc_input.solve1() == 122318


def test_solve_2_examples():
    assert test_input.solve2() == 85


@pytest.mark.skipif(not local_test, reason="Input files can not be shared")
def test_solve_2_input():
    assert aoc_input.solve2() == 3208583
