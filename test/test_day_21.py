import pytest
from resources import file_exists, read_as_string_list

from day_21 import Day21

local_test = file_exists("res/day21.in")
aoc_input_1 = Day21(read_as_string_list("res/day21.in"), "abcdefgh") if local_test else None
aoc_input_1_reversed = Day21(read_as_string_list("res/day21.in"), "cbeghdaf") if local_test else None
aoc_input_2 = Day21(read_as_string_list("res/day21.in"), "fbgdceah") if local_test else None
test_input_1 = Day21(read_as_string_list("res/day21.example"), "abcde")
test_input_2 = Day21(read_as_string_list("res/day21.example"), "decab")


def test_solve_1_examples():
    assert test_input_1.solve1() == "decab"


@pytest.mark.skipif(not local_test, reason="Input files can not be shared")
def test_solve_1_input():
    assert aoc_input_1.solve1() == "cbeghdaf"


def test_solve_2_examples():
    assert test_input_2.solve2() == "abcde"


@pytest.mark.skipif(not local_test, reason="Input files can not be shared")
def test_solve_2_inverse_of_solve_1():
    assert aoc_input_1_reversed.solve2() == "abcdefgh"


@pytest.mark.skipif(not local_test, reason="Input files can not be shared")
def test_solve_2_input():
    assert aoc_input_2.solve2() == "bacdefgh"
