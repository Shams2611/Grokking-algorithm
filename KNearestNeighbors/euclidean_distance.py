"""
Euclidean distance

How far apart are two points?
sqrt((x1-x2)^2 + (y1-y2)^2)
"""

import math


def distance(p1, p2):
    total = 0
    for a, b in zip(p1, p2):
        total += (a - b) ** 2
    return math.sqrt(total)


# 2D example
a = (1, 1)
b = (4, 5)
print(f"Distance {a} to {b}: {distance(a, b):.2f}")

# 3D example
c = (0, 0, 0)
d = (1, 1, 1)
print(f"Distance {c} to {d}: {distance(c, d):.2f}")
