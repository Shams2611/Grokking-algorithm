"""
Why BFS doesn't work for weighted graphs

BFS finds fewest edges, not lowest cost
"""

# example where BFS gives wrong answer
graph = {
    "A": {"B": 1, "C": 10},
    "B": {"C": 1},
    "C": {},
}

# BFS would say A->C (1 edge) is shortest
# But A->B->C (cost 2) is cheaper than A->C (cost 10)!

print("A->C direct: cost 10")
print("A->B->C: cost 1+1 = 2")
print("BFS would pick wrong path!")
