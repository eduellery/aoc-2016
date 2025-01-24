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

def left_shift(n, int_to_char):
    n %= len(int_to_char)
    chars = list(generate_string(int_to_char))
    return "".join(chars[n:] + chars[:n])

def right_shift(n, int_to_char):
    n %= len(int_to_char)
    chars = list(generate_string(int_to_char))
    return "".join(chars[-n:] + chars[:-n])

def move(i, j, int_to_char):
    chars = list(generate_string(int_to_char))
    chars.insert(j, chars.pop(i))
    return "".join(chars)

def rotate(x, char_to_int, int_to_char):
    i = char_to_int[x]
    n = i + 2 if i >= 4 else i + 1
    return right_shift(n, int_to_char)

class Day21:
    def __init__(self, instructions: list[str], input: str = "abcdefgh"):
        self.input = input
        self.instructions = instructions

    def solve1(self) -> str:
        char_to_int, int_to_char = create_maps(self.input)
        for instruction in self.instructions:
            if search(r"swap position*", instruction):
                i, j = map(int, findall(r"(\d)", instruction))
                swap_position(i, j, char_to_int, int_to_char)
            if search(r"swap letter*", instruction):
                x, y = findall(r"letter (\w)", instruction)
                swap_letter(x, y, char_to_int, int_to_char)
            if search(r"reverse positions*", instruction):
                i, j = map(int, findall(r"(\d)", instruction))
                reversed = reverse_position(i, j, int_to_char)
                char_to_int, int_to_char = create_maps(reversed)
            if search(r"rotate left*", instruction):
                [n] = map(int, findall(r"(\d)", instruction))
                reversed = left_shift(n, int_to_char)
                char_to_int, int_to_char = create_maps(reversed)
            if search(r"rotate right*", instruction):
                [n] = map(int, findall(r"(\d)", instruction))
                reversed = right_shift(n, int_to_char)
                char_to_int, int_to_char = create_maps(reversed)
            if search(r"move position*", instruction):
                i, j = map(int, findall(r"(\d)", instruction))
                moved = move(i, j, int_to_char)
                char_to_int, int_to_char = create_maps(moved)
            if search(r"rotate based*", instruction):
                [x] = findall(r"letter (\w)", instruction)
                rotated = rotate(x, char_to_int, int_to_char)
                char_to_int, int_to_char = create_maps(rotated)
        return generate_string(int_to_char)

    def solve2(self) -> str:
        return "abcdefgh"
