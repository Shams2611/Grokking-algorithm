"""
Simple (linear) search

Check every element. O(n) time.
"""

def simple_search(arr, target):
    for i, item in enumerate(arr):
        if item == target:
            return i
    return -1


nums = [1, 3, 5, 7, 9, 11]
print(simple_search(nums, 7))   # 3
print(simple_search(nums, 6))   # -1
