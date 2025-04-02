"""
0/1 Knapsack - greedy doesn't work!

Must take whole item or nothing.
Greedy gives approximation, not optimal.
"""

def knapsack_greedy(items, capacity):
    # sort by ratio
    items = sorted(items, key=lambda x: x[2]/x[1], reverse=True)

    total = 0
    taken = []
    weight = 0

    for name, w, v in items:
        if weight + w <= capacity:
            taken.append(name)
            weight += w
            total += v

    return total, taken


items = [
    ("item1", 10, 60),
    ("item2", 20, 100),
    ("item3", 30, 120),
]

value, taken = knapsack_greedy(items, 50)
print(f"Greedy: {taken}, value={value}")
# might not be optimal! need DP for that
