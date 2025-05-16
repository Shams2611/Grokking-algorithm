"""
Counting swaps in selection sort

Selection sort does at most n-1 swaps (one per pass)
This is actually good compared to bubble sort!
"""

def selection_sort_count_swaps(arr):
    arr = list(arr)
    n = len(arr)
    swaps = 0

    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j

        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            swaps += 1

    return arr, swaps


# test different cases
cases = [
    [5, 4, 3, 2, 1],  # reverse sorted
    [1, 2, 3, 4, 5],  # already sorted
    [3, 1, 4, 1, 5],  # random
]

for case in cases:
    _, swaps = selection_sort_count_swaps(case)
    print(f"{case} -> {swaps} swaps")
