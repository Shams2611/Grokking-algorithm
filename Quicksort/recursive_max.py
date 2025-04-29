"""
Find max recursively

Compare first element with max of the rest
"""

def find_max(arr):
    if len(arr) == 1:
        return arr[0]

    max_of_rest = find_max(arr[1:])

    if arr[0] > max_of_rest:
        return arr[0]
    else:
        return max_of_rest


print(find_max([1, 5, 3, 9, 2]))  # 9
print(find_max([7]))  # 7
print(find_max([-1, -5, -2]))  # -1
