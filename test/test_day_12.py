import pytest
from resources import file_exists, read_as_string_list

from day_12 import Day12

local_test = file_exists("res/day12.in")
aoc_input = Day12(read_as_string_list("res/day12.in")) if local_test else None
test_input = Day12(read_as_string_list("res/day12.example"))


def test_solve_1_examples():
    assert test_input.solve1() == 42


@pytest.mark.skipif(not local_test, reason="Input files can not be shared")
def test_solve_1_input():
    assert aoc_input.solve1() == 318003


def test_solve_2_examples():
    assert test_input.solve2() == 42


@pytest.mark.skipif(not local_test, reason="Input files can not be shared")
def test_solve_2_input():
    assert aoc_input.solve2() == 9227657
