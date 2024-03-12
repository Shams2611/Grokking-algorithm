"""
Knapsack Problem - Greedy vs Dynamic Programming

The greedy approach works for FRACTIONAL knapsack but NOT for 0/1 knapsack!

Fractional knapsack: You can take part of an item (like gold dust)
0/1 knapsack: Either take whole item or don't (like a laptop)

This file shows the greedy approach which is:
- Pick items with best value/weight ratio first
- Works perfectly for fractional, gives approximation for 0/1
"""

def knapsack_greedy_fractional(items, capacity):
    """
    items: list of (name, weight, value)
    returns: list of (name, fraction taken)
    """
    # sort by value per weight (descending)
    sorted_items = sorted(items, key=lambda x: x[2]/x[1], reverse=True)

    total_value = 0
    taken = []
    remaining = capacity

    for name, weight, value in sorted_items:
        if remaining <= 0:
            break

        ratio = value / weight
        print(f"{name}: weight={weight}, value={value}, ratio={ratio:.2f}")

        if weight <= remaining:
            # take whole item
            taken.append((name, 1.0))
            remaining -= weight
            total_value += value
            print(f"  -> took all of it, remaining capacity: {remaining}")
        else:
            # take fraction
            fraction = remaining / weight
            taken.append((name, fraction))
            total_value += value * fraction
            print(f"  -> took {fraction:.2%} of it")
            remaining = 0

    return taken, total_value


def knapsack_greedy_01(items, capacity):
    """
    0/1 knapsack using greedy - NOT optimal but quick
    shows why greedy doesn't always work for this problem
    """
    sorted_items = sorted(items, key=lambda x: x[2]/x[1], reverse=True)

    total_value = 0
    total_weight = 0
    taken = []

    for name, weight, value in sorted_items:
        if total_weight + weight <= capacity:
            taken.append(name)
            total_weight += weight
            total_value += value

    return taken, total_value, total_weight


if __name__ == "__main__":
    # item format: (name, weight, value)
    items = [
        ("laptop", 3, 2000),
        ("headphones", 1, 300),
        ("coffee mug", 1, 20),
        ("book", 2, 500),
        ("water bottle", 2, 30),
    ]

    capacity = 5

    print("Items available:")
    for name, w, v in items:
        print(f"  {name}: {w}kg, ${v}, ratio=${v/w:.0f}/kg")
    print(f"\nBackpack capacity: {capacity}kg")

    print("\n--- Fractional Knapsack (greedy works!) ---\n")
    taken, value = knapsack_greedy_fractional(items, capacity)
    print(f"\nTaken: {taken}")
    print(f"Total value: ${value:.2f}")

    print("\n--- 0/1 Knapsack (greedy approximation) ---\n")
    taken, value, weight = knapsack_greedy_01(items, capacity)
    print(f"Taken: {taken}")
    print(f"Total weight: {weight}kg")
    print(f"Total value: ${value}")
    print("\n(Note: this might not be optimal - need DP for that)")
