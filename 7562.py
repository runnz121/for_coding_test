from collections import deque
t = int(input())

for i in range(t):

    line = int(input())

    x, y = map(int, input().split())
    px, py = map(int, input().split())

    graph = [[0] * line for _ in range(line)]
    que = deque()

    que.append([x, y])

    def bfs():

        dx = [-2,-2,-1,-1,1,1,2,2]
        dy = [-1,1,-2,2,-2,2,-1,1]


        while que:
            a, b = que.popleft()
            if a == px and b == py:
                break

            for i in range(8):
                nx = a + dx[i]
                ny = b + dy[i]

                if nx < 0 or ny < 0 or nx >= line or ny >= line:
                    continue

                if graph[nx][ny] == 1:
                    continue

                if graph[nx][ny] == 0:
                    graph[nx][ny] = graph[a][b] + 1
                    que.append([nx, ny])

        return graph[px][py]

    print(bfs())
