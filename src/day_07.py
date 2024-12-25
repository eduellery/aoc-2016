from typing import List
from re import findall, search


class Day07:
    def __init__(self, values: List[str]):
        self.values = values

    def solve1(self) -> str:
        p1 = 0
        for value in self.values:
            hypernet = False
            for inside in findall(r"\[(.*?)\]", value):
                if search(r"(?!(\w)\1\1\1)(\w)(\w)\3\2", inside):
                    hypernet = True
            if not hypernet:
                for outside in findall(r"(.*?)(?:\[.*?\]|$)", value):
                    if search(r"(?!(\w)\1\1\1)(\w)(\w)\3\2", outside):
                        p1 += 1
                        break
        return p1

    def solve2(self) -> str:
        p2 = 0
        for value in self.values:
            for outside in findall(r"(.*?)(?:\[.*?\]|$)", value):
                stop = False
                for a, b in findall(r"(?=(?=(.)(?!\1)(.)\1))", outside):
                    for inside in findall(r"\[(.*?)\]", value):
                        if search(b + a + b, inside):
                            p2 += 1
                            stop = True
                    if stop:
                        break
                if stop:
                    break
        return p2
