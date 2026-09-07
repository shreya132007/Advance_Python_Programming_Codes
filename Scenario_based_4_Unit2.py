"""
4. House Robber Problem

Develop a Python program to determine the maximum amount that can be collected without selecting two adjacent houses.
Requirements
1. Accept the amount present in each house.
2. Use Dynamic Programming.
3. Display the maximum possible amount.
"""


n = int(input("Enter number of houses: "))
house = []

for i in range(n):
    amount = int(input("Enter amount in house: "))
    house.append(amount)

if n == 0:
    print("Maximum amount =", 0)
elif n == 1:
    print("Maximum amount =", house[0])
else:
    dp = [0] * n
    dp[0] = house[0]
    dp[1] = max(house[0], house[1])

    for i in range(2, n):
        dp[i] = max(dp[i-1], dp[i-2] + house[i])

    print("Maximum amount =", dp[n-1])