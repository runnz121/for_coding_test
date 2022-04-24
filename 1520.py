from collections import deque

a, b = map(int, input().split())

graph = []
check = [[False] * b for _ in range(a)]

for i in range(a):
    graph.append(list(map(int, input().split())))

ans = 0
sample = 0

def bfs(xx, yy, pree):

    q = deque()

    global ans

    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    check[xx][yy] = True
    q.append([xx, yy, pree])

    while q:
        x, y, pre = q.popleft()

        if x - 1 == a and y - 1 == b:
            ans += 1

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < a and 0 <= nx < b:
                if check[nx][ny] == False:
                    if graph[nx][ny] < pre:
                        check[nx][ny] = True
                        q.append([nx, ny, graph[nx][ny]])

bfs(0,0, graph[0][0])

print(ans)
print(sample)