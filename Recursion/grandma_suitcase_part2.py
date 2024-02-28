"""
Grandma's Suitcase - Recursive Approach

Problem: You're looking for a key in a box that contains other boxes,
which may contain more boxes. How do you search through all of them?

This solution uses RECURSION - when we find a box, we call the same
function on that box.

Time Complexity: O(n) - where n is total number of items in all boxes
Space Complexity: O(d) - where d is the maximum nesting depth (call stack)

Quote from Leigh Caldwell:
"Loops may achieve a performance gain for your program.
Recursion may achieve a performance gain for your programmer.
Choose which is more important in your situation!"
"""


def look_for_key(box):
    """
    Search for a key in nested boxes using recursion.

    Algorithm:
    1. For each item in the box:
       - If it's a box, recursively search that box
       - If it's a key, we found it!

    This is more elegant than the iterative approach because
    the call stack naturally handles the "pile" of boxes.

    Args:
        box: A box (container) to search through

    Returns:
        True if key is found, False otherwise
    """
    for item in box:
        if item.is_a_box():
            # Recursive case: search inside the nested box
            if look_for_key(item):
                return True
        elif item.is_a_key():
            # Base case: we found the key!
            print("Found the key!")
            return True

    return False


# Example usage with simple simulation
if __name__ == "__main__":
    # Simple class to simulate boxes and items
    class Item:
        def __init__(self, content, is_key=False):
            self.content = content
            self._is_key = is_key

        def is_a_box(self):
            return isinstance(self.content, list)

        def is_a_key(self):
            return self._is_key

        def __iter__(self):
            if self.is_a_box():
                return iter(self.content)
            return iter([])

    # Create nested boxes: Box[ Box[ Box[KEY], item ], item ]
    key = Item("key", is_key=True)
    inner_box = Item([key])
    middle_box = Item([inner_box, Item("socks")])
    outer_box = Item([middle_box, Item("photos")])

    print("Searching for key in nested boxes (recursive)...")
    result = look_for_key(outer_box)
    print(f"Key found: {result}")
