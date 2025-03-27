"""
Longest Common Substring

Different from subsequence - must be contiguous!
"fish" and "fosh" -> "sh" (length 2)
"""

def longest_substring(s1, s2):
    m, n = len(s1), len(s2)
    table = [[0] * (n + 1) for _ in range(m + 1)]
    max_len = 0

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i-1] == s2[j-1]:
                table[i][j] = table[i-1][j-1] + 1
                max_len = max(max_len, table[i][j])
            else:
                table[i][j] = 0  # reset!

    return max_len


print(f"fish vs fosh: {longest_substring('fish', 'fosh')}")
print(f"abcdef vs zabcf: {longest_substring('abcdef', 'zabcf')}")
