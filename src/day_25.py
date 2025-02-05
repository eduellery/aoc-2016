from itertools import count

TOGGLES = {
    "cpy": "jnz",
    "jnz": "cpy",
    "inc": "dec",
    "dec": "inc",
    "tgl": "inc",
}

class Day25:
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
        self.registers[target] = self.get_value(val)

    def inc(self, target):
        self.registers[target] += 1

    def dec(self, target):
        self.registers[target] -= 1

    def jnz(self, val, offset):
        val = self.get_value(val)
        offset = self.get_value(offset)
        if val != 0:
            return self.pc + offset

    def out(self, val):
        state = (self.pc, tuple(self.registers[x] for x in "abcd"))
        if state in self.states:
            return 999 # End execution
        self.states.append(state)
        self.output.append(self.get_value(val))

    def is_optimized(self):
        i_d_reg = self.is_addiction_loop()
        if i_d_reg is None:
            return False

        i_reg, d_reg = i_d_reg
        m_reg = self.is_multiplication_loop(i_reg, d_reg)

        self.registers[i_reg] += self.registers[m_reg] * self.registers[d_reg]
        self.registers[d_reg] = 0
        self.registers[m_reg] = 0
        self.pc += 5

        return True

    def is_addiction_loop(self):
        next = self.instructions[self.pc:self.pc + 3]
        if len(next) != 3:
            return

        i0, i1, i2 = next
        o0, o1, o2 = i0[0], i1[0], i2[0]
        if (o0, o1, o2) not in [("inc", "dec", "jnz"), ("dec", "inc", "jnz")]:
            return

        d_reg = (i0 if o0 == "dec" else i1)[1]
        i_reg = (i0 if o0 == "inc" else i1)[1]

        return i_reg, d_reg

    def is_multiplication_loop(self, i_reg, d_reg):
        next = self.instructions[self.pc + 3:self.pc + 5]
        i0, i1 = next
        _o0, _o1 = i0[0], i1[0]
        m_reg = i0[1]
        return m_reg

    def solve(self, a):
        self.instructions = self.original.copy()
        self.registers = dict.fromkeys("abcd", 0)
        self.registers['a'] = a
        self.pc = 0
        self.states = []
        self.output = []
        while self.pc < len(self.instructions):
            if self.is_optimized():
                continue
            instruction = self.instructions[self.pc]
            operation = getattr(self, str(instruction[0]))
            new_operation = operation(*instruction[1:])
            self.pc = self.pc + 1 if new_operation is None else new_operation

    def solve1(self) -> int:
        for a in count(start = 1):
            self.solve(a)
            if self.output == [0, 1]*(len(self.output)//2):
               break
        return a
