import pytest
from resources import file_exists, read_as_string_list

from day_21 import Day21

local_test = file_exists("res/day21.in")
aoc_input = Day21(read_as_string_list("res/day21.in")) if local_test else None
test_input = Day21(read_as_string_list("res/day21.example"), "abcde")


def test_solve_1_examples():
    assert test_input.solve1() == "decab"


@pytest.mark.skipif(not local_test, reason="Input files can not be shared")
def test_solve_1_input():
    assert aoc_input.solve1() == "cbeghdaf"


#def test_solve_2_examples():
#    assert test_input.solve2() == "abcde"


#@pytest.mark.skipif(not local_test, reason="Input files can not be shared")
#def test_solve_2_input():
#    assert aoc_input.solve2() == "abcdefgh"
