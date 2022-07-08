n = int(input())
arr = list(map(int, input().split()))

dp = [0] * n

for i in range(1, n):
    for k in range(1, i + 2):
        temp = arr[i-k+1:i+1]

        if k == i + 1:
            k = i
        dp[i] = max(dp[i], dp[i-k] + abs(max(temp) - min(temp)))

print(dp[-1])