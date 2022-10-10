from collections import deque

n, m, k = map(int, input().split())

graph = []

for i in range(n):
    tmp = [0] * m
    graph.append(tmp)

for i in range(k):
    x, y = map(int, input().split())
    graph[x-1][y-1] = 1


def checkClean():
    check = []
    for i in range(n):
        tmp1 = [False] * m
        check.append(tmp1)
    return check

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):

    cnt = 1
    check = checkClean()
    que = deque()
    que.append([x,y])
    check[x][y] = True

    while que:
        a, b = que.popleft()

        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 1:
                    if not check[nx][ny]:
                        cnt += 1
                        que.append([nx, ny])
                        check[nx][ny] = True
    return cnt


max_dump = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            max_dump = max(bfs(i, j), max_dump)

print(max_dump)