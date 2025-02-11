# How to Use Breadth-First Search (BFS)

To solve [2016, Day 22](https://adventofcode.com/2016/day/22), an important technique was used: breadth-first search, or simply BFS. In my experience, it is more error-prone to implement than depth-first search (DFS). So let's go through the basics of it.

## Initialization

BFS requires a queue to manage the order in which nodes are explored. Typically, the queue is initialized with the starting node, and a set is used to keep track of visited nodes to prevent redundant processing.

Example initialization:

```python
from collections import deque

queue = deque([start_node])  # Initialize queue with the start node
visited = set([start_node])  # Track visited nodes
```

The nodes can also be set with a value that changes as we traverse to minimize the path, we can also keep track of the path itself...

```python
for value in nodes.values():
    value["dist"] = float("inf")
    value["prev"] = None
queue = [start]
```

## Feeding Next Iteration

In each iteration, we dequeue a node, process it, and enqueue its unvisited neighbors. This ensures that nodes are explored layer by layer, maintaining the shortest-path property in an unweighted graph.

Example of expanding nodes:

```python
while queue:
    node = queue.popleft()  # Dequeue the next node
    for neighbor in get_neighbors(node):  # Retrieve adjacent nodes
        if neighbor not in visited:
            visited.add(neighbor)  # Mark as visited
            queue.append(neighbor)  # Enqueue for next exploration
```

For the other given example, we have to update the values if the node is eligible to be part of a minimal path:


```python
if nodes[neighbour]["dist"] > nodes[current]["dist"] + 1:
    nodes[neighbour]["dist"] = self.nodes[current]["dist"] + 1
    nodes[neighbour]["prev"] = current
    queue.append(neighbour)
```

## Stop Condition

BFS typically stops when either:

The queue is empty, meaning all reachable nodes have been explored.

A specific target node is found (in cases like shortest-path problems).

Example of an early exit condition:

```python
while queue:
    node = queue.popleft()
    if node == target:
        print("Target found!")
        break
```

We can also use some information that we updated as the nodes were traversed (e.g. `value["prev"]`) to output the entire path from start to target.

BFS is a powerful algorithm, particularly useful for finding shortest paths in unweighted graphs and for exploring all possible states in problem-solving scenarios like Advent of Code challenges. Understanding its initialization, iteration, and termination conditions helps in implementing it efficiently and correctly.
