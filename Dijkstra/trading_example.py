"""
Trading example from the book

Find cheapest way to trade items
"""

import heapq
import math


def find_cheapest(graph, start, end):
    costs = {node: math.inf for node in graph}
    costs[start] = 0
    parents = {start: None}
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

    # get path
    path = []
    node = end
    while node:
        path.append(node)
        node = parents.get(node)
    return costs[end], path[::-1]


# book -> poster -> guitar -> piano
trades = {
    "book": {"poster": 0, "record": 5},
    "poster": {"guitar": 30, "drums": 35},
    "record": {"guitar": 15, "drums": 20},
    "guitar": {"piano": 20},
    "drums": {"piano": 10},
    "piano": {},
}

cost, path = find_cheapest(trades, "book", "piano")
print(f"Cheapest path: {' -> '.join(path)}")
print(f"Total cost: ${cost}")
