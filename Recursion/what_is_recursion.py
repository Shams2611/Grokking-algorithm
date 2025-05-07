"""
What is recursion?

Function that calls itself.
Must have base case or infinite loop!
"""

def countdown(n):
    if n <= 0:  # base case
        print("Done!")
        return
    print(n)
    countdown(n - 1)  # recursive call


countdown(5)
