
import pytest
from aoc.day_01 import Day01
from resources import file_exists, read_as_text

local_test = file_exists("test/day01.in")
aoc_input = Day01(read_as_text("test/day01.in").split(", ")) if local_test else None


@pytest.mark.parametrize(
    "test_input, expected",
    [
        (["R2", "L3"], 5),
        (["R2", "R2", "R2"], 2),
        (["R5", "L5", "R5", "R3"], 12),
    ],
)
def test_solve_1_examples(test_input: list[str], expected: int):
    assert Day01(test_input).solve1() == expected


@pytest.mark.skipif(not local_test, reason="Input files can not be shared")
def test_solve_1_input():
    assert aoc_input.solve1() == 287


def test_solve_2_examples():
    assert Day01(["R8", "R4", "R4", "R8"]).solve2() == 4


@pytest.mark.skipif(not local_test, reason="Input files can not be shared")
def test_solve_2_input():
    assert aoc_input.solve2() == 133
