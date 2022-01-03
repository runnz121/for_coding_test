from collections import deque

a, b = map(int, input().split())

graph = [[] for _ in range(a)]

for i in range(a):
    graph[i] = list(map(int, input()))

visb = [[False] * b for _ in range(a)]

ans = []

def bfs(x, y):
    # 상하좌우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    #큐생성후 시작지점 넣기
    que = deque()
    que.append([x,y])

    #큐 존재시
    while que:
        x, y = que.popleft()

        #4방향 탐색
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            #범위넘어가면 패스
            if nx < 0 or nx >= a or ny < 0 or ny >= b:
                continue
            # 해당 위치값이 0인 경우 패스
            if graph[nx][ny] == 0:
                continue
            # 해당위차값이 1인 경우 길을 지나가는 곳임으로
            if graph[nx][ny] == 1:
                # print(graph)
                # 해당 값에다가 1을 더해줌
                graph[nx][ny] = graph[x][y] + 1

                que.append([nx, ny])

    #
    return graph[a-1][b-1]

print(bfs(0,0))


