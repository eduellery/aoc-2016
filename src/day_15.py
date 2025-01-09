from re import findall


def find_alignment(factors):
    t = 0
    while True:
        if all(t % mod == remainder for mod, remainder in factors):
            return t
        t += 1

class Day15:
    def __init__(self, values: list[str]):
        self.factors = []
        for i, value in enumerate(values, start=1):
            _, mod, _, x = map(int, findall(r"\b\d+\b", value))
            x = (mod - x - i) % mod
            self.factors.append((mod, x))

    def solve1(self) -> int:
        return find_alignment(self.factors)

    def solve2(self) -> int:
        return 2
