from collections import deque

m, n = map(int, input().split())

graph = []

for i in range(n):
    graph.append(list(map(int, input().split())))

que = deque()

# que 에 1인 경우를 모두 넣어줌(1이 여러개 있을 경우가 있기 때문에)
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            que.append([i, j])

def bfs():

    # 4방향 탐색
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    while que:
        x, y = que.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue

            if graph[nx][ny] == 1 or graph[nx][ny] == -1:
                continue

            if graph[nx][ny] == 0:
                graph[nx][ny] = 1

                # 그래프에 누적합을 시켜줌
                graph[nx][ny] = graph[x][y] + 1
                que.append([nx, ny])

# 큐에 넣은 값들을 실행 시킴
bfs()


# 그래프 돌면서 0 이있는지를 확인함
# 있으면 다 못익힌것임으로 -1
# 없으면 누적합중 최대값 출력
ans = 0
for i in graph:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
    ans = max(ans, max(i))


# 1부터 시작했기 때문에 1 빼줌
print(ans-1)