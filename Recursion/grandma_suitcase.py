"""
Grandma's Suitcase - Iterative Approach (Using Loops)

Problem: You're looking for a key in a box that contains other boxes,
which may contain more boxes. How do you search through all of them?

This solution uses a WHILE LOOP with a pile/stack to track boxes to search.

Time Complexity: O(n) - where n is total number of items in all boxes
Space Complexity: O(n) - pile can grow to hold all boxes
"""


def look_for_key(main_box):
    """
    Search for a key in nested boxes using iteration (loops).

    Algorithm:
    1. Create a pile of boxes to search
    2. Grab a box from the pile
    3. Search through each item in the box
    4. If item is a box, add it to the pile
    5. If item is a key, we found it!
    6. Repeat until pile is empty

    Args:
        main_box: The outermost box to start searching from

    Returns:
        True if key is found, False otherwise
    """
    pile = [main_box]  # Start with the main box in our pile

    while pile:  # While there are boxes to search
        box = pile.pop()  # Grab a box from the pile
        for item in box:
            if item.is_a_box():
                pile.append(item)  # Add box to pile to search later
            elif item.is_a_key():
                print("Found the key!")
                return True

    print("Key not found.")
    return False


# Example usage with simple data structure
if __name__ == "__main__":
    # Simulating nested boxes with nested lists
    # 'K' represents the key, lists represent boxes

    class Item:
        def __init__(self, value):
            self.value = value
        def is_a_box(self):
            return isinstance(self.value, list)
        def is_a_key(self):
            return self.value == 'K'
        def __iter__(self):
            return iter([Item(v) for v in self.value])

    # Box structure: [[['K'], 'stuff'], 'more stuff']
    nested_boxes = Item([
        Item([
            Item(['K']),  # Key is here!
            'stuff'
        ]),
        'more stuff'
    ])

    print("Searching for key in nested boxes (iterative)...")
    # Note: This example is pseudocode-like; real implementation
    # would need proper box/item classes
