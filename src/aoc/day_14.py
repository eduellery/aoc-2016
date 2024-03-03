from hashlib import md5
from re import compile, search
import functools


class Day14:
    def __init__(self, salt: str):
        self.salt = salt + "{}"
        self.regex = compile(r"([abcdef0-9])\1{2}")

    @functools.lru_cache(maxsize=None)
    def getmd5(self, input: str):
        return md5(input.encode("utf-8")).hexdigest()

    def process(self):
        i = 0
        j = 0
        while True:
            match = search(self.regex, self.getmd5(self.salt.format(i)))
            if match:
                check = match.group()[0] * 5
                if any(
                    check in self.getmd5(self.salt.format(j))
                    for j in range(i + 1, i + 1001)
                ):
                    j += 1
                    if j == 64:
                        return i
            i += 1

    def solve1(self) -> int:
        return self.process()
