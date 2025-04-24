"""
Cosine similarity

Measures angle between vectors.
Good for comparing documents or ratings.
"""

import math


def cosine_sim(a, b):
    dot = sum(x * y for x, y in zip(a, b))
    mag_a = math.sqrt(sum(x**2 for x in a))
    mag_b = math.sqrt(sum(x**2 for x in b))

    if mag_a == 0 or mag_b == 0:
        return 0

    return dot / (mag_a * mag_b)


# movie ratings: [comedy, action, romance]
alice = [5, 1, 4]
bob = [4, 2, 5]
carol = [1, 5, 1]

print(f"Alice-Bob: {cosine_sim(alice, bob):.3f}")   # similar
print(f"Alice-Carol: {cosine_sim(alice, carol):.3f}")  # different
