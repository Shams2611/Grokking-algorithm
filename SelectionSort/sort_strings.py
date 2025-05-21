"""
Selection sort works on strings too!

Python compares strings alphabetically by default
"""

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


names = ["charlie", "alice", "bob", "diana"]
print(f"Before: {names}")
print(f"After: {selection_sort(names)}")

fruits = ["banana", "Apple", "cherry", "apricot"]
print(f"\nFruits: {fruits}")
print(f"Sorted: {selection_sort(fruits)}")
print("(Note: uppercase comes before lowercase in ASCII)")
