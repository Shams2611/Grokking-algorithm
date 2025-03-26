"""
LCS - get actual subsequence string
"""

def lcs_string(s1, s2):
    m, n = len(s1), len(s2)
    table = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i-1] == s2[j-1]:
                table[i][j] = table[i-1][j-1] + 1
            else:
                table[i][j] = max(table[i-1][j], table[i][j-1])

    # backtrack
    result = []
    i, j = m, n
    while i > 0 and j > 0:
        if s1[i-1] == s2[j-1]:
            result.append(s1[i-1])
            i -= 1
            j -= 1
        elif table[i-1][j] > table[i][j-1]:
            i -= 1
        else:
            j -= 1

    return ''.join(reversed(result))


print(f"fish vs fosh: '{lcs_string('fish', 'fosh')}'")
print(f"ABCD vs ACBAD: '{lcs_string('ABCD', 'ACBAD')}'")
