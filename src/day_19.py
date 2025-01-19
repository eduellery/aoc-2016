class Day19:
    def __init__(self, size: int):
        self.elves = []
        for i in range(0, size - 1):
            self.elves.append(i + 1)
        self.elves.append(0)

    def solve1(self) -> int:
        i = 0
        while self.elves[i] != i:
            j = self.elves[self.elves[i]]
            self.elves[i] = j
            i = j
        return i + 1
