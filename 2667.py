n = int(input())
from collections import deque

graph = [[]*n for _ in range(n)]

for i in range(n):
    graph[i] = list(map(int,input()))

ans = [0] * n

def bfs(x, y):

    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    que = deque()
    que.append([x,y])

    while que:
        print("infi")
        x, y = que.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx <0 or nx >= n or ny < 0 or ny >= n:
                continue

            if graph[nx][ny] == 0:
                continue

            if graph[nx][ny] != 0:
                ans[graph[nx][ny]] += 1
                que.append([nx, ny])

    print("infi")
    return graph[nx-1][ny-1]

print(bfs(0,0))
print(ans)