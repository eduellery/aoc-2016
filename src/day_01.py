from typing import List


class Day01:
    def __init__(self, instructions: List[str]):
        position = 0 + 0j
        direction = 0 + 1j
        seen = {position}
        found = None
        for instruction in instructions:
            direction *= -1j if instruction[0] == "R" else 1j
            distance = int(instruction[1:])
            for i in range(distance):
                position += direction
                if not found and position in seen:
                    found = position
                seen.add(position)
        self.final = position
        self.twice = found if found else 0 + 0j

    @staticmethod
    def man_distance(a, b) -> int:
        return int(abs(a) + abs(b))

    def solve1(self) -> int:
        return Day01.man_distance(self.final.real, self.final.imag)

    def solve2(self) -> int:
        return Day01.man_distance(self.twice.real, self.twice.imag)
