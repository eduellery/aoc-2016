from collections import Counter
from re import findall
from string import ascii_lowercase


class Day04:
    def __init__(self, text: str):
        self.p1 = 0
        for encoded, sid, checksum in findall(r'([a-z-]+)(\d+)\[(\w+)\]', text):
            letters = ''.join(c for c in encoded if c in ascii_lowercase)
            most_common = [(-n, c) for c, n in Counter(letters).most_common()]
            if ''.join(c for n, c in sorted(most_common)).startswith(checksum):
                self.p1 += int(sid)
                if 'north' in encoded.translate(Day04.caesar_cipher(int(sid))):
                    self.p2 = int(sid)

    @staticmethod
    def caesar_cipher(shift):
        a_to_z = ascii_lowercase
        n_shift = shift % len(a_to_z)
        return str.maketrans(a_to_z, a_to_z[n_shift:] + a_to_z[:n_shift])

    def solve1(self) -> int:
        return self.p1

    def solve2(self) -> int:
        return self.p2
