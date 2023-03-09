from collections import deque

n = int(input())

for i in range(n):

    a, b = map(int, input().split())
    graph = []
    for i in range(a):
        p = list(input())
        graph.append(p)

    total = 0

    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    check = [[False] * b] * a

    def bfs(x1, y1):

        que = deque()
        que.append([x1, y1])
        graph[x1][y1] = '.'

        while que:
            x, y = que.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < a and 0 <= ny < b:
                    if graph[nx][ny] == '#':
                        que.append([nx, ny])
                        graph[nx][ny] = '.'

    for i in range(a):
        for j in range(b):
            if graph[i][j] == '#':

                bfs(i, j)
                total += 1

    print(total)