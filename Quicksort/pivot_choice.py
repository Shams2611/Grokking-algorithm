"""
Pivot choice matters!

Bad pivot = O(n^2)
Good pivot = O(n log n)

Random pivot is usually safe
"""

import random


def quicksort_first_pivot(arr):
    """always uses first element - can be slow on sorted arrays"""
    if len(arr) < 2:
        return arr
    pivot = arr[0]
    less = [x for x in arr[1:] if x <= pivot]
    greater = [x for x in arr[1:] if x > pivot]
    return quicksort_first_pivot(less) + [pivot] + quicksort_first_pivot(greater)


def quicksort_random_pivot(arr):
    """random pivot - avoids worst case"""
    if len(arr) < 2:
        return arr
    pivot_idx = random.randint(0, len(arr) - 1)
    pivot = arr[pivot_idx]
    rest = arr[:pivot_idx] + arr[pivot_idx + 1:]
    less = [x for x in rest if x <= pivot]
    greater = [x for x in rest if x > pivot]
    return quicksort_random_pivot(less) + [pivot] + quicksort_random_pivot(greater)


# both work but random is safer
test = [5, 4, 3, 2, 1]
print(f"First pivot: {quicksort_first_pivot(test)}")
print(f"Random pivot: {quicksort_random_pivot(test)}")
