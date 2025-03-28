"""
Coin change - minimum coins needed

Classic DP problem
"""

def min_coins(amount, coins):
    # dp[i] = min coins for amount i
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0

    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i and dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1

    return dp[amount] if dp[amount] != float('inf') else -1


print(f"Amount 11, coins [1,2,5]: {min_coins(11, [1,2,5])}")
print(f"Amount 6, coins [1,3,4]: {min_coins(6, [1,3,4])}")
