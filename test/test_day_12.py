import pytest
from aoc.day_12 import Day12
from resources import file_exists, read_as_string_list

local_test = file_exists("test/day12.in")
aoc_input = Day12(read_as_string_list("test/day12.in")) if local_test else None
test_input = Day12(read_as_string_list("test/day12.example"))


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
