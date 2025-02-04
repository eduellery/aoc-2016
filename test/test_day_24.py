import pytest
from resources import file_exists, read_as_string_list

from day_24 import Day24

local_test = file_exists("res/day24.in")
aoc_input = Day24(read_as_string_list("res/day24.in")) if local_test else None
test_input = Day24(read_as_string_list("res/day24.example"))


def test_solve_1_examples():
    assert test_input.solve1() == 14


@pytest.mark.skipif(not local_test, reason="Input files can not be shared")
def test_solve_1_input():
    assert aoc_input.solve1() == 474


def test_solve_2_examples():
    assert test_input.solve2() == 20


@pytest.mark.skipif(not local_test, reason="Input files can not be shared")
def test_solve_2_input():
    assert aoc_input.solve2() == 696
