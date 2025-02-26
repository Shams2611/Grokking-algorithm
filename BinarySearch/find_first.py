"""
Find first occurrence

When there are duplicates
"""

def find_first(arr, target):
    low, high = 0, len(arr) - 1
    result = -1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            result = mid
            high = mid - 1  # keep looking left
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return result


nums = [1, 2, 2, 2, 3, 4]
print(find_first(nums, 2))  # 1 (first 2)
