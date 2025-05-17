"""
Finding the smallest element - the core of selection sort

This is step 1 of selection sort: scan through array to find minimum
"""

def find_smallest(arr):
    smallest = arr[0]
    smallest_idx = 0

    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_idx = i

    return smallest_idx


# test it
if __name__ == "__main__":
    nums = [5, 3, 8, 1, 9, 2]
    idx = find_smallest(nums)
    print(f"Array: {nums}")
    print(f"Smallest element: {nums[idx]} at index {idx}")
