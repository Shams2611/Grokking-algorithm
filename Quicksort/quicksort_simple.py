"""
Quicksort - simple version

Pick pivot, partition, recursively sort both sides
"""

def quicksort(arr):
    if len(arr) < 2:
        return arr

    pivot = arr[0]
    less = [x for x in arr[1:] if x <= pivot]
    greater = [x for x in arr[1:] if x > pivot]

    return quicksort(less) + [pivot] + quicksort(greater)


test = [10, 5, 2, 3]
print(f"Original: {test}")
print(f"Sorted: {quicksort(test)}")
