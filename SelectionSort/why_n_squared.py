"""
Why is selection sort O(n^2)?

n + (n-1) + (n-2) + ... + 1 = n*(n+1)/2 = roughly n^2/2

Still O(n^2) because we drop constants
"""

def selection_sort_with_count(arr):
    arr = list(arr)
    n = len(arr)
    comparisons = 0

    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            comparisons += 1
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr, comparisons


# show the math
for n in [5, 10, 20, 50]:
    arr = list(range(n, 0, -1))  # worst case
    _, comps = selection_sort_with_count(arr)
    expected = n * (n - 1) // 2
    print(f"n={n}: {comps} comparisons (formula: {expected})")
