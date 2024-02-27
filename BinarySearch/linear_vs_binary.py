"""
Linear Search vs Binary Search Comparison

This demonstrates why binary search is so much faster than linear search
for large datasets.

Linear Search:
- Checks each element one by one
- Time Complexity: O(n)
- Works on unsorted lists

Binary Search:
- Divides search space in half each step
- Time Complexity: O(log n)
- Requires sorted list

The difference is HUGE for large lists!
"""

import time


def linear_search(my_list, target):
    """
    Search by checking each element one by one.

    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    for i, item in enumerate(my_list):
        if item == target:
            return i
    return None


def binary_search(sorted_list, target):
    """
    Search by dividing the search space in half.

    Time Complexity: O(log n)
    Space Complexity: O(1)
    """
    low = 0
    high = len(sorted_list) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = sorted_list[mid]

        if guess == target:
            return mid
        elif guess > target:
            high = mid - 1
        else:
            low = mid + 1

    return None


def count_steps_linear(my_list, target):
    """Count how many comparisons linear search makes."""
    steps = 0
    for item in my_list:
        steps += 1
        if item == target:
            return steps
    return steps


def count_steps_binary(sorted_list, target):
    """Count how many comparisons binary search makes."""
    low = 0
    high = len(sorted_list) - 1
    steps = 0

    while low <= high:
        steps += 1
        mid = (low + high) // 2
        guess = sorted_list[mid]

        if guess == target:
            return steps
        elif guess > target:
            high = mid - 1
        else:
            low = mid + 1

    return steps


# Example usage
if __name__ == "__main__":
    import math

    print("=" * 60)
    print("LINEAR SEARCH vs BINARY SEARCH COMPARISON")
    print("=" * 60)

    # Test with different list sizes
    sizes = [10, 100, 1000, 10000, 100000, 1000000]

    print()
    print(f"{'List Size':<12} {'Linear (worst)':<16} {'Binary (worst)':<16} {'Speedup'}")
    print("-" * 60)

    for size in sizes:
        linear_worst = size                    # O(n)
        binary_worst = math.ceil(math.log2(size))  # O(log n)
        speedup = linear_worst / binary_worst

        print(f"{size:<12} {linear_worst:<16} {binary_worst:<16} {speedup:.0f}x faster")

    print()
    print("=" * 60)
    print("PRACTICAL EXAMPLE")
    print("=" * 60)

    # Create a sorted list
    test_list = list(range(1, 100001))  # 1 to 100,000
    target = 73456  # Searching for this number

    print(f"\nSearching for {target} in a list of {len(test_list)} numbers...")
    print()

    # Count steps
    linear_steps = count_steps_linear(test_list, target)
    binary_steps = count_steps_binary(test_list, target)

    print(f"Linear search: {linear_steps:,} steps")
    print(f"Binary search: {binary_steps} steps")
    print(f"Binary search is {linear_steps // binary_steps}x faster!")

    print()
    print("=" * 60)
    print("KEY TAKEAWAY")
    print("=" * 60)
    print("""
    If you're searching through 4 billion items:
    - Linear search: up to 4,000,000,000 steps
    - Binary search: up to 32 steps!

    That's the power of O(log n) vs O(n)!

    BUT REMEMBER: Binary search only works on SORTED data.
    """)
