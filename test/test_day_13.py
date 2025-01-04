import pytest
from resources import file_exists, read_as_string

from day_13 import Day13

local_test = file_exists("res/day13.in")
aoc_input = Day13(int(read_as_string("res/day13.in"))) if local_test else None
test_input = Day13(10, 7, 4)


def test_solve_1_examples():
    assert test_input.solve1() == 11


@pytest.mark.skipif(not local_test, reason="Input files can not be shared")
def test_solve_1_input():
    assert aoc_input.solve1() == 90


def test_solve_2_examples():
    assert test_input.solve2() == 151


@pytest.mark.skipif(not local_test, reason="Input files can not be shared")
def test_solve_2_input():
    assert aoc_input.solve2() == 135
