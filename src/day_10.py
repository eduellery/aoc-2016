from collections import defaultdict
from re import findall


class Day10:
    def __init__(self, values: list[str], chip1: int, chip2: int):
        bot = defaultdict(list)
        output = defaultdict(list)
        pipeline = {}
        for value in values:
            if value.startswith("value"):
                n, b = map(int, findall(r"-?\d+", value))
                bot[b].append(n)
            else: # value.startswith("bot")
                who, n1, n2 = map(int, findall(r"-?\d+", value))
                t1, t2 = findall(r" (bot|output)", value)
                pipeline[who] = (t1, n1), (t2, n2)

        while bot:
            for k, v in dict(bot).items():
                if len(v) == 2:
                    v1, v2 = sorted(bot.pop(k))
                    if v1 == chip1 and v2 == chip2:
                        self.p1 = k
                    (t1, n1), (t2, n2) = pipeline[k]
                    eval(t1)[n1].append(v1)
                    eval(t2)[n2].append(v2)

        a, b, c = (output[k][0] for k in [0, 1, 2])
        self.p2 = a * b * c

    def solve1(self) -> int:
        return self.p1

    def solve2(self) -> str:
        return self.p2
