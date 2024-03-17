"""
KNN for Regression - predicting numeric values

Instead of voting (classification), we AVERAGE the neighbors' values.

Example from book: predicting bakery bread sales based on:
- weather (1-5)
- is it weekend? (0/1)
- is there a game today? (0/1)

This is the same idea as classification but for continuous outputs.
"""

import math


def euclidean_distance(p1, p2):
    return math.sqrt(sum((a - b) ** 2 for a, b in zip(p1, p2)))


def knn_regression(training_data, new_point, k=3):
    """
    training_data: list of (features, value) tuples
    new_point: features we want to predict for
    k: number of neighbors
    returns: predicted value (average of k nearest)
    """
    distances = []
    for features, value in training_data:
        dist = euclidean_distance(new_point, features)
        distances.append((dist, value, features))

    distances.sort(key=lambda x: x[0])
    k_nearest = distances[:k]

    # average the values
    avg_value = sum(v for _, v, _ in k_nearest) / k

    return avg_value, k_nearest


if __name__ == "__main__":
    # bakery example
    # features: (weather, weekend, game_day)
    # value: loaves of bread sold

    bakery_data = [
        ((5, 1, 0), 300),   # nice weather, weekend, no game
        ((3, 1, 1), 225),   # ok weather, weekend, game day
        ((1, 1, 0), 75),    # bad weather, weekend
        ((4, 0, 1), 200),   # nice weather, weekday, game
        ((4, 0, 0), 150),   # nice weather, weekday
        ((2, 0, 0), 50),    # bad weather, weekday
    ]

    print("Bakery sales data:")
    print("  (weather, weekend, game) -> loaves sold")
    for features, sales in bakery_data:
        print(f"  {features} -> {sales}")

    # predict for new scenarios
    print("\n" + "="*40)
    print("Predictions:\n")

    scenarios = [
        ((5, 1, 1), "Nice weather, weekend, game day"),
        ((1, 0, 0), "Bad weather, weekday, no game"),
        ((4, 1, 0), "Nice weather, weekend, no game"),
    ]

    for features, description in scenarios:
        prediction, neighbors = knn_regression(bakery_data, features, k=2)

        print(f"{description}")
        print(f"  Features: {features}")
        print(f"  Nearest neighbors:")
        for dist, value, feat in neighbors:
            print(f"    {feat} sold {value} loaves (dist={dist:.2f})")
        print(f"  Predicted sales: {prediction:.0f} loaves\n")

    # weighted average version (closer neighbors count more)
    print("="*40)
    print("Bonus: Weighted KNN\n")

    def knn_weighted(training_data, new_point, k=3):
        """neighbors closer to the point have more influence"""
        distances = []
        for features, value in training_data:
            dist = euclidean_distance(new_point, features)
            distances.append((dist, value))

        distances.sort()
        k_nearest = distances[:k]

        # weighted average: weight = 1/distance
        # (add small value to avoid division by zero)
        total_weight = sum(1 / (d + 0.001) for d, _ in k_nearest)
        weighted_sum = sum(v / (d + 0.001) for d, v in k_nearest)

        return weighted_sum / total_weight

    test = (4, 1, 0)
    regular = knn_regression(bakery_data, test, k=3)[0]
    weighted = knn_weighted(bakery_data, test, k=3)

    print(f"For scenario {test}:")
    print(f"  Regular KNN: {regular:.0f}")
    print(f"  Weighted KNN: {weighted:.0f}")
