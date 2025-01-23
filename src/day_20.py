def remove(ips, low, high):
    new_ranges = []
    for current_range in ips:
        new_ranges.extend(clip(current_range, (low, high)))
    return new_ranges

def clip(current, clipped):
    if current[0] > clipped[1] or current[1] < clipped[0]:
        return [current]
    result = []
    if current[0] < clipped[0]:
        result.append((current[0], clipped[0] - 1))
    if clipped[1] < current[1]:
        result.append((clipped[1] + 1, current[1]))
    return result

class Day20:
    def __init__(self, values: list[str], max: int = 4294967295):
        ranges = []
        for v in values:
            ranges.append(tuple(map(int, v.split("-"))))
        self.allowed_ips = [(0, max)]
        for pair in ranges:
            self.allowed_ips = remove(self.allowed_ips, pair[0], pair[1])


    def solve1(self, ) -> int:
        return self.allowed_ips[0][0]

    def solve2(self) -> int:
        count = 0
        for pair in self.allowed_ips:
            count += pair[1] - pair[0] + 1
        return count
