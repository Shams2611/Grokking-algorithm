"""
Quicksort - Chapter 4

This is a divide-and-conquer algorithm. The trick is picking a "pivot" and then
partitioning: put smaller stuff on left, bigger stuff on right.

How it works:
1. Pick a pivot (any element, I'm using the first one here)
2. Partition array into: [elements < pivot] + [pivot] + [elements > pivot]
3. Recursively quicksort the left and right parts
4. Base case: arrays with 0 or 1 elements are already sorted

Time complexity:
- Average case: O(n log n) - this is why it's called "quick"!
- Worst case: O(n^2) - happens when pivot is always smallest/largest (like already sorted array)

Space: O(log n) for the call stack

Note: this is the simple/readable version, not the most efficient
"""

def quicksort(arr):
    # base case - nothing to sort
    if len(arr) < 2:
        return arr

    # pick pivot - just using first element
    # (could pick random or median for better performance)
    pivot = arr[0]

    # partition into less than and greater than
    less = [x for x in arr[1:] if x <= pivot]
    greater = [x for x in arr[1:] if x > pivot]

    # recursively sort and combine
    return quicksort(less) + [pivot] + quicksort(greater)


def quicksort_verbose(arr, depth=0):
    """same thing but prints what's happening - helpful for understanding"""
    indent = "  " * depth
    print(f"{indent}quicksort({arr})")

    if len(arr) < 2:
        print(f"{indent}-> base case, returning {arr}")
        return arr

    pivot = arr[0]
    less = [x for x in arr[1:] if x <= pivot]
    greater = [x for x in arr[1:] if x > pivot]

    print(f"{indent}pivot={pivot}, less={less}, greater={greater}")

    result = quicksort_verbose(less, depth + 1) + [pivot] + quicksort_verbose(greater, depth + 1)
    print(f"{indent}-> returning {result}")
    return result


if __name__ == "__main__":
    # basic test
    test = [10, 5, 2, 3]
    print(f"Original: {test}")
    print(f"Sorted: {quicksort(test)}")

    print("\n" + "="*50)
    print("Let's see what's happening step by step:\n")

    small_test = [3, 1, 4, 1, 5]
    result = quicksort_verbose(small_test)
    print(f"\nFinal result: {result}")

    # more tests
    print("\n" + "="*50)
    print("More test cases:")
    print(f"Empty: {quicksort([])}")
    print(f"Single: {quicksort([1])}")
    print(f"Two elements: {quicksort([2, 1])}")
    print(f"Duplicates: {quicksort([3, 3, 3, 1, 1])}")
    print(f"Negative nums: {quicksort([-5, 3, -1, 0, 2])}")
