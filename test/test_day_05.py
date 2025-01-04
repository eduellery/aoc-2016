import pytest
from resources import file_exists, read_as_string

from day_05 import Day05

local_test = file_exists("res/day05.in")
aoc_input = Day05(read_as_string("res/day05.in")) if local_test else None
test_input = Day05("abc")


def test_solve_1_examples():
    assert test_input.solve1() == "18f47a30"


@pytest.mark.skipif(not local_test, reason="Input files can not be shared")
def test_solve_1_input():
    assert aoc_input.solve1() == "d4cd2ee1"


def test_solve_2_examples():
    assert test_input.solve2() == "05ace8e3"


@pytest.mark.skipif(not local_test, reason="Input files can not be shared")
def test_solve_2_input():
    assert aoc_input.solve2() == "f2c730e5"
