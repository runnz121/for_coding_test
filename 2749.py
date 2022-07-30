a = int(input())

dp = []
dp[0] = 0
dp[1] = 1
dp[2] = 1

for i in range(3, a+1):



print(dp[a])