n, k = map(int, input().split())

arr = []

INF = int(1e9)

for _ in range(n):
    x = int(input())
    arr.append(x)

arr.sort()
dp = [INF] * (k + 1)

for i in arr:
    for j in range(k + 1):
        if j % i == 0:
            dp[j] = min(j//i, dp[j])
        elif j > i :
            dp[j] = min(dp[j-i] + 1, dp[j])

if dp[k] == INF:
    print(-1)
else:
    print(dp[k])