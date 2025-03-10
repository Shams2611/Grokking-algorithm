"""
BFS by levels

Sometimes you want to process level by level
"""

from collections import deque


def bfs_levels(graph, start):
    levels = []
    queue = deque([start])
    seen = {start}

    while queue:
        level_size = len(queue)
        current_level = []

        for _ in range(level_size):
            node = queue.popleft()
            current_level.append(node)

            for neighbor in graph.get(node, []):
                if neighbor not in seen:
                    seen.add(neighbor)
                    queue.append(neighbor)

        levels.append(current_level)

    return levels


graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": [],
    "F": [],
}

for i, level in enumerate(bfs_levels(graph, "A")):
    print(f"Level {i}: {level}")
