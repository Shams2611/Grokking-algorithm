"""
Two Sum problem - classic interview question

Find two numbers that add up to target
Hash table makes it O(n) instead of O(n^2)
"""


def two_sum_bruteforce(nums, target):
    """O(n^2) - check all pairs"""
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return None


def two_sum_hash(nums, target):
    """O(n) - use hash table"""
    seen = {}  # value -> index

    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i

    return None


nums = [2, 7, 11, 15]
target = 9
print(f"Bruteforce: {two_sum_bruteforce(nums, target)}")
print(f"Hash table: {two_sum_hash(nums, target)}")
