import sys
# sys.setrecursionlimit(10000)
# x = int(input())
#
# dp = [0] * (20)
#
# dp[1] = 1
# dp[2] = 1
# dp[3] = 1
#
# arr = [x]
#
#
# for i in range(4, x+1):
#     if i % 3 == 0 and i % 2 == 0:
#         dp[i] = min(dp[i//3] + 1, dp[i//2] + 1, dp[i-1] + 1)
#
#     elif i % 3 == 0 and not i % 2 == 0:
#         dp[i] = min(dp[i//3] + 1, dp[i-1] + 1)
#
#     elif i % 2 == 0 and not i % 3 == 0:
#         dp[i] = min(dp[i//2] + 1, dp[i-1] + 1)
#
#     elif not i % 2 == 0 and not i % 3 == 0:
#         dp[i] = min(dp[i-1], dp[i-1] + 1)
#
# mins = sys.maxsize
#
# for a in range(dp[x]-1, 1, -1): # 4 3 2 1
#     print(a)
#     for b in range(x,0,-1):
#         if dp[b] == a:
#             mins = min(b, mins)
#     arr.append(mins)
#
#
# arr.append(1)
#
# print(dp)
# print(dp[x])
# print(*arr)


# N = int(input())
#
# result = [[0, []] for _ in range(N + 1)]  # [최솟값, 경로 리스트]
# result[1][0] = 0  # 최솟값
# result[1][1] = [1]  # 경로를 담을 리스트
#
# for i in range(2, N + 1):
#
#     # f(x-1) + 1
#     result[i][0] = result[i - 1][0] + 1
#     result[i][1] = result[i - 1][1] + [i]
#
#     # f(x//3) + 1
#     if i % 3 == 0 and result[i // 3][0] + 1 < result[i][0]:
#         result[i][0] = result[i // 3][0] + 1
#         result[i][1] = result[i // 3][1] + [i]
#
#     # f(x//2) + 1
#     if i % 2 == 0 and result[i // 2][0] + 1 < result[i][0]:
#         result[i][0] = result[i // 2][0] + 1
#         result[i][1] = result[i // 2][1] + [i]
#
#
#
# print(result[N][0])
# for i in result[N][1][::-1]:  # 뒤집은 뒤 출력
#     print(i, end=' ')

import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
q = deque()
q.append([n])
ans = []

while q:
    a = q.popleft()
    x = a[0]
    print("x", x)

    if x == 1:
        ans = a
        break

    if x % 3 == 0:
        q.append([x // 3] + a)

    if x % 2 == 0:
        q.append([x // 2] + a)

    q.append([x - 1] + a)

print(len(ans) - 1)
print(*ans[::-1])
