from typing import List, Set

class Day13:
    def __init__(self, input: int, a = 31, b = 39):
        self.input = input
        self.seen = {}
        self.a = a
        self.b = b
        frontier = [(1, 1, 0)]
        while len(frontier) > 0:
            new = frontier.pop()
            self.seen[(new[0], new[1])] = new[2]
            frontier += [x for x in self.next(new) if not (x[0], x[1]) in self.seen or self.seen[(x[0], x[1])] > x[2]]

    def sum(self, pair: List[int]):
        num = pair[0] * pair[0] + 3 * pair[0] + 2 * pair[0] * pair[1] + pair[1] + pair[1] * pair[1] + self.input
        return bin(num).count('1')

    def wall(self, pair: List[int]):
        inside = pair[0] >= 0 and pair[1] >= 0
        return self.sum(pair) %2 == 0 and inside
        
    def next(self, pair: List[int]):
        coordinates = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        path = []
        for x in coordinates:
            if self.wall((x[0] + pair[0], x[1] + pair[1])):
                path.append((x[0] + pair[0], x[1] + pair[1], pair[2] + 1))
        return path

    def solve1(self) -> int:
        return self.seen[self.a, self.b]

    def solve2(self) -> str:
        return len([self.seen[x] for x in self.seen.keys() if self.seen[x] <= 50])
