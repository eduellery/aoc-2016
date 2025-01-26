import pytest
from resources import file_exists, read_as_string_list

from day_22 import Day22

local_test = file_exists("res/day22.in")
aoc_input = Day22(read_as_string_list("res/day22.in")) if local_test else None
test_input = Day22(read_as_string_list("res/day22.example"))


def test_solve_1_examples():
    assert test_input.solve1() == 7


@pytest.mark.skipif(not local_test, reason="Input files can not be shared")
def test_solve_1_input():
    assert aoc_input.solve1() == 985


def test_solve_2_examples():
    assert test_input.solve2() == 2


@pytest.mark.skipif(not local_test, reason="Input files can not be shared")
def test_solve_2_input():
    assert aoc_input.solve2() == 2
