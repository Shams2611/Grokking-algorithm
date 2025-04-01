"""
Fractional knapsack

Can take parts of items (like gold dust).
Greedy works here! Pick by value/weight ratio.
"""

def fractional_knapsack(items, capacity):
    # sort by value per weight
    items = sorted(items, key=lambda x: x[2]/x[1], reverse=True)

    total = 0
    taken = []

    for name, weight, value in items:
        if capacity >= weight:
            taken.append((name, 1.0))
            capacity -= weight
            total += value
        elif capacity > 0:
            frac = capacity / weight
            taken.append((name, frac))
            total += value * frac
            capacity = 0

    return total, taken


items = [
    ("gold", 10, 500),
    ("silver", 20, 400),
    ("bronze", 30, 300),
]

value, taken = fractional_knapsack(items, 25)
print(f"Value: {value}")
print(f"Taken: {taken}")
