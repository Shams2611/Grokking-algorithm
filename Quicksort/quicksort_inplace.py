"""
In-place quicksort

The simple version creates new arrays. This one sorts in place.
More memory efficient but trickier to understand.
"""

def quicksort_inplace(arr, low=0, high=None):
    if high is None:
        high = len(arr) - 1

    if low < high:
        pivot_idx = partition(arr, low, high)
        quicksort_inplace(arr, low, pivot_idx - 1)
        quicksort_inplace(arr, pivot_idx + 1, high)


def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


test = [10, 7, 8, 9, 1, 5]
print(f"Before: {test}")
quicksort_inplace(test)
print(f"After: {test}")
