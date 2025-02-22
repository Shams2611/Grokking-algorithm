"""
KNN Regression

Average neighbors instead of voting.
Predict numeric values.
"""

import math


def distance(p1, p2):
    return math.sqrt(sum((a-b)**2 for a, b in zip(p1, p2)))


def knn_regression(data, point, k):
    # data = list of (features, value)
    distances = []
    for features, value in data:
        d = distance(point, features)
        distances.append((d, value))

    distances.sort()
    k_nearest = [value for _, value in distances[:k]]

    return sum(k_nearest) / k


# predict bread sales
sales = [
    ((5, 1), 300),  # weather, weekend -> sales
    ((3, 1), 225),
    ((1, 1), 75),
    ((4, 0), 150),
]

new_day = (4, 1)
pred = knn_regression(sales, new_day, k=2)
print(f"Predicted sales: {pred}")
