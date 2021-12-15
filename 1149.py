# import sys
# T = int(input())
#
# # arr = [[] * 3 for _ in range(T)]
# # arr = [[0] * T for _ in range(3)]
# dp = []
# for i in range(T):
#     dp.append(list(map(int, sys.stdin.readline().split())))
#
#
# res1 = dp[0][0]
# for i in range(T-2, 2):
#     res1 += min(dp[i + 1][1], dp[i + 1][2])
#     if dp[i+1][1] > dp[i+1][2]:
#         res1 += min(dp[i+2][1], dp[i+2][0])
#     else:
#         res1 += min(dp[i+2][2], dp[i+2][0])
#
# res2 = dp[0][1]
# for i in range(T-2, 2):
#     res2 += min(dp[i + 1][0], dp[i + 1][2])
#     if dp[i+1][0] > dp[i+1][2]:
#         res2 += min(dp[i+2][1], dp[i+2][0])
#     else:
#         res2 += min(dp[i + 2][2], dp[i + 2][1])
#
# res3 = dp[0][2]
# for i in range(T-2, 2):
#     res3 += min(dp[i + 1][1], dp[i + 1][0])
#     if dp[i+1][1] > dp[i+1][0]:
#         res3 += min(dp[i+2][1], dp[i+2][2])
#     else:
#         res3 += min(dp[i+2][0], dp[i+2][2])
#
# print(res1, res2, res3)
# print(min(res1, res2, res3))


import sys
T = int(input())
dp = []
for i in range(T):
    dp.append(list(map(int, sys.stdin.readline().split())))

# 다음 dp 의 값은 바로 하위 인덱스 값 빼고 이전 인덱스의 최소값을 더한 값으로 출력
# 즉 dp[1][0]번째는 조건에 따라 바로 아래 인덱스값을 제외한 min(dp[0][1], dp[0][2])
# 이전 dp 값에서 최소값을 누적해서 더해서 구함
for i in range(T-1):
    for j in range(3):
        if j == 0:
            dp[i+1][0] += min(dp[i][1], dp[i][2])
        if j == 2:
            dp[i+1][2] += min(dp[i][0], dp[i][1])
        if j == 1:
            dp[i + 1][1] += min(dp[i][0], dp[i][2])
print(min(dp[T-1]))



























