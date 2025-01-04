
commands = {"U": -5, "D": 5, "R": 1, "L": -1}
translate = {
    3: 1,
    7: 2,
    8: 3,
    9: 4,
    11: 5,
    12: 6,
    13: 7,
    14: 8,
    15: 9,
    17: 10,
    18: 11,
    19: 12,
    23: 13,
}


class Day02:
    def __init__(self, instructions: list[str]):
        self.code_1 = ""
        self.code_2 = ""
        idx_1 = 5
        idx_2 = 11

        for value in instructions:
            for char in value.strip():
                idx_1 = Day02.compute_idx_1(idx_1, char)
                idx_2 = Day02.compute_idx_2(idx_2, char)
            self.code_1 += str(idx_1)
            self.code_2 += str("%x".upper() % translate.get(idx_2))

    @staticmethod
    def compute_idx_1(value, char):
        if char == "U" and value not in [1, 2, 3]:
            value -= 3
        elif char == "D" and value not in [7, 8, 9]:
            value += 3
        elif char == "L" and value not in [1, 4, 7]:
            value -= 1
        elif char == "R" and value not in [3, 6, 9]:
            value += 1
        return value

    @staticmethod
    def compute_idx_2(value, char):
        step = commands.get(char)
        if translate.get(value + step):
            value += step
        return value

    def solve1(self) -> str:
        return self.code_1

    def solve2(self) -> str:
        return self.code_2
