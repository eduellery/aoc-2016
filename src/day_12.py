

class Day12:
    def __init__(self, values: list[str]):
        self.instructions = []
        for value in values:
            self.instructions.append(value.split(' '))

    def read(self, registers: list[int], value: str):
        try:
            return int(value)
        except ValueError:
            return registers[value]
        
    def get_register(self, instructions: dict[str, int], register: str, a = 0, b = 0, c = 0, d = 0):
        ip = 0
    
        registers = {
            'a': a,
            'b': b,
            'c': c,
            'd': d
        }

        while True:
            if ip >= len(instructions):
                break
            ins = instructions[ip]
            if ins[0] == 'cpy':
                registers[ins[2]] = self.read(registers, ins[1])
            elif ins[0] == 'inc':
                registers[ins[1]] += 1
            elif ins[0] == 'dec':
                registers[ins[1]] -= 1    
            elif ins[0] == 'jnz' and self.read(registers, ins[1]) != 0:                
                ip += self.read(registers, ins[2])
                ip -= 1
            ip += 1

        return registers[register]

    def solve1(self) -> int:
        return self.get_register(self.instructions, 'a')

    def solve2(self) -> str:
        return self.get_register(self.instructions, 'a', c = 1)
