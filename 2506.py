n = int(input())
arr = list(map(int, input().split()))
dp = [0 for _ in range(n + 1)]
ans = 0
for i in range(n):
    if arr[i] != 0:
        dp[i] = dp[i-1] + 1

print(sum(dp))