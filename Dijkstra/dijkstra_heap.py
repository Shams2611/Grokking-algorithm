"""
Dijkstra with heap (priority queue)

Faster than simple version: O((V+E)logV) vs O(V^2)
"""

import heapq
import math


def dijkstra(graph, start):
    costs = {node: math.inf for node in graph}
    costs[start] = 0
    parents = {}

    # priority queue: (cost, node)
    pq = [(0, start)]
    visited = set()

    while pq:
        cost, node = heapq.heappop(pq)

        if node in visited:
            continue
        visited.add(node)

        for neighbor, weight in graph[node].items():
            new_cost = cost + weight
            if new_cost < costs[neighbor]:
                costs[neighbor] = new_cost
                parents[neighbor] = node
                heapq.heappush(pq, (new_cost, neighbor))

    return costs, parents


graph = {
    "A": {"B": 4, "C": 2},
    "B": {"C": 1, "D": 5},
    "C": {"D": 8, "E": 10},
    "D": {"E": 2},
    "E": {},
}

costs, _ = dijkstra(graph, "A")
for node, cost in sorted(costs.items()):
    print(f"A to {node}: {cost}")
