"""
Reverse string recursively

Base: empty or single char
Recursive: last char + reverse(rest)
"""

def reverse(s):
    if len(s) <= 1:
        return s
    return s[-1] + reverse(s[:-1])


print(reverse("hello"))  # olleh
print(reverse("a"))      # a
print(reverse(""))       # empty
