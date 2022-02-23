import sys
from itertools import permutations

input = sys.stdin.readline

n = int(input())
health = [0] + list(map(int, input().split()))
happy = [0] + list(map(int, input().split()))

#https://sangminlog.tistory.com/entry/boj-1535

# i개의 물건마다 체력을 dp로 생성
dp = [[0] * 101 for _ in range(n + 1)]

for i in range(1, n+1):
    for j in range(1,101):
        # 체력을 기준으로 dp 함 따라서 i 번째 체력 소모값이 dp의 보다 낮을 경우 (즉 체력소모량이 초과되는 경우)
        if health[i] <= j:
            # 인덱스가 헬스, 값이 행복
            # 이전단계의 행복값과, 이전값을 빼고 현재 값을 넣은것과 비교해서 더 큰것을 선택
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-health[i]] + happy[i])
        # 체력량이 소모가 되는 경우가 아니라면 행복을 얻을 수 있음으로 테이블 갱신
        else:
            dp[i][j] = dp[i-1][j]
    print(dp ,"end", i)

# 체력 100을 완전 소모하면 죽으니 99번째 값 출력
print(dp[n][99])