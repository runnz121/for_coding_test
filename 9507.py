n = int(input())

dp = [0] * 70
dp[0] = 1
dp[1] = 1
dp[2] = 2
dp[3] = 4




def pibo(k):
    if k < 4:
        return dp[k]
    else:
        dp[k] = dp[k-4] + dp[k-3] + dp[k-2] + dp[k-1]
        return dp[k]

for i in range(70):
    pibo(i)

for i in range(n):
    x = int(input())
    print(dp[x])