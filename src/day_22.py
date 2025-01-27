from re import search


class Day22:
    def __init__(self, volumes: list[str]):
        self.nodes = {}
        self.max_x = 0
        self.max_y = 0
        for v in volumes[2:]:
            r = search(r"/dev/grid/node-x(\d+)-y(\d+)\s+\d+T\s+(\d+)T\s+(\d+)T", v)
            x, y, u, a = map(int, r.groups() if r is not None else "break it")
            self.max_x = max(self.max_x, x)
            self.max_y = max(self.max_y, y)
            self.nodes[(x,y)] = {"used": u, "avail": a}
            if u == 0:
                self.empty = (x,y)

    def solve1(self) -> int:
        count = 0
        for a in self.nodes:
            for b in self.nodes:
                if a != b and self.nodes[a]["used"] > 0 and self.nodes[a]["used"] <= self.nodes[b]["avail"]:
                    count += 1
        return count

    def find_path(self, start, end, obstacle = None):
        for value in self.nodes.values():
            value["dist"] = float("inf")
            value["prev"] = None
        queue = [start]
        self.nodes[start]["dist"] = 0
        while len(queue) > 0:
            n = queue.pop(0)
            # Check valid neighbours, within borders, not too used and not an obstacle
            for x, y in [(n[0]+1, n[1]), (n[0]-1, n[1]), (n[0], n[1]+1), (n[0], n[1]-1)]:
                if 0<=x<=self.max_x and 0<=y<=self.max_y and self.nodes[(x,y)]['used'] < 100 and (x, y) != obstacle:
                    # Possibly decrease neighbour distance to prev + 1, mark prev node and add to queue
                    if self.nodes[(x, y)]['dist'] > self.nodes[n]['dist'] + 1:
                        self.nodes[(x, y)]['dist'] = self.nodes[n]['dist'] + 1
                        self.nodes[(x, y)]['prev'] = n
                        queue.append((x, y))
                    # If we reached the end, traceback from end to start
                    if (x, y) == end:
                        path = [(x, y)]
                        while self.nodes[path[-1]]['prev'] is not None:
                            path.append(self.nodes[path[-1]]['prev'])
                        return path[-2::-1] # Return reverse, going to the end, don't include start

    def solve2(self) -> int:
        # We make a path as direct as possible from start to goal that avoids largely used nodes
        start = (0,0)
        goal = (self.max_x, 0)
        path_towards_goal = self.find_path(goal, start)
        # Our original target is an empty node
        target = self.empty
        count = 0
        while goal != start:
            # We keep making a path from the empty node to the next node in the path from start to goal
            path_towards_target = self.find_path(target, path_towards_goal.pop(0), obstacle = goal)
            count += len(path_towards_target) + 1
            target = goal
            goal = path_towards_target[-1]
        return count
