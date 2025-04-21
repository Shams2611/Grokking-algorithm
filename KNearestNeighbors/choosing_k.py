"""
Choosing K value

Too small: noisy, overfitting
Too large: ignores local patterns

Common choice: sqrt(n)
"""

import math

n = 100  # training samples
k = int(math.sqrt(n))
print(f"For n={n}, try k={k}")

# or just try different values
# and see which works best!

# odd k avoids ties in classification
print("\nTip: use odd k to avoid ties")
print("k=3, k=5, k=7 are common choices")
