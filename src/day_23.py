TOGGLES = {
    "cpy": "jnz",
    "jnz": "cpy",
    "inc": "dec",
    "dec": "inc",
    "tgl": "inc",
}

class Day23:
    def __init__(self, instructions: list[str]):
        self.original = []
        for i in instructions:
            values: list[int|str] = []
            for v in i.split(" "):
                try:
                    values.append(int(v))
                except ValueError:
                    values.append(v)
            self.original.append(tuple(values))

    def get_value(self, val):
        return val if isinstance(val, int) else self.registers[val]

    def cpy(self, val, target):
        if isinstance(target, str):
            self.registers[target] = self.get_value(val)

    def inc(self, target):
        if isinstance(target, str):
            self.registers[target] += 1

    def dec(self, target):
        if isinstance(target, str):
            self.registers[target] -= 1

    def jnz(self, val, offset):
        val = self.get_value(val)
        offset = self.get_value(offset)
        if val != 0:
            return self.pc + offset

    def tgl(self, offset):
        offset = self.get_value(offset)
        i = self.pc + offset
        if 0 <= i < len(self.instructions):
            instruction = self.instructions[i]
            new = [TOGGLES[instruction[0]]]
            new.extend(instruction[1:])
            self.instructions[i] = tuple(new)

    def solve(self, a) -> int:
        self.instructions = self.original.copy()
        self.registers = dict.fromkeys("abcd", 0)
        self.registers['a'] = a
        self.pc = 0
        while self.pc < len(self.instructions):
            instruction = self.instructions[self.pc]
            operation = getattr(self, str(instruction[0]))
            new_operation = operation(*instruction[1:])
            self.pc = self.pc + 1 if new_operation is None else new_operation
        return self.registers['a']

    def solve1(self) -> int:
        return self.solve(7)

    def solve2(self) -> int:
        return 2
