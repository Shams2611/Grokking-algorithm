"""
Using infinity for unknown costs

Start with infinity, update when we find a path
"""

import math

# math.inf is infinity in python
print(5 < math.inf)   # True
print(math.inf + 1)   # still inf

# float('inf') also works
print(float('inf') == math.inf)  # True

# useful for dijkstra initialization
costs = {"a": 0, "b": math.inf, "c": math.inf}

# update when we find path
if 5 < costs["b"]:
    costs["b"] = 5

print(costs)
