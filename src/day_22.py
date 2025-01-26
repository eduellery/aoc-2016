from re import search, findall

class Day22:
    def __init__(self, volumes: list[str]):
        self.input = []
        for v in volumes[2:]:
            r = search(r"/dev/grid/node-x(\d+)-y(\d+)\s+(\d+)T\s+(\d+)T\s+(\d+)T", v)
            x, y, t, u, a = map(int, r.groups())
            self.input.append((x, y, t, u, a))

    def solve1(self) -> int:
        count = 0
        for x, y, _, u, _ in self.input: # Node A
            for i, j, _, _, a in self.input: # Node B
                if (x != i or y != j) and u > 0 and u <= a:
                    count += 1
        return count

    def solve2(self) -> int:
        return 2
