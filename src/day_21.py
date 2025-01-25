from re import findall, search


def create_maps(string):
    char_to_int = {}
    int_to_char = {}
    for i, char in enumerate(string):
        char_to_int[char] = i
        int_to_char[i] = char
    return char_to_int, int_to_char

def generate_string(map):
    return "".join(map[n] for n in range(0, len(map)))

def swap_position(i, j, char_to_int, int_to_char):
    x = int_to_char[i]
    y = int_to_char[j]
    int_to_char[i] = y
    int_to_char[j] = x
    char_to_int[y] = i
    char_to_int[x] = j

def swap_letter(x, y, char_to_int, int_to_char):
    i = char_to_int[x]
    j = char_to_int[y]
    char_to_int[y] = i
    char_to_int[x] = j
    int_to_char[i] = y
    int_to_char[j] = x

def reverse_position(i, j, int_to_char):
    chars = list(generate_string(int_to_char))
    chars[i:j+1] = reversed(chars[i:j+1])
    return "".join(chars)

def shift(n, int_to_char, right, reverse):
    n %= len(int_to_char)
    chars = list(generate_string(int_to_char))
    if reverse:
        right = not right
    if right:
        n = -n
    return "".join(chars[n:] + chars[:n])

def move(i, j, int_to_char, reverse):
    if reverse:
        i, j = j, i
    chars = list(generate_string(int_to_char))
    chars.insert(j, chars.pop(i))
    return "".join(chars)

def rotate(x, char_to_int, int_to_char, reverse):
    i = char_to_int[x]
    if reverse:
        if i % 2:
            steps = (i + 1) // 2
        elif i == 0:
            steps = 1
        else:
            steps = ((i + len(char_to_int)) // 2) + 1
        return shift(steps, int_to_char, True, reverse)
    else:
        return shift(i + 2 if i >= 4 else i + 1, int_to_char, True, reverse)

class Day21:
    def __init__(self, instructions: list[str], input: str):
        self.input = input
        self.instructions = instructions

    def solve(self, reverse: int = False) -> str:
        char_to_int, int_to_char = create_maps(self.input)
        instructions = self.instructions if not reverse else self.instructions[::-1]
        for instruction in instructions:
            if search(r"swap position*", instruction):
                i, j = map(int, findall(r"(\d)", instruction))
                swap_position(i, j, char_to_int, int_to_char)
            elif search(r"swap letter*", instruction):
                x, y = findall(r"letter (\w)", instruction)
                swap_letter(x, y, char_to_int, int_to_char)
            elif search(r"reverse positions*", instruction):
                i, j = map(int, findall(r"(\d)", instruction))
                reversed = reverse_position(i, j, int_to_char)
                char_to_int, int_to_char = create_maps(reversed)
            elif search(r"move position*", instruction):
                i, j = map(int, findall(r"(\d)", instruction))
                moved = move(i, j, int_to_char, reverse)
                char_to_int, int_to_char = create_maps(moved)
            elif search(r"rotate based*", instruction):
                [x] = findall(r"letter (\w)", instruction)
                rotated = rotate(x, char_to_int, int_to_char, reverse)
                char_to_int, int_to_char = create_maps(rotated)
            else: # Rotate left or right...
                [n] = map(int, findall(r"(\d)", instruction))
                right = search(r"right", instruction)
                reversed = shift(n, int_to_char, right, reverse)
                char_to_int, int_to_char = create_maps(reversed)
        return generate_string(int_to_char)

    def solve1(self) -> str:
        return self.solve()

    def solve2(self) -> str:
        return self.solve(True)
