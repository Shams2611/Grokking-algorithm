"""
Calculate power recursively

x^n = x * x^(n-1)
"""

def power(x, n):
    if n == 0:
        return 1
    return x * power(x, n - 1)


print(f"2^10 = {power(2, 10)}")  # 1024
print(f"3^4 = {power(3, 4)}")   # 81
