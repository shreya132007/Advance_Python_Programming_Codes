# TITLE : Apply dynamic programming to determine the longest common subsequence between two sequences.

"""
This program aims to find the longest common subsequence (LCS) between two given sequences. The
LCS of two sequences is the longest sequence that can be derived from both original sequences by
deleting some or no elements without changing the order of the remaining elements. This problem has
applications in bioinformatics, text comparison, and various other fields.
"""

def longest_common_subsequence(str1, str2):
    m = len(str1)
    n = len(str2)

    # Create DP table initialized with 0
    dp = [[0 for j in range(n + 1)] for i in range(m + 1)]

    # Fill the DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Reconstruct the LCS
    i = m
    j = n
    lcs = ""

    while i > 0 and j > 0:
        if str1[i - 1] == str2[j - 1]:
            lcs = str1[i - 1] + lcs
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return lcs, dp[m][n]


# Main Program
sequence1 = input("Enter the first sequence: ")
sequence2 = input("Enter the second sequence: ")

lcs, length = longest_common_subsequence(sequence1, sequence2)

print("\nLongest Common Subsequence:", lcs)
print("Length of LCS:", length)

# shreya@192 ~ % /opt/homebrew/bin/python3 "/Users/sarthak/Desktop/Python /Assignment_5.py"
# Enter the first sequence: ABCDEF
# Enter the second sequence: ADBEFD

# Longest Common Subsequence: ADEF
# Length of LCS: 4