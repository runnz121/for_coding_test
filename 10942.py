
import sys
input = sys.stdin.readline

n = int(input())
a = list(input().split())
m = int(input())
dp = [[0 for _ in range(n)]for _ in range(n)]

# 길이가 1인 경우 자기 자신일 경우 -> 펠린드롬
for i in range(n):
    dp[i][i] = 1

# 길이가 2이일 경우 자기 옆인덱스와 같은 경우 -> 펠린드롬
for i in range(n-1):
    if a[i] == a[i+1]:
        dp[i][i+1] = 1

# 길이가 3이상이면 s와 e가 같고, dp[s+1][e-1] 이면 -> 펠린드롬
for i in range(2, n):
    for j in range(n-i):
        if a[j] == a[i+j] and dp[j+1][i+j-1] == 1:
            dp[j][i+j] = 1

for i in range(m):
    s, e = map(int, input().split())
    print(dp[s-1][e-1])

# n = int(input())
#
# arr = list(map(int, input().split()))
#
# m = int(input())
#
# while m > 0:
#     s, e = map(int, input().split())
#     s = s-1
#     print(arr[s:e])
#
#     if len(arr[s:e]) == 2 or len(arr[s:e]) % 2 == 0:
#         print(0)
#
#     else:
#         while True:
#             find = arr[s:e]
#             if s == e - 1:
#                 break
#             if find[s] != find[e-1]:
#                 break
#
#
#             s += 1
#             e -= 1
#
#     m -= 1



# 1 2 3 2 1 2 3 5
