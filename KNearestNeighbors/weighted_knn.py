"""
Weighted KNN

Closer neighbors count more.
Weight = 1/distance
"""

import math


def distance(p1, p2):
    return math.sqrt(sum((a-b)**2 for a, b in zip(p1, p2)))


def weighted_knn(data, point, k):
    distances = []
    for features, value in data:
        d = distance(point, features)
        distances.append((d, value))

    distances.sort()
    k_nearest = distances[:k]

    # weighted average
    total_weight = sum(1/(d + 0.001) for d, _ in k_nearest)
    weighted_sum = sum(v/(d + 0.001) for d, v in k_nearest)

    return weighted_sum / total_weight


data = [
    ((0, 0), 10),
    ((1, 0), 20),
    ((10, 0), 100),
]

point = (0.5, 0)
print(f"Regular average: 43.3")
print(f"Weighted: {weighted_knn(data, point, 3):.1f}")
# closer points (10, 20) matter more than far (100)
