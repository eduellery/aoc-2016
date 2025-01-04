import pytest
from aoc.day_07 import Day07
from resources import file_exists, read_as_string_list

local_test = file_exists("test/day07.in")
aoc_input = Day07(read_as_string_list("test/day07.in")) if local_test else None
test_part1_input = Day07(read_as_string_list("test/day07.part1.example"))
test_part2_input = Day07(read_as_string_list("test/day07.part2.example"))


def test_solve_1_examples():
    assert test_part1_input.solve1() == 2


@pytest.mark.skipif(not local_test, reason="Input files can not be shared")
def test_solve_1_input():
    assert aoc_input.solve1() == 110


def test_solve_2_examples():
    assert test_part2_input.solve2() == 3


@pytest.mark.skipif(not local_test, reason="Input files can not be shared")
def test_solve_2_input():
    assert aoc_input.solve2() == 242
