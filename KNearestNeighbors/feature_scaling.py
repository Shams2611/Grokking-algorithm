"""
Feature Scaling for KNN

This is important! If features are on different scales, KNN won't work well.

Example problem:
- Feature A: age (0-100)
- Feature B: income (0-1000000)

Distance would be dominated by income since it has bigger numbers.
A person earning $50k vs $51k would seem "further" than ages 20 vs 80!

Solution: normalize features to same scale (usually 0-1)

Two common approaches:
1. Min-Max scaling: (x - min) / (max - min)  -> range [0, 1]
2. Z-score: (x - mean) / std_dev  -> mean=0, std=1
"""

import math


def min_max_normalize(data, feature_idx):
    """normalize one feature to [0, 1] range"""
    values = [point[feature_idx] for point in data]
    min_val = min(values)
    max_val = max(values)

    if max_val == min_val:
        return [0.5] * len(data)  # all same value

    return [(v - min_val) / (max_val - min_val) for v in values]


def normalize_all_features(data):
    """normalize all features in dataset"""
    if not data:
        return []

    num_features = len(data[0])
    normalized = []

    # normalize each feature
    normalized_features = []
    for i in range(num_features):
        normalized_features.append(min_max_normalize(data, i))

    # rebuild data points
    for j in range(len(data)):
        point = tuple(normalized_features[i][j] for i in range(num_features))
        normalized.append(point)

    return normalized


def euclidean_distance(p1, p2):
    return math.sqrt(sum((a - b) ** 2 for a, b in zip(p1, p2)))


if __name__ == "__main__":
    # example: predicting movie preferences
    # features: (age, salary in thousands, movies watched per month)

    raw_data = [
        (25, 40, 5),    # young, low salary, watches some movies
        (45, 80, 2),    # middle aged, higher salary, few movies
        (20, 30, 10),   # young, low salary, watches lots
        (60, 100, 1),   # older, high salary, rarely watches
        (30, 55, 8),    # young-ish, mid salary, watches often
    ]

    print("Raw data (age, salary in $k, movies/month):")
    for point in raw_data:
        print(f"  {point}")

    # show the problem with raw data
    print("\n--- Problem with unnormalized data ---")
    print("Distance between person 1 and person 2:")
    print(f"  Raw: {euclidean_distance(raw_data[0], raw_data[1]):.2f}")
    print("  (dominated by salary difference!)")

    # normalize
    normalized = normalize_all_features(raw_data)

    print("\nNormalized data:")
    for i, point in enumerate(normalized):
        print(f"  {raw_data[i]} -> ({point[0]:.2f}, {point[1]:.2f}, {point[2]:.2f})")

    print("\n--- With normalized data ---")
    print("Distance between person 1 and person 2:")
    print(f"  Normalized: {euclidean_distance(normalized[0], normalized[1]):.2f}")
    print("  (all features contribute equally now)")

    # compare all distances
    print("\n--- Distance matrix (normalized) ---")
    print("      ", end="")
    for i in range(len(normalized)):
        print(f"  P{i+1}", end="")
    print()

    for i, p1 in enumerate(normalized):
        print(f"P{i+1}  ", end="")
        for j, p2 in enumerate(normalized):
            dist = euclidean_distance(p1, p2)
            print(f" {dist:.2f}", end="")
        print()

    print("\n(Now distances reflect actual similarity, not just salary gaps)")
