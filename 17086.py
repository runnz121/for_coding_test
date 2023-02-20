from collections import deque

n, m = map(int, input().split())

graph = []

for i in range(n):
    x = list(map(int, input().split()))
    graph.append(x)

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, 1, 0, -1]


que = deque()

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            que.append([i, j])

while que:
    x1, y1 = que.popleft()
    for i in range(8):
        nx = x1 + dx[i]
        ny = y1 + dy[i]

        if 0 <= nx < n and 0 <= ny < m:
            if graph[nx][ny] == 0:
                graph[nx][ny] = graph[x1][y1] + 1
                que.append([nx, ny])

res = 0
for i in range(n):
    for j in range(m):
        res = max(res, graph[i][j])

print(res - 1)