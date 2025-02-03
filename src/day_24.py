from itertools import combinations, pairwise, permutations


class Day24:
    def __init__(self, lines: list[str]):
        self.map = {}
        self.nodes = dict()
        self.max_y = len(lines)
        self.max_x = len(lines[0])
        for y, line in enumerate(lines):
            for x, char in enumerate(line):
                self.map[(x,y)] = {"wall": True} if char == "#" else {"wall": False}
                if char not in ["#", "."]:
                    self.nodes[char] = (x,y)

    def find_path(self, start, end):
        for value in self.map.values():
            value["dist"] = float("inf")
            value["prev"] = None
        queue = [start]
        self.map[start]["dist"] = 0
        while len(queue) > 0:
            n = queue.pop(0)
            # Check valid neighbours, within borders, not walls
            for x, y in [(n[0]+1, n[1]), (n[0]-1, n[1]), (n[0], n[1]+1), (n[0], n[1]-1)]:
                if 0<=x<=self.max_x and 0<=y<=self.max_y and not self.map[(x,y)]["wall"]:
                    # Possibly decrease neighbour distance to prev + 1, mark prev node and add to queue
                    if self.map[(x, y)]['dist'] > self.map[n]['dist'] + 1:
                        self.map[(x, y)]['dist'] = self.map[n]['dist'] + 1
                        self.map[(x, y)]['prev'] = n
                        queue.append((x, y))
                    # If we reached the end, traceback from end to start
                    if (x, y) == end:
                        path = [(x, y)]
                        while self.map[path[-1]]['prev'] is not None:
                            path.append(self.map[path[-1]]['prev'])
                        return path[-1::-1] # Return reverse, start to end of path

    def solve1(self) -> int:
        keys = self.nodes.keys()
        distances = {}
        for p in combinations(keys, 2):
            path = self.find_path(self.nodes[p[0]], self.nodes[p[1]])
            distances[p] = len(path)
            distances[(p[1], p[0])] = len(path)
        result = 1_000_000_000
        for perm in permutations(keys):
            if (perm[0] != "0"):
                continue
            distance = 0
            for pair in pairwise(perm):
                distance += distances[pair] - 1
            result = min(distance, result)
        return result

    def solve2(self) -> int:
        return 2
