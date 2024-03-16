"""
K-Nearest Neighbors (KNN) - Chapter 10

KNN is beautifully simple:
"Tell me who your neighbors are, and I'll tell you who you are"

For classification:
1. Calculate distance from new point to all known points
2. Find K nearest neighbors
3. Majority vote - whatever class most neighbors have, that's your prediction

For regression:
Same idea but average the values instead of voting.

Key decisions:
- K value: too small = noisy, too large = ignores local patterns
  (often use sqrt(n) or just try different values)
- Distance metric: usually Euclidean, but Manhattan or others work too

Time: O(n) to classify one point (have to check all training points)
      - can use KD-trees to speed this up
"""

import math
from collections import Counter


def euclidean_distance(point1, point2):
    """
    distance = sqrt((x1-x2)^2 + (y1-y2)^2 + ...)
    works for any number of dimensions
    """
    total = 0
    for a, b in zip(point1, point2):
        total += (a - b) ** 2
    return math.sqrt(total)


def knn_classify(training_data, new_point, k=3):
    """
    training_data: list of (features, label) tuples
                   features is a tuple/list of numeric values
    new_point: features of the point we want to classify
    k: number of neighbors to consider
    """
    # calculate distances to all training points
    distances = []
    for features, label in training_data:
        dist = euclidean_distance(new_point, features)
        distances.append((dist, label))

    # sort by distance and get k closest
    distances.sort(key=lambda x: x[0])
    k_nearest = distances[:k]

    print(f"  {k} nearest neighbors:")
    for dist, label in k_nearest:
        print(f"    distance={dist:.2f}, class={label}")

    # count votes
    labels = [label for _, label in k_nearest]
    vote_count = Counter(labels)

    winner = vote_count.most_common(1)[0][0]
    return winner


if __name__ == "__main__":
    # movie recommendation example (simplified from book)
    # features: (action_rating, romance_rating)
    # label: movie genre

    movies = [
        ((5, 1), "Action"),      # high action, low romance
        ((4, 1), "Action"),
        ((5, 2), "Action"),
        ((1, 5), "Romance"),     # low action, high romance
        ((2, 5), "Romance"),
        ((1, 4), "Romance"),
        ((3, 3), "Comedy"),      # middle ground
        ((3, 4), "Comedy"),
    ]

    print("Training data (movies):")
    print("  (action, romance) -> genre")
    for features, label in movies:
        print(f"  {features} -> {label}")

    # classify some new movies
    print("\n" + "="*40)
    print("Classifying new movies:\n")

    new_movies = [
        (5, 1),   # probably action
        (1, 5),   # probably romance
        (3, 3),   # probably comedy
        (4, 3),   # hmm, could be action or comedy
    ]

    for movie in new_movies:
        print(f"New movie with ratings {movie}:")
        prediction = knn_classify(movies, movie, k=3)
        print(f"  Predicted genre: {prediction}\n")

    # show effect of different k values
    print("="*40)
    print("Effect of different K values:\n")

    test_movie = (4, 3)
    print(f"Test movie: {test_movie}")
    for k in [1, 3, 5]:
        print(f"\nK = {k}:")
        result = knn_classify(movies, test_movie, k=k)
        print(f"  Prediction: {result}")
