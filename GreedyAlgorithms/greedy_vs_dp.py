"""
When to use greedy vs DP

Greedy: fast, simple, not always optimal
DP: slower, always optimal, more complex
"""

# coin change - compare approaches
def greedy_coins(amount, coins):
    coins = sorted(coins, reverse=True)
    result = []
    for c in coins:
        while amount >= c:
            result.append(c)
            amount -= c
    return result if amount == 0 else None


def dp_coins(amount, coins):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0

    for i in range(1, amount + 1):
        for c in coins:
            if c <= i and dp[i - c] + 1 < dp[i]:
                dp[i] = dp[i - c] + 1

    return dp[amount] if dp[amount] != float('inf') else None


# standard coins - greedy works
coins1 = [25, 10, 5, 1]
print(f"Standard coins, amount=67:")
print(f"  Greedy: {greedy_coins(67, coins1)}")
print(f"  DP: {dp_coins(67, coins1)} coins")

# weird coins - greedy fails
coins2 = [1, 3, 4]
print(f"\nWeird coins [1,3,4], amount=6:")
print(f"  Greedy: {greedy_coins(6, coins2)} = {len(greedy_coins(6, coins2))} coins")
print(f"  DP: {dp_coins(6, coins2)} coins (optimal: [3,3])")
