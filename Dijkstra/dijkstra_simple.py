"""
Dijkstra's algorithm - simple version

Find cheapest path in weighted graph
"""

import math


def dijkstra(graph, start):
    # track costs to reach each node
    costs = {node: math.inf for node in graph}
    costs[start] = 0

    # track path
    parents = {node: None for node in graph}

    visited = set()

    while len(visited) < len(graph):
        # find cheapest unvisited node
        node = None
        lowest = math.inf
        for n in graph:
            if n not in visited and costs[n] < lowest:
                lowest = costs[n]
                node = n

        if node is None:
            break

        visited.add(node)

        # update neighbors
        for neighbor, weight in graph[node].items():
            new_cost = costs[node] + weight
            if new_cost < costs[neighbor]:
                costs[neighbor] = new_cost
                parents[neighbor] = node

    return costs, parents


graph = {
    "start": {"a": 6, "b": 2},
    "a": {"finish": 1},
    "b": {"a": 3, "finish": 5},
    "finish": {},
}

costs, parents = dijkstra(graph, "start")
print("Costs:", costs)
print("Parents:", parents)
