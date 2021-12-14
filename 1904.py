N = int(input())

# 해당 갯수 저장
dp = [0] * (N+2)

dp[0] = 0
dp[1] = 1
dp[2] = 2

for i in range(3, N+1):
    dp[i] = (dp[i-1] + dp[i-2])%15746

print(dp[N]%15746)