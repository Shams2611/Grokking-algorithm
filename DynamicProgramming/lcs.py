"""
Longest Common Subsequence

Subsequence doesn't have to be contiguous.
"fish" and "fosh" -> "fsh" (length 3)
"""

def lcs(s1, s2):
    m, n = len(s1), len(s2)
    table = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i-1] == s2[j-1]:
                table[i][j] = table[i-1][j-1] + 1
            else:
                table[i][j] = max(table[i-1][j], table[i][j-1])

    return table[m][n]


print(f"fish vs fosh: {lcs('fish', 'fosh')}")
print(f"abc vs ac: {lcs('abc', 'ac')}")
