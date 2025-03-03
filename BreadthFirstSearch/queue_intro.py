"""
Queue - FIFO (First In First Out)

Like a line at a store. First person in line gets served first.
BFS uses a queue to track who to check next.
"""

from collections import deque

# deque is more efficient than list for queues
queue = deque()

# add to back
queue.append("first")
queue.append("second")
queue.append("third")

print("Queue:", list(queue))

# remove from front
print("Pop:", queue.popleft())
print("Pop:", queue.popleft())
print("Remaining:", list(queue))
