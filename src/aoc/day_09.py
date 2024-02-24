class Day09:
    def __init__(self, value: str):
        self.value = value

    def decompressed_length(self, value: str, recursive: bool):
        if "(" not in value:
            return len(value)
        ret = 0
        while "(" in value:
            ret += value.find("(")
            value = value[value.find("(") :]
            pre, pos = map(int, value[1 : value.find(")")].split("x"))
            value = value[value.find(")") + 1 :]
            if recursive:
                ret += self.decompressed_length(value[:pre], recursive) * pos
            else:
                ret += len(value[:pre]) * pos
            value = value[pre:]
        ret += len(value)
        return ret

    def solve1(self) -> int:
        return self.decompressed_length(self.value, False)

    def solve2(self) -> str:
        return self.decompressed_length(self.value, True)
