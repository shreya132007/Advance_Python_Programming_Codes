"""
7. Longest Common Subsequence

Develop a Python program to determine the length of the Longest Common Subsequence (LCS) between two strings.
Requirements :-
1. Accept two strings.
2. Use Dynamic Programming.
3. Display the LCS length.
"""


str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

m = len(str1)
n = len(str2)

dp = [[0] * (n + 1) for i in range(m + 1)]

for i in range(1, m + 1):
    for j in range(1, n + 1):
        if str1[i - 1] == str2[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

print("LCS length =", dp[m][n])