"""
Find last occurrence

When there are duplicates
"""

def find_last(arr, target):
    low, high = 0, len(arr) - 1
    result = -1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            result = mid
            low = mid + 1  # keep looking right
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return result


nums = [1, 2, 2, 2, 3, 4]
print(find_last(nums, 2))  # 3 (last 2)
