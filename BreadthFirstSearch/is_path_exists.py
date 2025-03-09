"""
Simple question: does a path exist?

Sometimes you just need yes/no, not the actual path
"""

from collections import deque


def path_exists(graph, start, end):
    if start == end:
        return True

    queue = deque([start])
    seen = {start}

    while queue:
        node = queue.popleft()

        for neighbor in graph.get(node, []):
            if neighbor == end:
                return True
            if neighbor not in seen:
                seen.add(neighbor)
                queue.append(neighbor)

    return False


graph = {
    "A": ["B", "C"],
    "B": ["D"],
    "C": [],
    "D": [],
    "E": ["F"],  # separate component
    "F": [],
}

print(f"A to D: {path_exists(graph, 'A', 'D')}")  # True
print(f"A to E: {path_exists(graph, 'A', 'E')}")  # False - not connected
