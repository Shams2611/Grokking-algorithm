"""
What is a greedy algorithm?

At each step, pick the locally optimal choice.
Hope it leads to globally optimal solution.

Sometimes it works, sometimes it doesn't!
"""

# example: making change
# greedy: always pick largest coin possible

def make_change_greedy(amount, coins):
    coins = sorted(coins, reverse=True)
    result = []

    for coin in coins:
        while amount >= coin:
            result.append(coin)
            amount -= coin

    return result


# works for US coins
print(make_change_greedy(67, [25, 10, 5, 1]))
# [25, 25, 10, 5, 1, 1]

# but not all coin systems!
# try [1, 3, 4] for amount 6
# greedy: [4, 1, 1] = 3 coins
# optimal: [3, 3] = 2 coins
