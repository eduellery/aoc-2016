import pytest
from day_06 import Day06
from resources import file_exists, read_as_string_list

local_test = file_exists("res/day06.in")
aoc_input = Day06(read_as_string_list("res/day06.in")) if local_test else None
test_input = Day06(read_as_string_list("res/day06.example"))


def test_solve_1_examples():
    assert test_input.solve1() == "easter"


@pytest.mark.skipif(not local_test, reason="Input files can not be shared")
def test_solve_1_input():
    assert aoc_input.solve1() == "qrqlznrl"


def test_solve_2_examples():
    assert test_input.solve2() == "advent"


@pytest.mark.skipif(not local_test, reason="Input files can not be shared")
def test_solve_2_input():
    assert aoc_input.solve2() == "kgzdfaon"
