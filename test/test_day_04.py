import pytest
from aoc.day_04 import Day04
from resources import read_as_text, file_exists

local_test =  file_exists('test/day04.in')
aoc_input = Day04(read_as_text('test/day04.in')) if local_test else None
test_part1_input = Day04(read_as_text('test/day04.part1.example'))
test_part2_input = Day04(read_as_text('test/day04.part2.example'))


def test_solve_1_examples():
    assert test_part1_input.solve1() == 1_514


@pytest.mark.skipif(not local_test, reason = 'Input files can not be shared')
def test_solve_1_input():
    assert aoc_input.solve1() == 137_896


def test_solve_2_examples():
    assert test_part2_input.solve2() == 111


@pytest.mark.skipif(not local_test, reason = 'Input files can not be shared')
def test_solve_2_input():
    assert aoc_input.solve2() == 501
