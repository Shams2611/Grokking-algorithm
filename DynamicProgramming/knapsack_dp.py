"""
0/1 Knapsack using Dynamic Programming - Chapter 9

This is the REAL solution to knapsack (greedy was just an approximation).

Key idea: build a table where cell[i][w] = max value using first i items
with capacity w.

For each item, we decide: take it or leave it?
- If we leave it: value = cell[i-1][w] (same as without this item)
- If we take it: value = item_value + cell[i-1][w - item_weight]
  (value of item + best we can do with remaining space)

We pick whichever is better.

Time: O(n * W) where n = num items, W = capacity
Space: O(n * W) for the table (can be optimized to O(W))

This is called "pseudo-polynomial" - polynomial in W but W could be huge!
"""

def knapsack_dp(items, capacity):
    """
    items: list of (name, weight, value)
    capacity: max weight
    returns: (max_value, list of items to take)
    """
    n = len(items)

    # create table - rows are items, columns are capacities 0 to capacity
    # table[i][w] = max value using items 0..i-1 with capacity w
    table = [[0] * (capacity + 1) for _ in range(n + 1)]

    # fill the table
    for i in range(1, n + 1):
        name, weight, value = items[i - 1]

        for w in range(capacity + 1):
            # option 1: don't take item i
            dont_take = table[i - 1][w]

            # option 2: take item i (if it fits)
            if weight <= w:
                take = value + table[i - 1][w - weight]
            else:
                take = 0

            # pick better option
            table[i][w] = max(dont_take, take)

    # backtrack to find which items we took
    taken = []
    w = capacity
    for i in range(n, 0, -1):
        if table[i][w] != table[i - 1][w]:
            # we took this item
            taken.append(items[i - 1][0])
            w -= items[i - 1][1]

    return table[n][capacity], taken, table


def print_table(table, items, capacity):
    """helper to visualize the DP table"""
    print("\nDP Table:")
    print("       ", end="")
    for w in range(capacity + 1):
        print(f"{w:4}", end="")
    print()
    print("       " + "----" * (capacity + 1))

    for i, row in enumerate(table):
        if i == 0:
            label = "empty"
        else:
            label = items[i-1][0][:5]
        print(f"{label:6}|", end="")
        for val in row:
            print(f"{val:4}", end="")
        print()


if __name__ == "__main__":
    # classic example
    items = [
        ("guitar", 1, 1500),
        ("stereo", 4, 3000),
        ("laptop", 3, 2000),
    ]
    capacity = 4

    print("Items:")
    for name, w, v in items:
        print(f"  {name}: {w}lb, ${v}")
    print(f"Backpack capacity: {capacity}lb")

    max_val, taken, table = knapsack_dp(items, capacity)

    print_table(table, items, capacity)

    print(f"\nMax value: ${max_val}")
    print(f"Items to take: {taken}")

    # verify
    total_weight = sum(items[i][1] for i in range(len(items)) if items[i][0] in taken)
    print(f"Total weight: {total_weight}lb")

    print("\n" + "="*50)
    print("Another example with more items:\n")

    items2 = [
        ("phone", 1, 500),
        ("tablet", 2, 800),
        ("camera", 3, 1200),
        ("laptop", 4, 1500),
    ]
    capacity2 = 5

    max_val2, taken2, _ = knapsack_dp(items2, capacity2)
    print(f"Max value: ${max_val2}")
    print(f"Items: {taken2}")
