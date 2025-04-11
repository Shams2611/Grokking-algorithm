"""
Example: check if someone already voted

Hash table makes this O(1) instead of searching a list
"""

voted = {}


def check_voter(name):
    if name in voted:
        print(f"{name} already voted!")
        return False
    else:
        voted[name] = True
        print(f"{name} can vote")
        return True


check_voter("tom")
check_voter("alice")
check_voter("tom")  # already voted!
check_voter("bob")
