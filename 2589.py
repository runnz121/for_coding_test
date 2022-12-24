from collections import deque

n, m = map(int, input().split())

arr = []
for i in range(n):
    x = list(str(input()))
    arr.append(x)

start = []
save = []

dx = [-1, 1, 0, 0]
dy = [0,0,-1,1]

def bfs(x, y):
    global start
    global save

    check = [[False for _ in range(m)] for _ in range(n)]
    check[x][y] = True
    q = deque()
    start.append([x, y])
    child = []
    dist = 0
    while q:
        x1, y1 = q.popleft()

        for i in range(4):
            nx = x1 + dx[i]
            ny = y1 + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if not check[nx][ny]:
                    if arr[nx][ny] == 'L':
                        dist += 1
                        q.append([nx, ny])
                        child.append([nx, ny, dist])
                        check[nx][ny] = True
                        print(nx, ny, dist)
    save.append(child)

for i in range(n):
    for j in range(m):
        if arr[i][j] == 'L':
            bfs(i, j)

print(start)
print(save)