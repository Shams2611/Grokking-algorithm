"""
Reconstruct path from Dijkstra result

Follow parents backwards from end to start
"""


def get_path(parents, start, end):
    path = []
    node = end

    while node != start:
        path.append(node)
        node = parents[node]
        if node is None:
            return None  # no path

    path.append(start)
    return path[::-1]


# example parents dict from dijkstra
parents = {
    "start": None,
    "a": "b",
    "b": "start",
    "finish": "a",
}

path = get_path(parents, "start", "finish")
print(" -> ".join(path))
