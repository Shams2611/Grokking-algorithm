"""
Hash tables have O(1) lookup!

Compare to list which is O(n)
"""

import time

# big list vs big dict
size = 100000
my_list = list(range(size))
my_dict = {i: True for i in range(size)}

# search for last element
target = size - 1

# list search - O(n)
start = time.time()
found = target in my_list
list_time = time.time() - start

# dict search - O(1)
start = time.time()
found = target in my_dict
dict_time = time.time() - start

print(f"List lookup: {list_time:.6f}s")
print(f"Dict lookup: {dict_time:.6f}s")
print(f"Dict is ~{list_time/dict_time:.0f}x faster!")
