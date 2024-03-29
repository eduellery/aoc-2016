import pytest
from aoc.day_06 import Day06
from resources import read_as_string_list, file_exists

local_test = file_exists("test/day06.in")
aoc_input = Day06(read_as_string_list("test/day06.in")) if local_test else None
test_input = Day06(read_as_string_list("test/day06.example"))


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
