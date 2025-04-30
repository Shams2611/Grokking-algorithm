"""
Partitioning - the key step in quicksort

Pick a pivot, put smaller stuff left, bigger stuff right
"""

def partition(arr, pivot):
    less = []
    greater = []

    for x in arr:
        if x <= pivot:
            less.append(x)
        else:
            greater.append(x)

    return less, greater


arr = [3, 7, 1, 9, 2, 8]
pivot = 5

less, greater = partition(arr, pivot)
print(f"Array: {arr}")
print(f"Pivot: {pivot}")
print(f"Less than pivot: {less}")
print(f"Greater than pivot: {greater}")
