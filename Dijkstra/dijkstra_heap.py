"""
Dijkstra with a Priority Queue (heap)

The basic version is O(V^2) because finding minimum takes O(V) each time.
Using a min-heap makes it O((V+E)logV) - much faster for sparse graphs!

Python's heapq gives us a min-heap. We push (distance, node) tuples
so it always gives us the closest unvisited node.
"""

import heapq
import math


def dijkstra_fast(graph, start, end=None):
    """
    faster dijkstra using a priority queue
    optionally stop early if we only care about one destination
    """
    distances = {node: math.inf for node in graph}
    distances[start] = 0
    parents = {node: None for node in graph}

    # priority queue: (distance, node)
    # heapq is a min-heap so smallest distance comes out first
    pq = [(0, start)]

    visited = set()

    while pq:
        current_dist, current = heapq.heappop(pq)

        # skip if we already found a better path to this node
        if current in visited:
            continue

        visited.add(current)

        # early exit if we only care about getting to 'end'
        if end and current == end:
            break

        for neighbor, weight in graph[current].items():
            if neighbor in visited:
                continue

            new_dist = current_dist + weight
            if new_dist < distances[neighbor]:
                distances[neighbor] = new_dist
                parents[neighbor] = current
                heapq.heappush(pq, (new_dist, neighbor))

    return distances, parents


def reconstruct_path(parents, start, end):
    """trace back from end to start"""
    path = []
    current = end

    while current != start:
        if current is None:
            return None  # no path
        path.append(current)
        current = parents[current]

    path.append(start)
    return path[::-1]


if __name__ == "__main__":
    # bigger graph to show heap advantage
    graph = {
        'A': {'B': 4, 'C': 2},
        'B': {'A': 4, 'C': 1, 'D': 5},
        'C': {'A': 2, 'B': 1, 'D': 8, 'E': 10},
        'D': {'B': 5, 'C': 8, 'E': 2, 'F': 6},
        'E': {'C': 10, 'D': 2, 'F': 3},
        'F': {'D': 6, 'E': 3}
    }

    print("Graph:")
    for node in sorted(graph.keys()):
        print(f"  {node}: {graph[node]}")

    start, end = 'A', 'F'
    distances, parents = dijkstra_fast(graph, start, end)

    print(f"\nShortest path from {start} to {end}:")
    path = reconstruct_path(parents, start, end)
    print(f"  Path: {' -> '.join(path)}")
    print(f"  Distance: {distances[end]}")

    print("\nAll distances from A:")
    distances, _ = dijkstra_fast(graph, 'A')  # compute all
    for node in sorted(graph.keys()):
        print(f"  {start} to {node}: {distances[node]}")
