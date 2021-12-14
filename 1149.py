import sys
T = int(input())

# arr = [[] * 3 for _ in range(T)]
arr = [[0] * T for _ in range(3)]
dp = []
for i in range(T):
    dp.append(list(map(int, sys.stdin.readline().split())))


res1 = dp[0][0]
for i in range(T-2, 2):
    res1 += min(dp[i + 1][1], dp[i + 1][2])
    if dp[i+1][1] > dp[i+1][2]:
        res1 += min(dp[i+2][1], dp[i+2][0])
    else:
        res1 += min(dp[i+2][2], dp[i+2][0])

res2 = dp[0][1]
for i in range(T-2, 2):
    res2 += min(dp[i + 1][0], dp[i + 1][2])
    if dp[i+1][0] > dp[i+1][2]:
        res2 += min(dp[i+2][1], dp[i+2][0])
    else:
        res2 += min(dp[i + 2][2], dp[i + 2][1])

res3 = dp[0][2]
for i in range(T-2, 2):
    res3 += min(dp[i + 1][1], dp[i + 1][0])
    if dp[i+1][1] > dp[i+1][0]:
        res3 += min(dp[i+2][1], dp[i+2][2])
    else:
        res3 += min(dp[i+2][0], dp[i+2][2])

print(res1, res2, res3)
print(min(res1, res2, res3))