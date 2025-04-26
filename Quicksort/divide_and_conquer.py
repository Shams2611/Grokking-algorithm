"""
Divide and Conquer intro

D&C is a strategy:
1. Figure out base case (simplest possible)
2. Divide problem until it becomes base case

Quicksort uses this approach!
"""

# simple example: sum an array using D&C
def dc_sum(arr):
    if len(arr) == 0:  # base case
        return 0
    return arr[0] + dc_sum(arr[1:])  # divide


nums = [1, 2, 3, 4]
print(f"Sum of {nums} = {dc_sum(nums)}")
