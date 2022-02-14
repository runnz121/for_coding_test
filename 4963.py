import sys
from collections import deque

input = sys.stdin.readline


def bfs(x, y):
    que = deque()
    que.append([x, y])

    dx = [1, -1, 0, 0, 1, -1, 1, -1]
    dy = [0, 0, -1, 1, -1, -1, 1, 1]

    graph[x][y] = 0

    while que:
        x, y = que.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < b and 0 <= ny < a:
                if graph[nx][ny] == 1:
                    graph[nx][ny] = 0
                    que.append([nx, ny])



while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    graph = []
    cnt = 0

    for i in range(b):
        graph.append(list(map(int, input().split())))

    for i in range(b):
        for j in range(a):
            if graph[i][j] == 1:
                bfs(i, j) # -> 여기서 기존 bfs를 통해 graph값을 변경시킴
                cnt += 1 # 처음 있는 1의 갯수를 새는게 아니라 -> 변경된 값을 다시 세게됨
    print(cnt)

