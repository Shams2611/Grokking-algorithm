"""
Selection Sort - Chapter 2

The idea: find the smallest element, put it first. Then find the next smallest, put it second. Repeat.

It's like sorting a hand of cards - you look through all cards to find the lowest, move it to the left,
then find the next lowest from what's remaining, etc.

Time: O(n^2) - gotta check n elements, then n-1, then n-2... which is n*n/2 basically
Space: O(1) - we sort in place, no extra arrays needed
"""

def find_smallest(arr):
    """finds index of smallest element in array"""
    smallest = arr[0]
    smallest_idx = 0

    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_idx = i

    return smallest_idx


def selection_sort(arr):
    """
    sorts array using selection sort
    returns new sorted array (doesn't modify original)
    """
    new_arr = []
    # make a copy so we don't mess up the original
    arr_copy = list(arr)

    for i in range(len(arr_copy)):
        smallest_idx = find_smallest(arr_copy)
        new_arr.append(arr_copy.pop(smallest_idx))

    return new_arr


def selection_sort_inplace(arr):
    """
    in-place version - modifies the original array
    more memory efficient since we don't create a new list
    """
    n = len(arr)

    for i in range(n):
        # find minimum in remaining unsorted part
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j

        # swap current position with the minimum
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr


# testing it out
if __name__ == "__main__":
    my_list = [64, 25, 12, 22, 11]
    print(f"Original: {my_list}")
    print(f"Sorted: {selection_sort(my_list)}")

    # test in-place version
    another_list = [5, 3, 6, 2, 10]
    print(f"\nBefore in-place sort: {another_list}")
    selection_sort_inplace(another_list)
    print(f"After in-place sort: {another_list}")

    # edge cases
    print(f"\nEmpty list: {selection_sort([])}")
    print(f"Single element: {selection_sort([42])}")
    print(f"Already sorted: {selection_sort([1, 2, 3, 4, 5])}")
