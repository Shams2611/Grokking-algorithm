"""
Binary search basics

Array must be SORTED!
Check middle, eliminate half each time.
O(log n) time.
"""

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1


nums = [1, 3, 5, 7, 9, 11, 13]
print(binary_search(nums, 7))   # 3
print(binary_search(nums, 6))   # -1
