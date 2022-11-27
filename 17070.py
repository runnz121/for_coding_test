n = int(input())
graph = [[] for _ in range(n)]

# 0은 가로, 1은 세로, 2는 대각선(1번째 값을 말함, 2번째 3번째 값은 x, y, 좌표를 뜻함)
dp = [[[0] * n for _ in range(n)] for _ in range(3)] # dp 그래프는 총 3차원 그래프로 graph가 3개 있다고 생각하면 된다(3가지 방법을 가각ㄱ 저장하기 위해)

# 그래프 정보 입력
for i in range(n):
    graph[i] = list(map(int, input().split()))

dp[0][0][1] = 1  # 첫 시작 위치

# dp를 위해서는 윗 행을 사용해야하므로 첫 행을 먼저 초기화(첫행은 가로로 파이프가 놓여져있음으로)
for i in range(2, n):
    if graph[0][i] == 0:
        dp[0][0][i] = dp[0][0][i - 1]

for r in range(1, n):
    for c in range(1, n):
        # 현재위치가 대각선인 경우
        if graph[r][c] == 0 and graph[r][c - 1] == 0 and graph[r - 1][c] == 0:# 대각선은 3군데가 비어있어야 함으로
            dp[2][r][c] = dp[0][r - 1][c - 1] + dp[1][r - 1][c - 1] + dp[2][r - 1][c - 1] # dp의 3번째 에 저장함

        if graph[r][c] == 0:
            # 현재 위치가 가로인 경우
            dp[0][r][c] = dp[0][r][c - 1] + dp[2][r][c - 1]
            # 현재 위치가 세로인 경우
            dp[1][r][c] = dp[1][r - 1][c] + dp[2][r - 1][c]

print(sum(dp[i][n - 1][n - 1] for i in range(3)))