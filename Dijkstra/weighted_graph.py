"""
Weighted graphs

Edges have costs (distance, time, money, etc.)
BFS doesn't work here - need Dijkstra!
"""

# weighted graph - dict of dicts
# graph[node][neighbor] = weight

graph = {
    "start": {"a": 6, "b": 2},
    "a": {"finish": 1},
    "b": {"a": 3, "finish": 5},
    "finish": {},
}

print("start to a costs:", graph["start"]["a"])
print("start to b costs:", graph["start"]["b"])
print("neighbors of start:", list(graph["start"].keys()))
