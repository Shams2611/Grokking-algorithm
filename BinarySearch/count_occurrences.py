"""
Count occurrences using binary search

Find first and last, subtract
"""

def count(arr, target):
    def find_first():
        low, high = 0, len(arr) - 1
        result = -1
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] == target:
                result = mid
                high = mid - 1
            elif arr[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return result

    def find_last():
        low, high = 0, len(arr) - 1
        result = -1
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] == target:
                result = mid
                low = mid + 1
            elif arr[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return result

    first = find_first()
    if first == -1:
        return 0
    return find_last() - first + 1


nums = [1, 2, 2, 2, 2, 3, 4]
print(f"Count of 2: {count(nums, 2)}")  # 4
