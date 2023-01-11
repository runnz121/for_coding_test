import sys

input = sys.stdin.readline

n = int(input())

arr = list(map(int, input().split()))

k = int(input())

dp = [0] * n

dp[0] = arr[0]

for i in range(1, n):
    dp[i] = dp[i-1] + arr[i]

for idx in range(k):
    i, j = map(int, input().split())

    x = dp[i - 2]
    if i - 2 < 0:
        x = 0

    print(dp[j-1] - x)