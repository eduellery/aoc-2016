from aoc.day_02 import Day02
from resources import read_as_string_list

aoc_input = Day02(read_as_string_list('test/day02.in'))
test_input = Day02(['ULL', 'RRDDD', 'LURDL', 'UUUUD'])


def test_solve_1_examples():
    assert test_input.solve1() == '1985'


def test_solve_1_input():
    assert aoc_input.solve1() == '99332'


def test_solve_2_examples():
    assert test_input.solve2() == '5DB3'


def test_solve_2_input():
    assert aoc_input.solve2() == 'DD483'
