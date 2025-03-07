"""
Find distance from start to all nodes

BFS naturally finds shortest distances
"""

from collections import deque


def distances(graph, start):
    dist = {start: 0}
    queue = deque([start])

    while queue:
        node = queue.popleft()

        for neighbor in graph.get(node, []):
            if neighbor not in dist:
                dist[neighbor] = dist[node] + 1
                queue.append(neighbor)

    return dist


graph = {
    "A": ["B", "C"],
    "B": ["D"],
    "C": ["D", "E"],
    "D": ["F"],
    "E": [],
    "F": [],
}

result = distances(graph, "A")
for node, d in sorted(result.items()):
    print(f"A -> {node}: {d} steps")
