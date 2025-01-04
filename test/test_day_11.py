import pytest
from aoc.day_11 import Day11
from resources import file_exists, read_as_string_list

local_test = file_exists("test/day11.in")
aoc_input = Day11(read_as_string_list("test/day11.in")) if local_test else None
test_input = Day11(read_as_string_list("test/day11.example"))


def test_solve_1_examples():
    assert test_input.solve1() == 9


@pytest.mark.skipif(not local_test, reason="Input files can not be shared")
def test_solve_1_input():
    assert aoc_input.solve1() == 31


def test_solve_2_examples():
    assert test_input.solve2() == 33


@pytest.mark.skipif(not local_test, reason="Input files can not be shared")
def test_solve_2_input():
    assert aoc_input.solve2() == 55
