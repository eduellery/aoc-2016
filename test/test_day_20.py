import pytest
from resources import file_exists, read_as_string_list

from day_20 import Day20

local_test = file_exists("res/day20.in")
aoc_input = Day20(read_as_string_list("res/day20.in")) if local_test else None
test_input = Day20(read_as_string_list("res/day20.example"))


def test_solve_1_examples():
    assert test_input.solve1(9) == 3


@pytest.mark.skipif(not local_test, reason="Input files can not be shared")
def test_solve_1_input():
    assert aoc_input.solve1() == 4793564


#@pytest.mark.skipif(not local_test, reason="Input files can not be shared")
#def test_solve_2_input():
#    assert aoc_input.solve2() == 2
