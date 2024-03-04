"""
Hash Tables - Chapter 5

Hash tables = dictionaries in Python. Super useful data structure.

The magic: O(1) average lookup time! Compare to O(n) for lists.

How it works (simplified):
1. Hash function takes a key -> returns an index
2. Store value at that index in an array
3. To lookup: hash the key again, go directly to that spot

Python's dict handles all this for us but good to know what's happening underneath.

Collisions: when two keys hash to same index. Python handles this automatically.

Use cases from the book:
- Phone book (name -> number)
- DNS (domain -> IP)
- Caching
- Detecting duplicates
"""

# basic phonebook example
phonebook = {}
phonebook["jenny"] = "867-5309"
phonebook["emergency"] = "911"
phonebook["pizza"] = "555-1234"

print("Phone book:")
for name, number in phonebook.items():
    print(f"  {name}: {number}")

# lookup is O(1)
print(f"\nJenny's number: {phonebook['jenny']}")
print(f"Is 'jenny' in phonebook? {'jenny' in phonebook}")
print(f"Is 'bob' in phonebook? {'bob' in phonebook}")


# voting example from the book - checking if someone already voted
def check_voter(voters, name):
    if name in voters:
        print(f"{name} has already voted!")
    else:
        voters[name] = True
        print(f"{name} can vote")

print("\n--- Voting booth ---")
voters = {}
check_voter(voters, "tom")
check_voter(voters, "alice")
check_voter(voters, "tom")  # already voted!


# caching example - store results so we don't recompute
cache = {}

def get_page(url):
    """
    pretend this fetches a webpage
    with caching so we don't fetch same page twice
    """
    if url in cache:
        print(f"  (returning cached data for {url})")
        return cache[url]

    # simulate fetching page
    print(f"  (fetching {url} from server...)")
    data = f"<html>Content of {url}</html>"

    # save in cache for next time
    cache[url] = data
    return data

print("\n--- Caching demo ---")
get_page("google.com")
get_page("facebook.com")
get_page("google.com")  # this one's cached!
get_page("google.com")  # still cached


# hash tables for counting
def count_words(text):
    """count occurrences of each word"""
    word_count = {}
    words = text.lower().split()

    for word in words:
        # strip punctuation (lazy way)
        word = word.strip(".,!?")
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    return word_count

print("\n--- Word counting ---")
sample = "the cat sat on the mat and the cat was happy"
counts = count_words(sample)
print(f"Text: {sample}")
print(f"Counts: {counts}")
