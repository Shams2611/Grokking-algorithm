"""
Dijkstra step by step

See what happens at each iteration
"""

import math


def dijkstra_verbose(graph, start):
    costs = {node: math.inf for node in graph}
    costs[start] = 0
    visited = set()

    step = 0
    while len(visited) < len(graph):
        # find min
        node = None
        lowest = math.inf
        for n in graph:
            if n not in visited and costs[n] < lowest:
                lowest = costs[n]
                node = n

        if node is None:
            break

        step += 1
        print(f"Step {step}: visit {node} (cost {costs[node]})")
        visited.add(node)

        for neighbor, weight in graph[node].items():
            new_cost = costs[node] + weight
            if new_cost < costs[neighbor]:
                print(f"  update {neighbor}: {costs[neighbor]} -> {new_cost}")
                costs[neighbor] = new_cost

        print(f"  costs: {costs}")
        print()

    return costs


graph = {
    "A": {"B": 4, "C": 2},
    "B": {"D": 3},
    "C": {"B": 1, "D": 5},
    "D": {},
}

dijkstra_verbose(graph, "A")
