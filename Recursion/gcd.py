"""
Greatest common divisor - Euclidean algorithm

gcd(a, b) = gcd(b, a % b)
Base: b == 0 -> return a
"""

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


print(f"gcd(48, 18) = {gcd(48, 18)}")  # 6
print(f"gcd(100, 25) = {gcd(100, 25)}")  # 25
