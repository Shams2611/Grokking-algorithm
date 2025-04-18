"""
K-Nearest Neighbors

Simple idea: you are what your neighbors are.
Find K closest points, majority vote.
"""

# example: is fruit an orange or grapefruit?
# features: size and color (redness)

fruits = [
    (4, 3, "orange"),
    (4, 2, "orange"),
    (5, 4, "grapefruit"),
    (6, 4, "grapefruit"),
]

new_fruit = (4.5, 3)  # what is this?
# find nearest neighbors and vote!

print("Training data:")
for f in fruits:
    print(f"  size={f[0]}, color={f[1]} -> {f[2]}")

print(f"\nNew fruit: size={new_fruit[0]}, color={new_fruit[1]}")
print("Prediction: probably orange (closer to oranges)")
