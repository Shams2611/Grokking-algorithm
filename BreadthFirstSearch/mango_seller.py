"""
Finding a mango seller - example from the book

Search your network for someone who sells mangoes
"""

from collections import deque

graph = {
    "you": ["alice", "bob", "claire"],
    "bob": ["anuj", "peggy"],
    "alice": ["peggy"],
    "claire": ["thom", "jonny"],
    "anuj": [],
    "peggy": [],
    "thom": [],
    "jonny": [],
}


def is_seller(name):
    # silly rule: sellers have names ending in 'm'
    return name[-1] == 'm'


def find_seller(start):
    queue = deque([start])
    checked = set()

    while queue:
        person = queue.popleft()
        if person in checked:
            continue

        if is_seller(person):
            return person

        queue.extend(graph[person])
        checked.add(person)

    return None


seller = find_seller("you")
print(f"Found seller: {seller}")
