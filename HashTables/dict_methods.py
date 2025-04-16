"""
Useful dict methods in Python

Good to know these for interviews
"""

d = {"a": 1, "b": 2, "c": 3}

# get with default
print(d.get("x", 0))  # 0 instead of error

# keys, values, items
print(list(d.keys()))
print(list(d.values()))
print(list(d.items()))

# pop removes and returns
val = d.pop("b")
print(f"Popped: {val}, dict now: {d}")

# setdefault - set if not exists
d.setdefault("x", 100)
print(d)

# update - merge dicts
d.update({"y": 200, "z": 300})
print(d)
