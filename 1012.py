from collections import deque
t = int(input())

def bfs(graph, x, y, m, n):
    flag = 0
    # 4방향 처리
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

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue

            if graph[nx][ny] == 0:
                continue

            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                que.append([nx, ny])
                flag = 1
    return flag


while t > 0:
    m, n, k = map(int, input().split())

    graph = [[0]*m for _ in range(n)]

    for i in range(k):
        a, b = map(int, input().split())
        graph[b][a] = 1

    ans = []

    # 그래프에서 1일 경우에만 bfs 함수에 넣는다
    # 그러면 bfs가 그 지점부터 시작해서 bfs 함
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                ans.append(bfs(graph, i, j, m, n))

    print(len(ans))
    t -=1