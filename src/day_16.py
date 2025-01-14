def invert_reverse(value: str) -> str:
    return "".join('0' if c == '1' else '1' for c in value[::-1])

def fill(value: str, size: int) -> str:
    result = value
    while (len(result) < size):
        result = result + "0" + invert_reverse(result)
    return result[:size]

def reduce(value: str) -> str:
    result = []
    for i in range(0, len(value), 2):
        result.append("1" if value[i] == value[i+1] else "0")
    return "".join(result)

def checksum(value: str) -> str:
    result = reduce(value)
    while len(result) % 2 == 0:
        result = reduce(result)
    return result

class Day16:
    def __init__(self, seed: str):
        self.seed = seed

    def solve(self, size: int = 20) -> str:
        return checksum(fill(self.seed, size))
