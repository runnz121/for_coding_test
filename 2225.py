
n, k = map(int, input().split())

dp = [[0] * (n + 1) for _ in range(k)]


for x in range(n+1):
    dp[0][x] = 1

for i in range(1, k):
    dp[i][0] = 1
    for j in range(1, n+1):
        dp[i][j] = dp[i][j-1] + dp[i-1][j]


print(dp[k-1][n]%1000000000)
# x , n 일떄 n이 들어오는 것
#     0 1  2  3  4  5  6
# 1 : 1 1  1  1  1  1  1
# 2 : 1 2  3  4  5  6  7
# 3 : 1 3  6 10 15 21 28
# 4 : 1 4 10 20 35 56 84

# n, k = map(int, input().split())
# cnt = 0
# tmp = []
# check = [False] * n
#
# def back(depth):
#
#     global tmp
#     global cnt
#
#     if depth == k:
#         if sum(tmp) == n:
#             print(tmp)
#             cnt += 1
#         return
#
#
#     for i in range(n):
#         if check[i]:
#             continue
#
#         tmp.append(i)
#         #check[i] = True
#         back(depth + 1)
#         tmp.pop()
#         #check[i] = False
#
# back(0)
#
# print(cnt + k)

# n, k = map(int, input().split())
#
# cnt = 0
#
# dp = [0] * n
# dp[1] = 1
#
# tmp = []
#
# check = [False] * n
#
# def back(depth):
#
#     global tmp
#     global cnt
#
#     if depth == k:
#         if sum(tmp) == n:
#             cnt += 1
#         return
#
#
#     for i in range(n):
#         if check[i]:
#             continue
#
#         tmp.append(i)
#         #check[i] = True
#         back(depth + 1)
#         tmp.pop()
#         #check[i] = False
#
# back(0)
#
# print(cnt + k)

# 20, 2

# 0 -> (0,0)                                        \\ 1
# 1 ->                   ||(1,0),(0,1)(k 갯수(0))    \\ 2
# 2 -> (1,1),            ||(2,0),(0,2)              \\ 3
# 3 -> (1,2),(2,1)       ||(0,3),(3,0)              \\ 4
# 4 -> (1,3),(3,1),(2,2) ||(4,0),(0,4)              \\ 5


# 6, 4

# 0 -> (0,0,0,0)
# 1 -> (1,0,0,0), (0,0,0,1), (0,1,0,0), (0,0,1,0)
# 2 -> (1,1,0,0), (0,0,1,1), (1,0,0,1), (0,1,1,0) ,
