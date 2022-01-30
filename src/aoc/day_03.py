from typing import List


class Day03:
    def __init__(self, values: List[str]):
        self.values = values

    @staticmethod
    def count_triangles(values) -> int:
        triangles = 0
        for value in values:
            sides = sorted(int(x) for x in value.split())
            if sides[0] + sides[1] > sides[2]:
                triangles += 1
        return triangles

    def get_vertical_values(self):
        a = b = c = ''
        vertical_values = []
        for i, value in enumerate(self.values):
            x, y, z = value.split()
            a += x + ' '
            b += y + ' '
            c += z + ' '
            if i % 3 == 2:
                vertical_values.extend([a, b, c])
                a = b = c = ''
        return vertical_values

    def solve1(self) -> int:
        return self.count_triangles(self.values)

    def solve2(self) -> int:
        return self.count_triangles(self.get_vertical_values())
