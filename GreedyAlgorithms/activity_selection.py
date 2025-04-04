"""
Activity selection

Similar to classroom scheduling.
Pick most activities that don't overlap.
"""

def select_activities(activities):
    # sort by finish time
    activities = sorted(activities, key=lambda x: x[1])

    selected = [activities[0]]

    for act in activities[1:]:
        if act[0] >= selected[-1][1]:
            selected.append(act)

    return selected


# (start, finish)
activities = [
    (1, 4),
    (3, 5),
    (0, 6),
    (5, 7),
    (3, 9),
    (5, 9),
    (6, 10),
    (8, 11),
]

result = select_activities(activities)
print(f"Selected: {result}")
print(f"Count: {len(result)}")
