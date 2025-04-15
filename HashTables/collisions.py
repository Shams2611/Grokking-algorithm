"""
Collisions: when two keys hash to same slot

Solutions:
1. Chaining - linked list at each slot
2. Open addressing - find next empty slot
"""

# Python handles this automatically but here's the concept

class SimpleHashChaining:
    def __init__(self, size=5):
        self.size = size
        self.buckets = [[] for _ in range(size)]

    def _hash(self, key):
        return sum(ord(c) for c in str(key)) % self.size

    def put(self, key, value):
        idx = self._hash(key)
        # check if key exists
        for i, (k, v) in enumerate(self.buckets[idx]):
            if k == key:
                self.buckets[idx][i] = (key, value)
                return
        self.buckets[idx].append((key, value))

    def get(self, key):
        idx = self._hash(key)
        for k, v in self.buckets[idx]:
            if k == key:
                return v
        return None


ht = SimpleHashChaining(size=3)
ht.put("a", 1)
ht.put("b", 2)
ht.put("c", 3)  # might collide

print(ht.get("a"))
print(ht.get("b"))
print(ht.buckets)  # see the chains
