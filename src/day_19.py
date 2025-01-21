class Day19:
    def __init__(self, size: int):
        self.size = size

    def solve1(self) -> int:
        return int(bin(self.size)[3:] + "0", 2) + 1

    def solve2(self) -> int:
        if self.size == 1 or self.size == 3:
            # Corner cases...
            return self.size
        else:
            winner = 1
            while winner * 3 < self.size:
                winner *= 3
            return self.size - winner

