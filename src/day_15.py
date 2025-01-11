from re import findall


def normalize(discs):
    factors = []
    for i, value in enumerate(discs, start=1):
        mod, x = value
        x = (mod - x - i) % mod
        factors.append((mod, x))
    return factors


def find_alignment(factors):
    t = 0
    while True:
        if all(t % mod == remainder for mod, remainder in factors):
            return t
        t += 1

class Day15:
    def __init__(self, values: list[str]):
        self.discs = []
        for value in values:
            _, mod, _, x = map(int, findall(r"\b\d+\b", value))
            self.discs.append((mod, x))

    def normalize(self, discs):
        factors = []
        for i, value in enumerate(discs, start=1):
            mod, x = value
            x = (mod - x - i) % mod
            factors.append((mod, x))
        return factors

    def solve1(self) -> int:
        return find_alignment(normalize(self.discs))

    def solve2(self) -> int:
        return find_alignment(normalize(self.discs + [(11,0)]))
