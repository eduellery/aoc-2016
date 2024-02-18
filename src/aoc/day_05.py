from hashlib import md5


class Day05:
    def __init__(self, seed: str):
        self.p1 = ""
        self.p2 = [None] * 8
        i = 0
        while None in self.p2:
            digest = md5((seed + str(i)).encode("utf-8")).hexdigest()
            if digest.startswith("00000"):
                value = digest[5]
                self.p1 += value
                location = int(value, 16)
                if 0 <= location <= 7 and self.p2[location] is None:
                    self.p2[location] = digest[6]
            i += 1

    def solve1(self) -> str:
        return self.p1[0:8]

    def solve2(self) -> str:
        return "".join(self.p2)
