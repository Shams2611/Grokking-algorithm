"""
Sum array recursively

Base: empty array = 0
Recursive: first + sum of rest
"""

def rec_sum(arr):
    if len(arr) == 0:
        return 0
    return arr[0] + rec_sum(arr[1:])


print(rec_sum([1, 2, 3, 4, 5]))  # 15
