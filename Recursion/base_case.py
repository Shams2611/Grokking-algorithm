"""
Base case vs recursive case

Base case: when to stop
Recursive case: call yourself with smaller problem
"""

def factorial(n):
    # base case
    if n <= 1:
        return 1

    # recursive case
    return n * factorial(n - 1)


print(f"5! = {factorial(5)}")
# 5 * 4 * 3 * 2 * 1 = 120
