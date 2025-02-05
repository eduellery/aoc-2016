import pytest
from resources import file_exists, read_as_string_list

from day_25 import Day25

local_test = file_exists("res/day25.in")
aoc_input = Day25(read_as_string_list("res/day25.in")) if local_test else None


@pytest.mark.skipif(not local_test, reason="Input files can not be shared")
def test_solve_1_input():
    assert aoc_input.solve1() == 196
