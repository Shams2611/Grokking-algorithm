"""
KNN Classification

Vote among K nearest neighbors
"""

import math
from collections import Counter


def distance(p1, p2):
    return math.sqrt(sum((a-b)**2 for a, b in zip(p1, p2)))


def knn_classify(data, point, k):
    # data = list of (features, label)
    distances = []
    for features, label in data:
        d = distance(point, features)
        distances.append((d, label))

    distances.sort()
    k_nearest = [label for _, label in distances[:k]]

    # vote
    votes = Counter(k_nearest)
    return votes.most_common(1)[0][0]


# movie preferences
movies = [
    ((5, 1), "action"),
    ((4, 1), "action"),
    ((1, 5), "romance"),
    ((2, 4), "romance"),
]

new = (4, 2)
print(f"New point {new}: {knn_classify(movies, new, k=3)}")
