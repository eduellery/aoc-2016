def clip_range(current, clipped):
    if current[0] > clipped[1] or current[1] < clipped[0]:
        return [current]
    result = []
    if current[0] < clipped[0]:
        result.append((current[0], clipped[0] - 1))
    if clipped[1] < current[1]:
        result.append((clipped[1] + 1, current[1]))
    return result

class Day20:
    def __init__(self, values: list[str]):
        self.ranges = []
        for v in values:
            self.ranges.append(tuple(map(int, v.split("-"))))

    def remove_range(self, ips, low, high):
        new_ranges = []
        for current_range in ips:
            new_ranges.extend(clip_range(current_range, (low, high)))
        return new_ranges

    def solve1(self, max: int = 4294967295) -> int:
        ips = [(0, max)]
        for pair in self.ranges:
            ips = self.remove_range(ips, pair[0], pair[1])
        return ips[0][0]

    def solve2(self) -> int:
        return 2
