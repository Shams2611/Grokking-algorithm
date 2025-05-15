"""
Comparing selection sort with Python's built-in sort

Spoiler: built-in is way faster (it uses Timsort - O(n log n))
"""

import time
import random


def selection_sort(arr):
    arr = list(arr)
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


# benchmark
sizes = [100, 500, 1000]

for size in sizes:
    data = [random.randint(1, 1000) for _ in range(size)]

    # selection sort
    start = time.time()
    selection_sort(data.copy())
    sel_time = time.time() - start

    # built-in
    start = time.time()
    sorted(data.copy())
    builtin_time = time.time() - start

    print(f"n={size}:")
    print(f"  Selection sort: {sel_time:.4f}s")
    print(f"  Built-in sort:  {builtin_time:.6f}s")
    print(f"  Ratio: {sel_time/builtin_time:.0f}x slower")
    print()
