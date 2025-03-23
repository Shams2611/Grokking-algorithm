"""
Knapsack with DP table

Build grid: rows = items, cols = capacities
Each cell = best value for that subproblem
"""

def knapsack(items, capacity):
    n = len(items)
    # table[i][w] = best value with first i items, capacity w
    table = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        name, weight, value = items[i-1]
        for w in range(capacity + 1):
            # don't take item i
            table[i][w] = table[i-1][w]
            # take item i if it fits
            if weight <= w:
                take = value + table[i-1][w - weight]
                table[i][w] = max(table[i][w], take)

    return table[n][capacity]


items = [
    ("guitar", 1, 1500),
    ("stereo", 4, 3000),
    ("laptop", 3, 2000),
]

print(f"Max value: {knapsack(items, 4)}")
