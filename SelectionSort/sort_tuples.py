"""
Sorting tuples by specific element

Like sorting students by grade or age
"""

def selection_sort_by_key(arr, key_idx):
    """sort list of tuples by element at key_idx"""
    arr = list(arr)
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j][key_idx] < arr[min_idx][key_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


# students: (name, age, grade)
students = [
    ("Alice", 20, 85),
    ("Bob", 19, 92),
    ("Charlie", 21, 78),
    ("Diana", 19, 95),
]

print("Original:", students)
print("\nBy age:", selection_sort_by_key(students, 1))
print("\nBy grade:", selection_sort_by_key(students, 2))
