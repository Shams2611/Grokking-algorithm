"""
What is a graph?

Nodes connected by edges
Like a network of friends, cities, etc.
"""

# graph as dictionary (adjacency list)
# each node points to its neighbors

friends = {
    "you": ["alice", "bob", "claire"],
    "alice": ["you", "peggy"],
    "bob": ["you", "anuj"],
    "claire": ["you", "jonny"],
    "peggy": ["alice"],
    "anuj": ["bob"],
    "jonny": ["claire"],
}

print("Your friends:", friends["you"])
print("Alice's friends:", friends["alice"])
