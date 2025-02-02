import pytest
from resources import file_exists, read_as_string_list

from day_23 import Day23

local_test = file_exists("res/day23.in")
aoc_input = Day23(read_as_string_list("res/day23.in")) if local_test else None
test_input = Day23(read_as_string_list("res/day23.example"))


def test_solve_1_examples():
    assert test_input.solve1() == 3


@pytest.mark.skipif(not local_test, reason="Input files can not be shared")
def test_solve_1_input():
    assert aoc_input.solve1() == 12624


@pytest.mark.skipif(not local_test, reason="Input files can not be shared")
def test_solve_2_input():
    assert aoc_input.solve2() == 479009184
