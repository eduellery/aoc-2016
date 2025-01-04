import pytest
from aoc.day_03 import Day03
from resources import file_exists, read_as_string_list

local_test = file_exists("test/day03.in")
aoc_input = Day03(read_as_string_list("test/day03.in")) if local_test else None
test_input = Day03(["5 10 25", "5 5 10", "5 5 9"])


def test_solve_1_examples():
    assert test_input.solve1() == 1


@pytest.mark.skipif(not local_test, reason="Input files can not be shared")
def test_solve_1_input():
    assert aoc_input.solve1() == 917


def test_solve_2_examples():
    assert test_input.solve2() == 1


@pytest.mark.skipif(not local_test, reason="Input files can not be shared")
def test_solve_2_input():
    assert aoc_input.solve2() == 1_649
