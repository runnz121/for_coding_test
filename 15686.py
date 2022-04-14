from collections import deque

xx, yy = map(int, input().split())

INF = int(1e9)

left = 0

graph = []
dp = [[INF] * xx for _ in range(xx)]


for i in range(xx):
    graph.append(list(map(int, input().split())))

for xxx in range(xx):
    for yyy in range(xx):
        if graph[xxx][yyy] == 2:
            left += 1

left = yy - left


def bfs(x, y, left):

    q = deque()

    q.append([x,y])

    # 1 = 집
    # 2 = 치킨
    check = [[False] * xx for _ in range(xx)]
    print(check)

    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    check[x][y] = True

    while q:
        a, b = q.popleft()

        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]

            if 0 <= nx < x and 0 <= ny < x:
                print(nx, ny)

                if not check[nx][ny] and graph[nx][ny] == 2 and left > 0:
                    dp[x][y] = min(dp[x][y], abs(nx - x) + abs(ny - y))
                    q.append([nx, ny])
                    check[nx][ny] = Trues
                    left -= 1

for a in range(xx):
    for b in range(xx):
        if graph[a][b] == 1:
            #print(a, b)
            bfs(a, b, left)

print(dp)