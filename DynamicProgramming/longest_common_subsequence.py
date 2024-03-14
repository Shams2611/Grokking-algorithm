"""
Longest Common Subsequence (LCS) - Chapter 9

Problem: Find the longest subsequence present in both strings.
Subsequence = doesn't have to be contiguous, just in order.

Example: "fish" and "fosh" -> LCS is "fsh" (length 3)

This is useful for:
- diff tools (comparing files)
- DNA sequence comparison
- plagiarism detection

DP approach:
- Build a table where cell[i][j] = LCS length of first i chars of A and j chars of B
- If chars match: cell[i][j] = cell[i-1][j-1] + 1
- If they don't: cell[i][j] = max(cell[i-1][j], cell[i][j-1])

Time: O(m * n)
Space: O(m * n)
"""

def lcs_length(str1, str2):
    """just returns the length of LCS"""
    m, n = len(str1), len(str2)

    # table[i][j] = LCS length for str1[:i] and str2[:j]
    table = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                # chars match, extend previous LCS
                table[i][j] = table[i - 1][j - 1] + 1
            else:
                # take best of ignoring one char from either string
                table[i][j] = max(table[i - 1][j], table[i][j - 1])

    return table[m][n]


def lcs_with_string(str1, str2):
    """returns both length and actual LCS string"""
    m, n = len(str1), len(str2)
    table = [[0] * (n + 1) for _ in range(m + 1)]

    # fill table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                table[i][j] = table[i - 1][j - 1] + 1
            else:
                table[i][j] = max(table[i - 1][j], table[i][j - 1])

    # backtrack to find the actual string
    lcs = []
    i, j = m, n
    while i > 0 and j > 0:
        if str1[i - 1] == str2[j - 1]:
            lcs.append(str1[i - 1])
            i -= 1
            j -= 1
        elif table[i - 1][j] > table[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return table[m][n], ''.join(reversed(lcs))


def print_lcs_table(str1, str2, table):
    """visualize the table"""
    print("     ", end="")
    for c in str2:
        print(f" {c}", end="")
    print()

    for i, row in enumerate(table):
        if i == 0:
            print("  ", end="")
        else:
            print(f"{str1[i-1]} ", end="")

        for val in row:
            print(f" {val}", end="")
        print()


if __name__ == "__main__":
    # examples from the book
    test_cases = [
        ("fish", "fosh"),
        ("fish", "hish"),
        ("fort", "fosh"),
        ("clues", "blue"),
    ]

    for s1, s2 in test_cases:
        length, lcs_str = lcs_with_string(s1, s2)
        print(f"'{s1}' vs '{s2}'")
        print(f"  LCS: '{lcs_str}' (length {length})")
        print()

    # show table for one example
    print("="*40)
    print("Detailed view for 'fish' vs 'fosh':\n")

    s1, s2 = "fish", "fosh"
    m, n = len(s1), len(s2)
    table = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                table[i][j] = table[i - 1][j - 1] + 1
            else:
                table[i][j] = max(table[i - 1][j], table[i][j - 1])

    print_lcs_table(s1, s2, table)
