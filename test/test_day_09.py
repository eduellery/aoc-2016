import pytest
from day_09 import Day09
from resources import file_exists, read_as_string

local_test = file_exists("res/day09.in")
aoc_input = Day09(read_as_string("res/day09.in")) if local_test else None


@pytest.mark.parametrize(
    "test_input, expected",
    [
        ("ADVENT", 6),
        ("A(1x5)BC", 7),
        ("(3x3)XYZ", 9),
        ("A(2x2)BCD(2x2)EFG", 11),
        ("(6x1)(1x3)A", 6),
        ("X(8x2)(3x3)ABCY", 18),
    ],
)
def test_solve_1_examples(test_input: str, expected: int):
    assert Day09(test_input).solve1() == expected


@pytest.mark.skipif(not local_test, reason="Input files can not be shared")
def test_solve_1_input():
    assert aoc_input.solve1() == 120765


@pytest.mark.parametrize(
    "test_input, expected",
    [
        ("(3x3)XYZ", 9),
        ("X(8x2)(3x3)ABCY", 20),
        ("(27x12)(20x12)(13x14)(7x10)(1x12)A", 241920),
        ("(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN", 445),
    ],
)
def test_solve_2_examples(test_input: str, expected: int):
    assert Day09(test_input).solve2() == expected


@pytest.mark.skipif(not local_test, reason="Input files can not be shared")
def test_solve_2_input():
    assert aoc_input.solve2() == 11658395076
