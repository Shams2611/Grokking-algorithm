"""
BFS for finding shortest path

This builds on basic BFS but now we track the actual path, not just whether
a path exists.

The trick: keep track of how we got to each node (parent pointers)
Then reconstruct path by following parents backwards
"""

from collections import deque


def bfs_shortest_path(graph, start, end):
    """
    find shortest path between start and end
    returns the path as a list, or None if no path exists
    """
    if start == end:
        return [start]

    queue = deque([start])
    visited = {start}

    # parent dict tracks how we reached each node
    # key = node, value = the node we came from
    parent = {start: None}

    while queue:
        current = queue.popleft()

        for neighbor in graph.get(current, []):
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = current
                queue.append(neighbor)

                # found it! reconstruct path
                if neighbor == end:
                    path = []
                    node = end
                    while node is not None:
                        path.append(node)
                        node = parent[node]
                    return path[::-1]  # reverse to get start->end

    return None  # no path found


def bfs_all_distances(graph, start):
    """
    find distance from start to ALL reachable nodes
    useful for understanding the BFS "levels"
    """
    queue = deque([start])
    distances = {start: 0}

    while queue:
        current = queue.popleft()
        current_dist = distances[current]

        for neighbor in graph.get(current, []):
            if neighbor not in distances:
                distances[neighbor] = current_dist + 1
                queue.append(neighbor)

    return distances


# test with a small graph
if __name__ == "__main__":
    # simple graph - like a small social network or map
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }

    print("Graph:")
    for node, neighbors in graph.items():
        print(f"  {node} -> {neighbors}")

    # find shortest paths
    print("\n--- Shortest paths from A ---")
    for target in ['B', 'C', 'D', 'E', 'F']:
        path = bfs_shortest_path(graph, 'A', target)
        print(f"A -> {target}: {' -> '.join(path)} (length: {len(path)-1})")

    # what about non-existent paths?
    graph['G'] = []  # isolated node
    path = bfs_shortest_path(graph, 'A', 'G')
    print(f"A -> G: {path}")  # should be None

    # distances from A
    print("\n--- All distances from A ---")
    distances = bfs_all_distances(graph, 'A')
    for node, dist in sorted(distances.items()):
        print(f"  A to {node}: {dist} steps")
