from collections import Counter


class Day06:
    def __init__(self, words: list[str]):
        self.count = [Counter(x).most_common() for x in zip(*words, strict=False)]

    def solve1(self) -> str:
        return "".join(x[0][0] for x in self.count)

    def solve2(self) -> str:
        return "".join(x[-1][0] for x in self.count)
