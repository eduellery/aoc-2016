class Day19:
    def __init__(self, size: int):
        self.size = size

    def solve1(self) -> int:
        return int(bin(self.size)[3:] + "0", 2) + 1

    def solve2(self) -> int:
        elf = 1
        while elf * 3 < self.size:
            elf *= 3
        return self.size - elf
