"""
Manhattan distance

Alternative to Euclidean.
Sum of absolute differences.
Like walking on a grid (city blocks).
"""


def manhattan(p1, p2):
    return sum(abs(a - b) for a, b in zip(p1, p2))


def euclidean(p1, p2):
    return sum((a - b) ** 2 for a, b in zip(p1, p2)) ** 0.5


a = (0, 0)
b = (3, 4)

print(f"Euclidean: {euclidean(a, b)}")  # 5
print(f"Manhattan: {manhattan(a, b)}")  # 7

# manhattan good when features are independent
# euclidean good when relationship matters
