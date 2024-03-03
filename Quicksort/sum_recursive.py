"""
Recursive Sum - also from Chapter 4

This shows the D&C (divide and conquer) approach for summing a list.

The idea:
- Base case: empty list -> sum is 0
- Recursive case: first element + sum of the rest

Honestly for real code you'd just use sum() but this helps understand recursion
"""

def recursive_sum(arr):
    if len(arr) == 0:
        return 0
    return arr[0] + recursive_sum(arr[1:])


def recursive_sum_v2(arr):
    """alternative version using conditional expression"""
    return 0 if not arr else arr[0] + recursive_sum_v2(arr[1:])


def count_items(arr):
    """count items in list recursively - same pattern"""
    if arr == []:
        return 0
    return 1 + count_items(arr[1:])


def find_max(arr):
    """
    find max element recursively
    this one's a bit trickier - compare first with max of rest
    """
    # base cases
    if len(arr) == 0:
        return None  # or could raise error
    if len(arr) == 1:
        return arr[0]

    # recursive case
    max_of_rest = find_max(arr[1:])
    return arr[0] if arr[0] > max_of_rest else max_of_rest


# let's test
if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5]

    print(f"List: {numbers}")
    print(f"Sum: {recursive_sum(numbers)}")
    print(f"Sum v2: {recursive_sum_v2(numbers)}")
    print(f"Count: {count_items(numbers)}")
    print(f"Max: {find_max(numbers)}")

    # edge cases
    print(f"\nEmpty list sum: {recursive_sum([])}")
    print(f"Single item sum: {recursive_sum([42])}")
    print(f"Empty list max: {find_max([])}")
    print(f"Negative numbers max: {find_max([-5, -2, -10, -1])}")
