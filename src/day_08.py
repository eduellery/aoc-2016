from typing import List


class Day08:
    def __init__(self, values: List[str]):
        h, w = 6, 50
        self.grid = [[0] * w for _ in range(h)]

        for value in values:
            if value.startswith("rect"):
                x, y = map(int, value.split("rect ")[1].split("x"))
                for a in range(y):
                    for b in range(x):
                        self.grid[a][b] = 1
            elif value.startswith("rotate column"):
                x, vshift = map(int, value.split("rotate column x=")[1].split(" by "))
                column = [row[x] for row in self.grid]
                for a in range(h):
                    self.grid[a][x] = column[a - vshift]
            elif value.startswith("rotate row"):
                y, hshift = map(int, value.split("rotate row y=")[1].split(" by "))
                self.grid[y] = self.grid[y][-hshift:] + self.grid[y][:-hshift]

    def solve1(self) -> int:
        return sum(sum(line) for line in self.grid)

    def solve2(self) -> str:
        return "\n" + (
            "\n".join("".join("#" if v else " " for v in row) for row in self.grid)
        )
