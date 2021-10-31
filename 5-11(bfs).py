from collections import deque

n,m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))


dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    queue = deque()
    queue.append((x,y))


    while queue:
        x, y = queue.popleft()
        #4방향 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue

            if graph[nx][ny] == 0:
                continue

            #처음 방문시에만 1로 기록한다
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y]+1
                queue.append((nx, ny))

    #가장 오른쪽 아래까지의 최단 거리반환
    return graph[n-1][m-1]

print(bfs(0,0))