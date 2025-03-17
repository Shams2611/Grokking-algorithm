"""
City map example

Find shortest drive between locations
"""

import heapq


def shortest_route(roads, start, end):
    costs = {loc: float('inf') for loc in roads}
    costs[start] = 0
    pq = [(0, start)]
    visited = set()

    while pq:
        cost, loc = heapq.heappop(pq)
        if loc in visited:
            continue
        if loc == end:
            return cost
        visited.add(loc)

        for neighbor, dist in roads[loc].items():
            new_cost = cost + dist
            if new_cost < costs[neighbor]:
                costs[neighbor] = new_cost
                heapq.heappush(pq, (new_cost, neighbor))

    return None


roads = {
    "home": {"school": 10, "mall": 15, "gym": 25},
    "school": {"home": 10, "library": 5},
    "mall": {"home": 15, "park": 8},
    "library": {"school": 5, "gym": 3},
    "park": {"mall": 8, "gym": 7},
    "gym": {"home": 25, "library": 3, "park": 7},
}

dist = shortest_route(roads, "home", "gym")
print(f"Shortest route home to gym: {dist} min")
