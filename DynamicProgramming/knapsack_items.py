"""
Knapsack - get actual items taken

Backtrack through table to find which items
"""

def knapsack_with_items(items, capacity):
    n = len(items)
    table = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        _, weight, value = items[i-1]
        for w in range(capacity + 1):
            table[i][w] = table[i-1][w]
            if weight <= w:
                table[i][w] = max(table[i][w], value + table[i-1][w - weight])

    # backtrack
    taken = []
    w = capacity
    for i in range(n, 0, -1):
        if table[i][w] != table[i-1][w]:
            taken.append(items[i-1][0])
            w -= items[i-1][1]

    return table[n][capacity], taken


items = [
    ("guitar", 1, 1500),
    ("stereo", 4, 3000),
    ("laptop", 3, 2000),
]

value, taken = knapsack_with_items(items, 4)
print(f"Value: {value}")
print(f"Items: {taken}")
