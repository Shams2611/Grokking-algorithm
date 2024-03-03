"""
Binary Search - Recursive Implementation

This is the recursive version of binary search. Instead of using a while loop,
the function calls itself with a smaller search range each time.

Time Complexity: O(log n) - same as iterative
Space Complexity: O(log n) - due to recursive call stack

Note: The iterative version is generally preferred in practice because:
- It uses O(1) space instead of O(log n)
- No risk of stack overflow for very large lists
- Slightly faster (no function call overhead)

But the recursive version is elegant and helps understand recursion!
"""


def binary_search_recursive(sorted_list, target, low=None, high=None):
    """
    Search for a target value using recursive binary search.

    Args:
        sorted_list: A list sorted in ascending order
        target: The value to search for
        low: Start index of search range (default: 0)
        high: End index of search range (default: len-1)

    Returns:
        The index of the target if found, None otherwise
    """
    # Initialize low and high on first call
    if low is None:
        low = 0
    if high is None:
        high = len(sorted_list) - 1

    # Base case: search space is empty
    if low > high:
        return None

    mid = (low + high) // 2
    guess = sorted_list[mid]

    # Base case: found the target
    if guess == target:
        return mid
    # Recursive case: search left half
    elif guess > target:
        return binary_search_recursive(sorted_list, target, low, mid - 1)
    # Recursive case: search right half
    else:
        return binary_search_recursive(sorted_list, target, mid + 1, high)


# Example usage
if __name__ == "__main__":
    my_list = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

    print("List:", my_list)
    print()

    # Search for existing element
    result = binary_search_recursive(my_list, 7)
    print(f"Searching for 7: found at index {result}")

    # Search for another element
    result = binary_search_recursive(my_list, 15)
    print(f"Searching for 15: found at index {result}")

    # Search for non-existing element
    result = binary_search_recursive(my_list, 8)
    print(f"Searching for 8: {result}")

    print()
    print("--- Recursive call trace for searching 7 ---")
    print("Call 1: binary_search([...], 7, low=0, high=9)")
    print("        mid=4, guess=9 > 7, go left")
    print("Call 2: binary_search([...], 7, low=0, high=3)")
    print("        mid=1, guess=3 < 7, go right")
    print("Call 3: binary_search([...], 7, low=2, high=3)")
    print("        mid=2, guess=5 < 7, go right")
    print("Call 4: binary_search([...], 7, low=3, high=3)")
    print("        mid=3, guess=7 == 7, FOUND!")
