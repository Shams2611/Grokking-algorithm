"""
Counting word frequency

Classic hash table use case
"""

text = "the cat sat on the mat and the cat was happy"

word_count = {}

for word in text.split():
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print(word_count)

# simpler way with get()
word_count2 = {}
for word in text.split():
    word_count2[word] = word_count2.get(word, 0) + 1

print(word_count2)
