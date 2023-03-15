from collections import deque

m, n = map(int, input().split())
graph = []

for i in range(n):
    arr = list(map(int, input()))
    graph.append(arr)

dx = [-1,1,0,0]
dy = [0,0,-1,1]

dist = [[-1] * m for _ in range(n)]  # 가중치


def bfs(x, y):

    que = deque()
    que.append([x, y])
    dist[0][0] = 0

    while que:
        x, y = que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if dist[nx][ny] == -1:
                    # 벽을 안부셔도 되는 경우
                    if graph[nx][ny] == 0:
                        dist[nx][ny] = dist[x][y]
                        que.appendleft([nx, ny])
                    # 벽을 부셔야 하는 경우
                    else:
                        dist[nx][ny] = dist[x][y] + 1
                        que.append([nx, ny])

bfs(0,0)


print(dist[n-1][m-1])