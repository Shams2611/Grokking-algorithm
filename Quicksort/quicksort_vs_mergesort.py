"""
Quicksort vs Mergesort

Both are O(n log n) average
Quicksort: faster in practice, O(n^2) worst case
Mergesort: always O(n log n), needs extra space
"""

import time
import random


def quicksort(arr):
    if len(arr) < 2:
        return arr
    pivot = arr[len(arr) // 2]
    less = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    greater = [x for x in arr if x > pivot]
    return quicksort(less) + equal + quicksort(greater)


def mergesort(arr):
    if len(arr) < 2:
        return arr
    mid = len(arr) // 2
    left = mergesort(arr[:mid])
    right = mergesort(arr[mid:])
    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


# compare
data = [random.randint(1, 1000) for _ in range(1000)]

start = time.time()
quicksort(data.copy())
qs_time = time.time() - start

start = time.time()
mergesort(data.copy())
ms_time = time.time() - start

print(f"Quicksort: {qs_time:.4f}s")
print(f"Mergesort: {ms_time:.4f}s")
