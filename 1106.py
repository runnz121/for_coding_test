# import sys
#
# input = sys.stdin.readline
# INF = 1e9
#
# c, n = map(int, input().split())
# data = []
#
# min_cost = [INF] * (c+100)
# min_cost[0] = 0
#
# for _ in range(n):
#     # cost, cus
#     data.append(list(map(int, input().split())))
#
# # print(data)
#
# # cost 순서 작은 순서로 정리
# data_sort = sorted(data, key = lambda x: x[0])
#
# # print(data_sort)
#
# for cost, cus in data:
#     print(data)
#     for i in range(cus, c+100): # 최소값 지정해주기 위해서
#         min_cost[i] = min(min_cost[i-cus] + cost, min_cost[i])
#
# print(min(min_cost[c:]))


n, m = map(int, input().split())
INF = int(1e9)

#dp = [[0] + [INF] * (n + 1) for _ in range(m + 1)]

dp = [INF] * 101
dp[0] = 0

for _ in range(1, m + 1):
    cost, people = map(int, input().split())

    for j in range(cost, n + 1):
        print(cost, people)
        #   if j >= people:
        dp[j] = min(dp[j-people] + cost, dp[j])

        #dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - people] + cost)
    # else:
    #     dp[i][j] = dp[i-1][j]
print(dp)
print(dp[n])
