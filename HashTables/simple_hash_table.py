"""
Building a simple hash table from scratch

Just to understand how it works internally.
Don't use this in real code - Python's dict is way better!

Basic idea:
- Array of "buckets"
- Hash function maps key to bucket index
- Handle collisions with chaining (linked lists at each bucket)
"""

class SimpleHashTable:
    def __init__(self, size=10):
        self.size = size
        # each bucket is a list (for handling collisions)
        self.buckets = [[] for _ in range(size)]

    def _hash(self, key):
        """
        super simple hash function
        just sum up character codes and mod by size
        real hash functions are way more sophisticated
        """
        total = 0
        for char in str(key):
            total += ord(char)
        return total % self.size

    def put(self, key, value):
        """add or update a key-value pair"""
        idx = self._hash(key)
        bucket = self.buckets[idx]

        # check if key exists, update if so
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return

        # key doesn't exist, add it
        bucket.append((key, value))

    def get(self, key):
        """get value by key, returns None if not found"""
        idx = self._hash(key)
        bucket = self.buckets[idx]

        for k, v in bucket:
            if k == key:
                return v

        return None

    def remove(self, key):
        """remove key-value pair"""
        idx = self._hash(key)
        bucket = self.buckets[idx]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                return True

        return False

    def __repr__(self):
        """show internal structure for debugging"""
        lines = []
        for i, bucket in enumerate(self.buckets):
            if bucket:
                lines.append(f"  [{i}]: {bucket}")
        return "HashTable:\n" + "\n".join(lines)


# let's try it
if __name__ == "__main__":
    ht = SimpleHashTable(size=5)  # small size to see collisions

    # add some data
    ht.put("apple", 1.50)
    ht.put("banana", 0.75)
    ht.put("cherry", 2.00)
    ht.put("date", 3.00)
    ht.put("elderberry", 4.50)

    print("After adding fruits:")
    print(ht)

    print(f"\nPrice of apple: ${ht.get('apple')}")
    print(f"Price of banana: ${ht.get('banana')}")
    print(f"Price of grape (not in table): {ht.get('grape')}")

    # update existing key
    ht.put("apple", 1.75)  # price went up!
    print(f"\nApple after price update: ${ht.get('apple')}")

    # remove something
    ht.remove("banana")
    print(f"Banana after removal: {ht.get('banana')}")

    # show what hash values look like
    print("\n--- Hash values for some keys ---")
    for key in ["apple", "banana", "cherry", "a", "b", "ab", "ba"]:
        print(f"  hash('{key}') = {ht._hash(key)}")
