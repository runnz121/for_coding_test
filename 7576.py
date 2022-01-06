from collections import deque

m, n = map(int, input().split())

graph = []

for i in range(n):
    graph.append(list(map(int, input().split())))

def bfs(graph, x, y, flag):
    day = []
    que = deque()
    check = deque()

    # 방문 처리용
    graph[x][y] = 1
    que.append([x,y])

    # 4방향 탐색
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    while que:
        x, y = que.popleft()
        cnt = 0

        # for i in range(4):
        #     nnx = x + dx[i]
        #     nny = y + dy[i]
        #     if graph[nnx][nny] == 0:
        #         print(nnx, nny)
        #         check.append((flag, nny, nnx))
        flag += 1


        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]



            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue

            if graph[nx][ny] == 1 or graph[nx][ny] == -1:
                continue

            if graph[nx][ny] == 0:
                cnt += 1
                graph[nx][ny] = 1
                check.append([nx, ny, flag])
                que.append([nx,ny])
                # print(que)
                print('check',check)

    return day

ans = []
flag = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            ans.append(bfs(graph, i, j, flag))

print(ans)


