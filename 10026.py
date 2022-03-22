import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
graph = []
graph_rg = []
color = ["R", "G", "B"]

score = {"R": 0, "G": 0, "B": 0}
score_rg = {"R": 0, "G": 0, "B": 0}

check = [[False] * n for _ in range(n)]
checkrg = [[False] * n for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(n):
    res = str(input().rstrip())
    graph.append(list(res))
    graph_rg.append(list(res))


for a in range(n):
    for b in range(n):
        if graph_rg[a][b] == 'G':
            graph_rg[a][b] = 'R'

def bfs(x, y):
    if check[x][y]:
        return

    q = deque()
    q.append([x, y])

    the_color = graph[x][y]


    while q:
        a, b = q.popleft()

        check[a][b] = True

        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]

            if nx >= 0 and ny >= 0 and nx < n and ny < n:
                if graph[nx][ny] == the_color and check[nx][ny] == False:
                    check[nx][ny] = True
                    q.append([nx, ny])

    score[the_color] += 1

def bfs_rg(x, y):

    if checkrg[x][y]:
        return

    q = deque()
    q.append([x, y])

    the_color = graph_rg[x][y]

    while q:
        a, b = q.popleft()

        checkrg[a][b] = True

        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]

            if nx >= 0 and ny >= 0 and nx < n and ny < n:
                if graph_rg[nx][ny] == the_color and checkrg[nx][ny] == False:
                    checkrg[nx][ny] = True
                    q.append([nx, ny])

    score_rg[the_color] += 1



for k in range(3):
    for i in range(n):
        for j in range(n):
            if graph[i][j] == color[k]:
                bfs(i, j)
                bfs_rg(i, j)

#
# print(score)
# print(score_rg)

normal = 0
redgreen = 0
for key in score.keys():
    normal += score[key]
    redgreen += score_rg[key]


print(normal, redgreen)
