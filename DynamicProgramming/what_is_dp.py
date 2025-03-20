"""
What is Dynamic Programming?

Break problem into subproblems.
Solve each subproblem once, store results.
Use stored results to solve bigger problem.
"""

# fibonacci - classic DP example
# without DP: exponential time
# with DP: linear time

def fib_slow(n):
    """recursive, no caching - O(2^n)"""
    if n <= 1:
        return n
    return fib_slow(n-1) + fib_slow(n-2)


def fib_dp(n):
    """with DP - O(n)"""
    if n <= 1:
        return n
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]


print(f"fib(10) = {fib_dp(10)}")
print(f"fib(30) = {fib_dp(30)}")
# try fib_slow(30) - it's SLOW
