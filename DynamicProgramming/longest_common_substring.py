"""
Longest Common Substring - Chapter 9

Different from subsequence - substring must be CONTIGUOUS.

Example: "fish" and "fosh" -> longest common substring is "sh" (length 2)
         but LCS (subsequence) would be "fsh" (length 3)

DP approach similar but:
- If chars match: cell[i][j] = cell[i-1][j-1] + 1
- If they don't: cell[i][j] = 0  <-- this is the difference!

The answer is the MAX value in the table, not the bottom-right corner.

Time: O(m * n)
Space: O(m * n)
"""

def longest_common_substring(str1, str2):
    """returns length and starting positions of longest common substring"""
    m, n = len(str1), len(str2)

    table = [[0] * (n + 1) for _ in range(m + 1)]

    max_length = 0
    end_pos = 0  # ending position in str1

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                table[i][j] = table[i - 1][j - 1] + 1

                if table[i][j] > max_length:
                    max_length = table[i][j]
                    end_pos = i
            else:
                table[i][j] = 0  # reset! substring must be contiguous

    # extract the substring
    start_pos = end_pos - max_length
    substring = str1[start_pos:end_pos]

    return max_length, substring


def compare_substring_vs_subsequence(str1, str2):
    """show the difference between substring and subsequence"""
    # substring
    sub_len, substring = longest_common_substring(str1, str2)

    # subsequence (using function from other file, reimplemented here)
    m, n = len(str1), len(str2)
    table = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                table[i][j] = table[i - 1][j - 1] + 1
            else:
                table[i][j] = max(table[i - 1][j], table[i][j - 1])

    seq_len = table[m][n]

    return {
        'substring': (sub_len, substring),
        'subsequence_length': seq_len
    }


if __name__ == "__main__":
    test_cases = [
        ("fish", "fosh"),
        ("fish", "hish"),
        ("abcdef", "zbcdf"),
        ("programming", "gaming"),
    ]

    for s1, s2 in test_cases:
        length, substr = longest_common_substring(s1, s2)
        print(f"'{s1}' vs '{s2}'")
        print(f"  Longest common substring: '{substr}' (length {length})")
        print()

    print("="*50)
    print("Substring vs Subsequence comparison:\n")

    for s1, s2 in test_cases:
        result = compare_substring_vs_subsequence(s1, s2)
        print(f"'{s1}' vs '{s2}':")
        print(f"  Substring: '{result['substring'][1]}' (len {result['substring'][0]})")
        print(f"  Subsequence length: {result['subsequence_length']}")
        print()
