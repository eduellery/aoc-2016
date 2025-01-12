from hashlib import md5


class Day05:
    def __init__(self, seed: str):
        self.p1: str = ""
        self.p2: list[str] = ["deadbeef"] * 8
        i = 0
        # If the hash produces deadbeef we are doomed, but whatever :)
        # I don't want to use a list of None to avoid dealing with Optional
        while "deadbeef" in self.p2:
            digest = md5((seed + str(i)).encode("utf-8")).hexdigest()
            if digest.startswith("00000"):
                value = digest[5]
                self.p1 += value
                location = int(value, 16)
                if 0 <= location <= 7 and self.p2[location] == "deadbeef":
                    self.p2[location] = digest[6]
            i += 1

    def solve1(self) -> str:
        return self.p1[0:8]

    def solve2(self) -> str:
        return "".join(self.p2)
