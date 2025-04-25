"""
Simple movie recommender

Find users similar to you.
Recommend what they liked.
"""

import math


def similarity(a, b):
    # use euclidean distance
    return 1 / (1 + math.sqrt(sum((x-y)**2 for x, y in zip(a, b))))


# ratings: [comedy, action, drama]
users = {
    "alice": [5, 1, 3],
    "bob": [4, 2, 4],
    "carol": [1, 5, 2],
    "dave": [2, 4, 1],
}

me = [5, 2, 3]

# find most similar user
best = None
best_sim = 0
for name, ratings in users.items():
    sim = similarity(me, ratings)
    print(f"{name}: {sim:.3f}")
    if sim > best_sim:
        best_sim = sim
        best = name

print(f"\nMost similar: {name}")
print("Recommend what they like!")
