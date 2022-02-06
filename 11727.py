x = int(input())

dp = [0] * 1001

dp[0] = 0
dp[1] = 1
dp[2] = 3
dp[3] = 5
for i in range(4, x+1):
    if i % 2 == 0:
        dp[i] = dp[i-1] * 2 + 1
    else:
        dp[i] = dp[i-1] * 2 - 1
print(dp[x] % 10007)

# n = int(input())
#
# dp = [0] * 1001
#
# dp[0] = 0
# dp[1] = 1
# dp[2] = 2
#
# for i in range(3, n + 1):
#     dp[i] = dp[i - 1] + dp[i - 2]
# print(dp[n] % 10007)