n = int(input())
arr = list(map(int, input().split()))

dp = [0] * len(arr)


for i in range(len(arr)):
    for j in range(i, len(arr)):
        if arr[i] < arr[j]:
            dp[j] = max(dp[j], dp[i] + 1)

print(max(dp) + 1)