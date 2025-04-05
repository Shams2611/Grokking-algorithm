"""
Job sequencing with deadlines

Each job has profit and deadline.
Do highest profit jobs first.
"""

def job_sequence(jobs, max_deadline):
    # sort by profit descending
    jobs = sorted(jobs, key=lambda x: x[2], reverse=True)

    slots = [None] * max_deadline
    total = 0

    for name, deadline, profit in jobs:
        # find latest available slot before deadline
        for i in range(min(deadline, max_deadline) - 1, -1, -1):
            if slots[i] is None:
                slots[i] = name
                total += profit
                break

    return [j for j in slots if j], total


# (name, deadline, profit)
jobs = [
    ("A", 2, 100),
    ("B", 1, 19),
    ("C", 2, 27),
    ("D", 1, 25),
    ("E", 3, 15),
]

sequence, profit = job_sequence(jobs, 3)
print(f"Jobs: {sequence}")
print(f"Total profit: {profit}")
