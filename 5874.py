import sys
input = sys.stdin.readline

arr = list(input().rstrip())

# 뒷다리 ((, 앞다리 ))

dp = [0] * (len(arr))

for i in range(len(arr)):
    if i == 0:
        if arr[i] == ')':
            dp[i] = 1
        else:
            dp[i] = -1
    else:
        if arr[i] == ')':
            dp[i] = dp[i-1] + 1
        else:
            dp[i] = dp[i-1] - 1

count = 0
for i in dp:
    if i == 0:
        count += 1
print(dp)
print(count)