from typing import List

import pytest
from aoc.day_01 import Day01

from resources import read_as_text

aoc_input = Day01(read_as_text('test/day01.in').split(', '))


@pytest.mark.parametrize("test_input, expected", [
    (['R2', 'L3'], 5),
    (['R2', 'R2', 'R2'], 2),
    (['R5', 'L5', 'R5', 'R3'], 12),
])
def test_solve_1_examples(test_input: List[str], expected: int):
    assert Day01(test_input).solve1() == expected


def test_solve_1_input():
    assert aoc_input.solve1() == 287


def test_solve_2_examples():
    assert Day01(['R8', 'R4', 'R4', 'R8']).solve2() == 4


def test_solve_2_input():
    assert aoc_input.solve2() == 133
