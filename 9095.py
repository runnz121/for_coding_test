t = int(input())

for i in range(t):
    x = int(input())

    dp = [0] * 11
    dp[1] = 1
    dp[2] = 2
    dp[3] = 4

    for k in range(4, 11):
        dp[k] = dp[k-3] + dp[k-2] + dp[k-1]
    print(dp[x])