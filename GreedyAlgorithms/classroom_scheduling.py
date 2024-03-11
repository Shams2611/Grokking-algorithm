"""
Classroom Scheduling - classic greedy problem

Problem: You have a list of classes with start/end times.
You want to fit as many classes as possible in one classroom.

Greedy solution: Always pick the class that ENDS earliest.
This leaves maximum time for remaining classes.

Why this works: ending early = more room for other classes
"""

def schedule_classes(classes):
    """
    classes: list of (name, start, end) tuples
    returns: list of classes that fit without overlap
    """
    # sort by end time - key insight!
    sorted_classes = sorted(classes, key=lambda x: x[2])

    schedule = []
    last_end = 0  # when the last scheduled class ends

    for name, start, end in sorted_classes:
        if start >= last_end:
            # this class fits
            schedule.append((name, start, end))
            last_end = end
            print(f"Added: {name} ({start}:00 - {end}:00)")
        else:
            print(f"Skipped: {name} ({start}:00 - {end}:00) - overlaps")

    return schedule


if __name__ == "__main__":
    # class schedule with name, start hour, end hour
    classes = [
        ("Art", 9, 10),
        ("Eng", 9, 11),       # overlaps with art
        ("Math", 10, 11),
        ("CS", 10, 12),       # overlaps with math
        ("Music", 11, 12),
        ("History", 11, 13),  # overlaps with music
    ]

    print("Available classes:")
    for name, start, end in classes:
        print(f"  {name}: {start}:00 - {end}:00")

    print("\n--- Scheduling ---\n")
    schedule = schedule_classes(classes)

    print(f"\nFinal schedule ({len(schedule)} classes):")
    for name, start, end in schedule:
        print(f"  {start}:00 - {end}:00: {name}")

    # visual timeline
    print("\nTimeline:")
    print("  9    10    11    12    13")
    print("  |     |     |     |     |")
    for name, start, end in schedule:
        spaces = "      " * (start - 9)
        blocks = "####" * (end - start)
        print(f"  {spaces}{blocks} {name}")
