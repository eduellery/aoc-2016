from typing import List
from re import findall

class Day11:
    def __init__(self, values: List[str]):
        self.value = values
        self.p1 = [0,0,0,0]
        i = 0
        for value in values:
            self.p1[i] = len(findall(r'(generator|microchip)', value))
            i += 1
        self.p2 = self.p1[:]
        self.p2[0] += 4

    def count_moves(self, items: List[int]):
        moves = 0
        while items[-1] != sum(items):
            base_floor = 0
            while items[base_floor] == 0:
                base_floor += 1
            moves += 2 * (items[base_floor] - 1) - 1
            items[base_floor + 1] += items[base_floor]
            items[base_floor] = 0
        return moves

    def solve1(self) -> int:
        return self.count_moves(self.p1)

    def solve2(self) -> str:
        return self.count_moves(self.p2)
