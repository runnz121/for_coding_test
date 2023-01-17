n, m = map(int, input().split())
arr = list(map(int, input().split()))

dp = [0] * n
dp[0] = arr[0]

for i in range(1, n):
    dp[i] = dp[i-1] + arr[i]

max_res = dp[m-1]
for idx in range(m, n):

    find = dp[idx] - dp[idx-m]
    max_res = max(find, max_res)

print(max_res)