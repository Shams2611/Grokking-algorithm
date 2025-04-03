"""
NP-Complete problems

No known fast solution. Greedy gives approximation.

Examples:
- Traveling salesman
- Set covering
- Knapsack (0/1)
"""

# traveling salesman - visit all cities once, minimize distance
# greedy: always go to nearest unvisited city

def tsp_greedy(distances, start):
    n = len(distances)
    visited = [False] * n
    path = [start]
    visited[start] = True
    current = start
    total = 0

    for _ in range(n - 1):
        nearest = None
        min_dist = float('inf')

        for city in range(n):
            if not visited[city] and distances[current][city] < min_dist:
                min_dist = distances[current][city]
                nearest = city

        visited[nearest] = True
        path.append(nearest)
        total += min_dist
        current = nearest

    # return to start
    total += distances[current][start]
    path.append(start)

    return path, total


# distance matrix
dist = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0],
]

path, cost = tsp_greedy(dist, 0)
print(f"Path: {path}")
print(f"Cost: {cost}")
print("(might not be optimal)")
