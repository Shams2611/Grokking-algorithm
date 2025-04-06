"""
Huffman coding intro

Greedy algorithm for compression.
More frequent chars get shorter codes.
"""

# basic idea - frequency determines code length
text = "aaaaaabbbccd"

# count frequency
freq = {}
for c in text:
    freq[c] = freq.get(c, 0) + 1

print("Frequencies:", freq)

# simple greedy: shorter codes for frequent chars
# a: very common -> short code like "0"
# b: common -> medium code like "10"
# c: less common -> longer code like "110"
# d: rare -> longest code like "111"

# this is just the intuition
# real huffman builds a tree
print("\nIntuition:")
print("a (6x) -> 0")
print("b (3x) -> 10")
print("c (2x) -> 110")
print("d (1x) -> 111")
