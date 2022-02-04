from aoc.day_04 import Day04
from resources import read_as_text

aoc_input = Day04(read_as_text('test/day04.in'))
test_input = Day04(read_as_text('test/day04.example'))


def test_solve_1_examples():
    assert test_input.solve1() == 1_514


def test_solve_1_input():
    assert aoc_input.solve1() == 137_896


def test_solve_2_input():
    assert aoc_input.solve2() == 501
