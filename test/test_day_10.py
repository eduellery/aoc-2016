import pytest
from aoc.day_10 import Day10
from resources import read_as_string_list, file_exists

local_test = file_exists("test/day10.in")
aoc_input = Day10(read_as_string_list("test/day10.in"), 17, 61) if local_test else None
test_input = Day10(read_as_string_list("test/day10.example"), 2, 5)


def test_solve_1_examples():
    assert test_input.solve1() == 2


@pytest.mark.skipif(not local_test, reason="Input files can not be shared")
def test_solve_1_input():
    assert aoc_input.solve1() == 27


def test_solve_2_examples():
    assert test_input.solve2() == 30


@pytest.mark.skipif(not local_test, reason="Input files can not be shared")
def test_solve_2_input():
    assert aoc_input.solve2() == 13727
