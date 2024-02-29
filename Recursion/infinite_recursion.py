"""
Infinite Recursion - What Happens Without a Base Case

This demonstrates the WRONG way to write a recursive function.
Without a base case, the function calls itself forever until
Python raises a RecursionError (stack overflow).

WARNING: Running this code will crash with RecursionError!

Time Complexity: N/A (never terminates)
Space Complexity: N/A (grows until stack overflow)
"""


def countdown(i):
    """
    BAD EXAMPLE: Countdown without a base case.

    This function has no stopping condition, so it will
    call itself infinitely: 3 -> 2 -> 1 -> 0 -> -1 -> -2 -> ...

    Args:
        i: The number to start from

    Returns:
        Never returns - causes stack overflow
    """
    print(i)
    countdown(i - 1)  # No base case! This never stops.


# Example usage (commented out to prevent crash)
if __name__ == "__main__":
    print("This would print: 3...2...1...0...-1...-2... until crash")
    print("Uncomment the line below to see the RecursionError:")
    # countdown(3)  # WARNING: This will crash!
