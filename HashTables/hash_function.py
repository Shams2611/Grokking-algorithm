"""
How hash functions work (simplified)

Key -> hash function -> index in array
"""


def simple_hash(key, array_size):
    """sum of character codes mod array size"""
    total = 0
    for char in str(key):
        total += ord(char)
    return total % array_size


# same key always gives same hash
print(simple_hash("apple", 10))
print(simple_hash("apple", 10))  # same!

# different keys can give same hash (collision)
print(simple_hash("ab", 10))
print(simple_hash("ba", 10))  # same hash!
