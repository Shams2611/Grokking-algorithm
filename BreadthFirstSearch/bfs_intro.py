"""
Breadth-First Search (BFS) - Chapter 6

BFS answers two types of questions:
1. Is there a path from A to B?
2. What's the shortest path from A to B?

The algorithm uses a QUEUE (first in, first out - like a line at a store)
- Add starting node to queue
- Take first person from queue, check if they're what we're looking for
- If not, add all their neighbors to queue
- Repeat until found or queue is empty

Key insight: BFS checks nodes in order of distance from start
- First checks all nodes 1 step away
- Then all nodes 2 steps away
- etc.

Time: O(V + E) where V = vertices (nodes), E = edges (connections)
Space: O(V) for the queue
"""

from collections import deque

# The mango seller problem from the book
# We want to find if any of our friends (or friends of friends) sells mangoes

# graph represented as a dictionary (adjacency list)
# each person points to list of their friends
graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []


def is_mango_seller(name):
    """
    silly check from the book - mango sellers have names ending in 'm'
    in real life this would be checking a database or something
    """
    return name[-1] == 'm'


def find_mango_seller(start):
    """
    BFS to find a mango seller in our network
    returns the seller's name or None if not found
    """
    # deque is a double-ended queue, more efficient than list for this
    search_queue = deque()
    search_queue.append(start)

    # keep track of who we've already checked (avoid infinite loops!)
    searched = set()

    while search_queue:
        person = search_queue.popleft()  # get first person in queue

        # skip if already checked
        if person in searched:
            continue

        print(f"Checking {person}...")

        if is_mango_seller(person):
            print(f"  {person} is a mango seller!")
            return person

        # not a seller, add their friends to the queue
        search_queue.extend(graph[person])
        searched.add(person)

    print("No mango seller found :(")
    return None


if __name__ == "__main__":
    print("Graph structure:")
    for person, friends in graph.items():
        print(f"  {person} -> {friends}")

    print("\nSearching for mango seller starting from 'you':\n")
    seller = find_mango_seller("you")

    if seller:
        print(f"\nFound mango seller: {seller}")
