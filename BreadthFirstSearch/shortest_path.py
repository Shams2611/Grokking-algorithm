"""
BFS finds shortest path (by number of edges)

Track parents to reconstruct the path
"""

from collections import deque


def shortest_path(graph, start, end):
    queue = deque([start])
    parent = {start: None}

    while queue:
        node = queue.popleft()

        if node == end:
            # rebuild path
            path = []
            while node:
                path.append(node)
                node = parent[node]
            return path[::-1]

        for neighbor in graph.get(node, []):
            if neighbor not in parent:
                parent[neighbor] = node
                queue.append(neighbor)

    return None


graph = {
    "A": ["B", "C"],
    "B": ["D"],
    "C": ["D", "E"],
    "D": ["F"],
    "E": ["F"],
    "F": [],
}

path = shortest_path(graph, "A", "F")
print(f"Path: {' -> '.join(path)}")
