"""
BFS vs DFS

BFS: level by level (uses queue)
DFS: go deep first (uses stack or recursion)
"""

from collections import deque


def bfs(graph, start):
    visited = []
    queue = deque([start])
    seen = {start}

    while queue:
        node = queue.popleft()
        visited.append(node)
        for n in graph.get(node, []):
            if n not in seen:
                seen.add(n)
                queue.append(n)
    return visited


def dfs(graph, start):
    visited = []
    stack = [start]
    seen = {start}

    while stack:
        node = stack.pop()  # pop from end = stack
        visited.append(node)
        for n in graph.get(node, []):
            if n not in seen:
                seen.add(n)
                stack.append(n)
    return visited


graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": [],
    "F": [],
}

print("BFS:", bfs(graph, "A"))
print("DFS:", dfs(graph, "A"))
