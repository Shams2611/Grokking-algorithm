"""
Count items recursively

Another D&C example
"""

def count(arr):
    if arr == []:
        return 0
    return 1 + count(arr[1:])


print(count([1, 2, 3, 4, 5]))  # 5
print(count([]))  # 0
print(count(["a", "b"]))  # 2
