import pytest
from day_02 import Day02
from resources import file_exists, read_as_string_list

local_test = file_exists("res/day02.in")
aoc_input = Day02(read_as_string_list("res/day02.in")) if local_test else None
test_input = Day02(["ULL", "RRDDD", "LURDL", "UUUUD"])


def test_solve_1_examples():
    assert test_input.solve1() == "1985"


@pytest.mark.skipif(not local_test, reason="Input files can not be shared")
def test_solve_1_input():
    assert aoc_input.solve1() == "99332"


def test_solve_2_examples():
    assert test_input.solve2() == "5DB3"


@pytest.mark.skipif(not local_test, reason="Input files can not be shared")
def test_solve_2_input():
    assert aoc_input.solve2() == "DD483"
