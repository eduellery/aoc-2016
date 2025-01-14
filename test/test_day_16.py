
import pytest
from resources import file_exists, read_as_string

from day_16 import Day16

local_test = file_exists("res/day16.in")
aoc_input = Day16(read_as_string("res/day16.in")) if local_test else None


def test_solve_1_examples():
    assert Day16("10000").solve() == "01100"


@pytest.mark.skipif(not local_test, reason="Input files can not be shared")
def test_solve_1_input():
    assert aoc_input.solve(272) == "10010010110011010"


@pytest.mark.skipif(not local_test, reason="Input files can not be shared")
def test_solve_2_input():
    assert aoc_input.solve(35651584) == "01010100101011100"
