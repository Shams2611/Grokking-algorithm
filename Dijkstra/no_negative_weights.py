"""
Dijkstra doesn't work with negative weights!

Once we visit a node, we assume we found the best path.
Negative weights can make this wrong.
"""

# example where dijkstra fails
graph = {
    "A": {"B": 5, "C": 2},
    "B": {"C": -10},  # negative!
    "C": {},
}

# dijkstra would visit C first (cost 2)
# but A->B->C has cost 5 + (-10) = -5 which is cheaper!

print("A->C direct: 2")
print("A->B->C: 5 + (-10) = -5")
print("Dijkstra picks 2, but -5 is actually cheaper!")
print("\nUse Bellman-Ford for negative weights")
