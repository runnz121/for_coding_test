from collections import deque
t = int(input())

def bfs(graph, x, y, m, n):
    flag = 0
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    graph[x][y] = 0

    que = deque()
    que.append([x,y])

    while que:

        x, y = que.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= m or ny >= n:
                continue

            if graph[nx][ny] == 0:
                continue

            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                que.append([nx, ny])
                flag = 1
    return flag


m, n, k = map(int, input().split())

graph = [[0]*m for _ in range(n)]

for i in range(k):
    a, b = map(int, input().split())
    graph[b][a] = 1

ans = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            ans.append(bfs(graph, i, j, m, n))
            print("infi")
