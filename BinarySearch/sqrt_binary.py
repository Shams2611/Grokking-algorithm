"""
Square root using binary search

Find largest x where x*x <= n
"""

def sqrt_int(n):
    if n < 2:
        return n

    low, high = 1, n // 2
    result = 1

    while low <= high:
        mid = (low + high) // 2
        if mid * mid == n:
            return mid
        elif mid * mid < n:
            result = mid
            low = mid + 1
        else:
            high = mid - 1

    return result


print(f"sqrt(16) = {sqrt_int(16)}")
print(f"sqrt(10) = {sqrt_int(10)}")
print(f"sqrt(100) = {sqrt_int(100)}")
