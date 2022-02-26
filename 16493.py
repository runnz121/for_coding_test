# n, m = map(int, input().split())
#
# # day 기준으로 dp
# dp = [0] * (n + 1)
#
# for i in range(1, m+1):
#     day, page = map(int, input().split())
#
#     if day <= i:
#         dp[i] = max(dp[i-1], dp[i-day] + page)
#     else:
#         dp[i] = dp[i-1] + page
#
# print(dp[m])

# 일, 페이지
n, m = map(int,input().split())

# 챕터를 기준으로 해야됨
# dp[i][j] => i챕터, j일 까지 검사했을 때 읽을 수 있는 최대 페이지 수
dp = [[0] * (n + 1) for _ in range(m + 1)]

# 모든 챕터를 돌린다
for i in range(1, m+1):
    day, page = map(int, input().split())

    #일 수를 기준으로 업데이트한다
    for j in range(1, n + 1):
        if j >= day:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-day] + page)
        else:
            dp[i][j] = dp[i-1][j]
print(dp)
print(dp[-1][-1])