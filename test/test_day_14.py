import pytest
from day_14 import Day14
from resources import file_exists, read_as_string

local_test = file_exists("res/day14.in")
aoc_input = Day14(read_as_string("res/day14.in")) if local_test else None
test_input = Day14("abc")


def test_solve_1_examples():
    assert test_input.solve1() == 22728


@pytest.mark.skipif(not local_test, reason="Input files can not be shared")
def test_solve_1_input():
    assert aoc_input.solve1() == 35186


def test_solve_2_examples():
    assert test_input.solve2() == 22551


@pytest.mark.skipif(not local_test, reason="Input files can not be shared")
def test_solve_2_input():
    assert aoc_input.solve2() == 22429
