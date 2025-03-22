"""
Tabulation - bottom-up DP

Build solution iteratively.
Fill table from smallest subproblems up.
"""

def fib_table(n):
    if n <= 1:
        return n

    # build table bottom-up
    table = [0] * (n + 1)
    table[1] = 1

    for i in range(2, n + 1):
        table[i] = table[i-1] + table[i-2]

    return table[n]


# can optimize space - only need last 2 values
def fib_optimized(n):
    if n <= 1:
        return n

    prev2, prev1 = 0, 1
    for _ in range(2, n + 1):
        curr = prev1 + prev2
        prev2, prev1 = prev1, curr

    return prev1


print(f"fib(100) = {fib_table(100)}")
print(f"fib(100) = {fib_optimized(100)}")
