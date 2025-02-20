"""
Classroom scheduling

Fit as many classes as possible in one room.
Greedy: pick class that ends earliest.
"""

def schedule(classes):
    # sort by end time
    classes = sorted(classes, key=lambda x: x[1])

    result = []
    last_end = 0

    for name, start, end in classes:
        if start >= last_end:
            result.append(name)
            last_end = end

    return result


classes = [
    ("Art", 9, 10),
    ("English", 9, 11),
    ("Math", 10, 11),
    ("CS", 10, 12),
    ("Music", 11, 12),
]

print("Classes:", schedule(classes))
