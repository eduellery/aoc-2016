def is_safe(left: bool, right: bool) -> bool:
    return not (left ^ right)

def next_row(row: list[bool]) -> list[bool]:
    new_row = [True]
    for i in range(1, len(row)-1):
        new_row.append(is_safe(row[i-1], row[i+1]))
    new_row.append(True)
    return new_row

class Day18:
    def __init__(self, value: str):
        self.traps = [c == '.' for c in value]
        self.traps = [True] + self.traps + [True]

    def solve(self, rounds: int) -> int:
        row = self.traps
        count = sum(row) - 2
        for _ in range(1, rounds):
            row = next_row(row)
            count += sum(row) - 2
        return count

    def solve1(self, rounds: int = 40) -> int:
        return self.solve(rounds)

    def solve2(self) -> int:
        return self.solve(400000)
