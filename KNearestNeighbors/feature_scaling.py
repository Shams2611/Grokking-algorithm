"""
Feature scaling

If features have different scales, big ones dominate!
Normalize to same range.
"""

def normalize(data):
    """scale all features to 0-1"""
    if not data:
        return []

    n_features = len(data[0])
    mins = [min(d[i] for d in data) for i in range(n_features)]
    maxs = [max(d[i] for d in data) for i in range(n_features)]

    result = []
    for point in data:
        normalized = []
        for i in range(n_features):
            if maxs[i] == mins[i]:
                normalized.append(0.5)
            else:
                normalized.append((point[i] - mins[i]) / (maxs[i] - mins[i]))
        result.append(tuple(normalized))

    return result


# age and salary - very different scales
data = [
    (25, 50000),
    (45, 80000),
    (35, 60000),
]

print("Before:", data)
print("After:", normalize(data))
