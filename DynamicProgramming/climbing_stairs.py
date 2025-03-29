"""
Climbing stairs

Can take 1 or 2 steps. How many ways to reach top?
Basically fibonacci!
"""

def climb_stairs(n):
    if n <= 2:
        return n

    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 2

    for i in range(3, n + 1):
        dp[i] = dp[i-1] + dp[i-2]

    return dp[n]


for n in range(1, 8):
    print(f"{n} stairs: {climb_stairs(n)} ways")
