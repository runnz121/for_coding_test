import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

graph = []

sheep, wolf = 0, 0
for i in range(n):
    x = list(str(input()))

    for j in range(m):
        if x[j] == 'o':
            sheep += 1
        if x[j] == 'v':
            wolf += 1

    graph.append(x)

check = [[False] * m for _ in range(n)]



dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x1, y1):

    global sheep
    global wolf

    q = deque()

    sheep1, wolf1 = 0, 0

    q.append([x1, y1])
    if graph[x1][y1] == 'v':
        wolf1 += 1
    elif graph[x1][y1] == 'o':
        sheep1 += 1

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] != '#':
                if check[nx][ny]:
                    continue
                check[nx][ny] = True
                if graph[x1][y1] == 'v':
                    wolf1 += 1
                if graph[x1][y1] == 'o':
                    sheep1 += 1
                q.append([nx, ny])

    if sheep1 > wolf1:
        wolf -= wolf1
    else:
        sheep -= sheep1
    return

for i in range(n):
    for j in range(m):
        if (graph[i][j] == 'v' or graph[i][j] == 'o') and check[i][j] == False:
            check[i][j] = True
            bfs(i, j)

print(sheep, wolf)
