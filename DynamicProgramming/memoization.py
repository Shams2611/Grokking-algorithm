"""
Memoization - top-down DP

Cache results of function calls.
Same input = return cached result.
"""

def fib_memo(n, cache={}):
    if n in cache:
        return cache[n]
    if n <= 1:
        return n

    result = fib_memo(n-1, cache) + fib_memo(n-2, cache)
    cache[n] = result
    return result


# or use decorator
from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)


print(f"fib(50) = {fib(50)}")
