"""
Selection sort but in descending order

Same idea but find LARGEST instead of smallest
"""

def find_largest(arr):
    largest_idx = 0
    for i in range(1, len(arr)):
        if arr[i] > arr[largest_idx]:
            largest_idx = i
    return largest_idx


def selection_sort_desc(arr):
    new_arr = []
    arr_copy = list(arr)

    while arr_copy:
        largest_idx = find_largest(arr_copy)
        new_arr.append(arr_copy.pop(largest_idx))

    return new_arr


if __name__ == "__main__":
    nums = [3, 1, 4, 1, 5, 9, 2, 6]
    print(f"Original: {nums}")
    print(f"Descending: {selection_sort_desc(nums)}")
