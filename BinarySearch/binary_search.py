"""
Binary Search Algorithm

Binary search is an efficient algorithm for finding an item in a SORTED list.
It works by repeatedly dividing the search interval in half.

How it works:
1. Start with the middle element
2. If target equals middle, we're done!
3. If target < middle, search the left half
4. If target > middle, search the right half
5. Repeat until found or search space is empty

Time Complexity: O(log n) - halves the search space each step
Space Complexity: O(1) - iterative version uses constant space

Comparison with Linear Search:
- Linear search: O(n) - checks every element
- Binary search: O(log n) - much faster for large lists
- For a list of 1,000,000 items:
  - Linear search: up to 1,000,000 steps
  - Binary search: up to 20 steps!

Requirement: The list MUST be sorted!
"""


def binary_search(sorted_list, target):
    """
    Search for a target value in a sorted list using binary search.

    Args:
        sorted_list: A list sorted in ascending order
        target: The value to search for

    Returns:
        The index of the target if found, None otherwise
    """
    low = 0
    high = len(sorted_list) - 1

    while low <= high:
        mid = (low + high) // 2  # Find the middle index
        guess = sorted_list[mid]

        if guess == target:
            return mid          # Found it!
        elif guess > target:
            high = mid - 1      # Target is in the left half
        else:
            low = mid + 1       # Target is in the right half

    return None  # Target not found


# Example usage
if __name__ == "__main__":
    # Binary search requires a SORTED list
    my_list = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

    print("List:", my_list)
    print()

    # Search for existing element
    result = binary_search(my_list, 7)
    print(f"Searching for 7: found at index {result}")  # Output: 3

    # Search for another element
    result = binary_search(my_list, 15)
    print(f"Searching for 15: found at index {result}")  # Output: 7

    # Search for non-existing element
    result = binary_search(my_list, 8)
    print(f"Searching for 8: {result}")  # Output: None

    print()
    print("--- Step-by-step example searching for 7 ---")
    print("List: [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]")
    print("Step 1: low=0, high=9, mid=4, guess=9 (too high)")
    print("Step 2: low=0, high=3, mid=1, guess=3 (too low)")
    print("Step 3: low=2, high=3, mid=2, guess=5 (too low)")
    print("Step 4: low=3, high=3, mid=3, guess=7 (found!)")
