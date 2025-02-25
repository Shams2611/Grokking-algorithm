"""
Why O(log n)?

Each step eliminates half.
128 -> 64 -> 32 -> 16 -> 8 -> 4 -> 2 -> 1
That's log2(128) = 7 steps
"""

import math

sizes = [10, 100, 1000, 1000000]

for n in sizes:
    linear = n
    binary = int(math.log2(n)) + 1
    print(f"n={n:>10}: linear={linear:>10}, binary={binary}")
