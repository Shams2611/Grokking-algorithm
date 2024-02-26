"""
Countdown - Basic Recursion Example

This demonstrates the two essential parts of any recursive function:
1. Base case: When the function stops calling itself
2. Recursive case: When the function calls itself

Time Complexity: O(n) - where n is the starting number
Space Complexity: O(n) - due to call stack depth
"""


def countdown(i):
    """
    Recursively counts down from i to 1.

    Args:
        i: The number to start counting down from

    Returns:
        None (prints each number)
    """
    print(i)

    if i <= 1:      # Base case - stop recursion
        return
    else:           # Recursive case - call itself with smaller input
        countdown(i - 1)


# Example usage
if __name__ == "__main__":
    print("Counting down from 5:")
    countdown(5)
    # Output: 5, 4, 3, 2, 1
