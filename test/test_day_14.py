import pytest
from aoc.day_14 import Day14
from resources import read_as_string, file_exists

local_test = file_exists("test/day14.in")
aoc_input = Day14(read_as_string("test/day14.in")) if local_test else None
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
