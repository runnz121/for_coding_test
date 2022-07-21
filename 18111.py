from collections import deque

N, M, B = map(int, input().split())

graph = []

time = 0
height = 0

for i in range(N):
    x = list(map(int, input().split()))
    graph.append(x)


def bfs():

    que = deque()

    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    while que:
        x, y = que.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx