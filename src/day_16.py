def reverse(value: str) -> str:
    return value[::-1]

def invert(value: str) -> str:
    return "".join('0' if c == '1' else '1' for c in value)

def fill(value: str, size: int) -> str:
    result = value
    while (len(result) < size):
        result = result + "0" + invert(reverse(result))
    return result[:size]

def reduce(value: str) -> str:
    result = ""
    for i in range(0, len(value), 2):
        result += "1" if value[i:i+2] in ["00", "11"] else "0"
    return result

def checksum(value: str) -> str:
    result = value
    while len(result) % 2 == 0:
        result = reduce(result)
    return result

class Day16:
    def __init__(self, seed: str, size: int = 20):
        self.seed = seed
        self.size = size

    def solve1(self) -> str:
        return checksum(fill(self.seed, self.size))

    def solve2(self) -> int:
        return 2
