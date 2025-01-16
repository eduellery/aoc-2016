from hashlib import md5

DIRECTIONS = ['U','D','L','R']
MOVE = [(0, -1), (0, 1), (-1, 0), (1, 0)]

def hash(value: str) -> str:
    return md5(value.encode("utf-8")).hexdigest()[:4]

def get_directions(value: str) -> list[bool]:
    return [c in ['b','c','d','e','f'] for c in value]

def reached_vault(value: str) -> bool:
    (x, y) = (0, 0)
    for c in value:
        if c == 'U':
            y -= 1
        elif c == 'D':
            y += 1
        elif c == 'L':
            x -= 1
        else: # c == 'R':
            x += 1
    return x == 3 and y == 3

def solve(values: list[list], length: int, shortest: bool = True, solution: str = "") -> str:
    next_values = []
    for value, x, y in values:
        if reached_vault(value[length:]):
            new_solution = value[length:]
            if shortest:
                return new_solution
            elif len(new_solution) > len(solution):
                solution = new_solution
        else:
            for i, open in enumerate(get_directions(hash(value))):
                a = x + MOVE[i][0]
                b = y + MOVE[i][1]
                if open and a >= 0 and a < 4 and b >= 0 and b < 4:
                    next_values.append([value + DIRECTIONS[i], a, b])
    if next_values == []:
        return solution
    return solve(next_values, length, shortest, solution)

class Day17:
    def __init__(self, value: str):
        self.value = value

    def solve1(self) -> str:
        return solve([[self.value, 0, 0]], len(self.value))

    def solve2(self) -> str:
        return len(solve([[self.value, 0, 0]], len(self.value), False))
