"""
Selection Sort - basic version that creates new array

Time: O(n^2)
Space: O(n) - creates a new list
"""

def find_smallest(arr):
    smallest_idx = 0
    for i in range(1, len(arr)):
        if arr[i] < arr[smallest_idx]:
            smallest_idx = i
    return smallest_idx


def selection_sort(arr):
    new_arr = []
    arr_copy = list(arr)  # don't modify original

    for i in range(len(arr_copy)):
        smallest_idx = find_smallest(arr_copy)
        new_arr.append(arr_copy.pop(smallest_idx))

    return new_arr


if __name__ == "__main__":
    test = [64, 25, 12, 22, 11]
    print(f"Original: {test}")
    print(f"Sorted: {selection_sort(test)}")
