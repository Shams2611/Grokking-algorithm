"""
Dijkstra's Algorithm - Chapter 7

BFS finds shortest path by NUMBER of edges.
Dijkstra finds shortest path by WEIGHT (like distance, time, cost).

When to use what:
- Unweighted graph -> BFS
- Weighted graph (no negative weights!) -> Dijkstra
- Negative weights -> Bellman-Ford (not covered in book)

The algorithm:
1. Start at source node
2. Find the unvisited node with smallest known distance
3. Update distances to its neighbors (if we found a shorter path)
4. Mark current node as visited
5. Repeat until all nodes visited or target found

Time: O(V^2) simple version, O((V+E)logV) with priority queue
Space: O(V)

IMPORTANT: doesn't work with negative edge weights!
"""

import math


def dijkstra(graph, start):
    """
    graph format: {node: {neighbor: weight, neighbor2: weight2, ...}}
    returns: (distances dict, parents dict)
    """
    # initialize distances - infinity for all except start
    distances = {node: math.inf for node in graph}
    distances[start] = 0

    # track the path (who did we come from to reach each node)
    parents = {node: None for node in graph}

    # nodes we haven't processed yet
    unvisited = set(graph.keys())

    while unvisited:
        # find unvisited node with smallest distance
        current = None
        current_dist = math.inf
        for node in unvisited:
            if distances[node] < current_dist:
                current = node
                current_dist = distances[node]

        # if smallest is infinity, remaining nodes are unreachable
        if current is None or current_dist == math.inf:
            break

        unvisited.remove(current)

        # update distances to neighbors
        for neighbor, weight in graph[current].items():
            new_dist = distances[current] + weight
            if new_dist < distances[neighbor]:
                distances[neighbor] = new_dist
                parents[neighbor] = current

    return distances, parents


def get_path(parents, start, end):
    """reconstruct path from start to end using parent pointers"""
    if parents.get(end) is None and start != end:
        return None  # no path

    path = []
    current = end
    while current is not None:
        path.append(current)
        current = parents[current]

    return path[::-1]


if __name__ == "__main__":
    # Example from the book - trading piano for something else
    # node = what you have, edges = trades you can make with costs

    graph = {
        'start': {'a': 6, 'b': 2},
        'a': {'finish': 1},
        'b': {'a': 3, 'finish': 5},
        'finish': {}
    }

    print("Graph (trading network):")
    for node, edges in graph.items():
        print(f"  {node}: {edges}")

    distances, parents = dijkstra(graph, 'start')

    print("\nShortest distances from 'start':")
    for node, dist in distances.items():
        print(f"  to {node}: {dist}")

    path = get_path(parents, 'start', 'finish')
    print(f"\nShortest path to finish: {' -> '.join(path)}")
    print(f"Total cost: {distances['finish']}")

    # another example - city distances
    print("\n" + "="*50)
    print("Another example - city map:\n")

    cities = {
        'home': {'school': 10, 'mall': 15},
        'school': {'home': 10, 'library': 5, 'park': 12},
        'mall': {'home': 15, 'park': 8},
        'library': {'school': 5, 'gym': 3},
        'park': {'school': 12, 'mall': 8, 'gym': 7},
        'gym': {'library': 3, 'park': 7}
    }

    distances, parents = dijkstra(cities, 'home')

    print("From home to all locations:")
    for city, dist in sorted(distances.items(), key=lambda x: x[1]):
        path = get_path(parents, 'home', city)
        path_str = ' -> '.join(path) if path else "N/A"
        print(f"  {city}: {dist} min ({path_str})")
