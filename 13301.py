n = int(input())

dp = [0] * 81

dp[0] = 1
dp[1] = 1
dp[2] = 2

for i in range(2, n + 1):
    dp[i] = dp[i - 1] + dp[i - 2]

if n == 1:
    print(4)
else:
    print(dp[n] * 2 + dp[n-1] * 2)