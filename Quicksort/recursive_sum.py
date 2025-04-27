"""
Recursive sum - D&C example

Base case: empty list = 0
Recursive: first + sum of rest
"""

def rec_sum(arr):
    if len(arr) == 0:
        return 0
    return arr[0] + rec_sum(arr[1:])


print(rec_sum([1, 2, 3, 4]))  # 10
print(rec_sum([]))  # 0
print(rec_sum([5]))  # 5
