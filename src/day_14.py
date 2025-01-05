import functools
from hashlib import md5
from re import compile, search


@functools.lru_cache(maxsize=100000)
def getmd5(input: str):
    return md5(input.encode("utf-8")).hexdigest()

@functools.lru_cache(maxsize=100000)
def getlongmd5(input: str):
    for _ in range(2017):
        input = md5(input.encode("utf-8")).hexdigest()
    return input

class Day14:
    def __init__(self, salt: str):
        self.salt = salt + "{}"
        self.regex = compile(r"([abcdef0-9])\1{2}")

    def process(self, long=False):
        hash_function = getlongmd5 if long else getmd5
        i = 0
        j = 0
        while True:
            match = search(self.regex, hash_function(self.salt.format(i)))
            if match:
                check = match.group()[0] * 5
                if any(
                    check in hash_function(self.salt.format(j))
                    for j in range(i + 1, i + 1001)
                ):
                    j += 1
                    if j == 64:
                        return i
            i += 1

    def solve1(self) -> int:
        return self.process()

    def solve2(self) -> int:
        return self.process(True)
