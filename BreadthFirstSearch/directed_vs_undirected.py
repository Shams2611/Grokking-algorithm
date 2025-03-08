"""
Directed vs Undirected graphs

Directed: A->B doesn't mean B->A (like Twitter follow)
Undirected: A-B means both ways (like Facebook friend)
"""

# directed - you follow them, they don't follow you back
twitter = {
    "you": ["celebrity", "friend"],
    "friend": ["you"],
    "celebrity": [],  # doesn't follow anyone
}

# undirected - need to add both directions
def add_edge(graph, a, b):
    if a not in graph:
        graph[a] = []
    if b not in graph:
        graph[b] = []
    graph[a].append(b)
    graph[b].append(a)


facebook = {}
add_edge(facebook, "you", "alice")
add_edge(facebook, "you", "bob")
add_edge(facebook, "alice", "bob")

print("Twitter (directed):", twitter)
print("Facebook (undirected):", facebook)
