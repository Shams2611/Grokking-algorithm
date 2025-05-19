"""
Selection Sort - in-place version

More memory efficient - sorts the array directly without creating new one

Time: O(n^2)
Space: O(1)
"""

def selection_sort_inplace(arr):
    n = len(arr)

    for i in range(n):
        # find min in remaining unsorted part
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j

        # swap
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr


if __name__ == "__main__":
    test = [5, 3, 6, 2, 10]
    print(f"Before: {test}")
    selection_sort_inplace(test)
    print(f"After: {test}")
