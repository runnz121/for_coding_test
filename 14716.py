import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m = map(int, input().split())

graph = []

for i in range(n):
    x = list(map(int, input().split()))
    graph.append(x)

dx = [-1, 1, 0, 0, -1, 1, -1, 1]
dy = [0, 0, -1, 1, 1, -1, -1, 1]

word = 0

#check = [[False] * m for _ in range(n)]

def dfs(x, y):

    #check[x][y] = True
    graph[x][y] = -1

    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1:
            dfs(nx, ny)
            #check[nx][ny] = True
    return

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            dfs(i, j)
            word += 1

print(word)
