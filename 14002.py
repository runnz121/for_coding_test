import copy
import sys
input = sys.stdin.readline

n = int(input())

arr = list(map(int, input().split()))

comp = copy.deepcopy(arr)

dp = [1] * n

ans = []

for i in range(n):
    temp = set()
    for j in range(i+1):
        if arr[i] > comp[j]:
            dp[i] = max(dp[i], dp[j] + 1)

longest = max(dp)
print(longest)

# for k in range(longest, -1, -1):
#     idx = dp.index(k)
#     ans.append(arr[idx])
#
# ans.reverse()
# print(*ans)
# print(dp)

answer = []
for i in range(n - 1, -1, -1):
    if dp[i] == longest:
        answer.append(arr[i])
        longest -=1
answer.reverse()
#print(dp)
print(*answer)