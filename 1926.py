import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

n, m = map(int, input().split())

graph = []
for i in range(n):
    x = list(map(int, input().split()))
    graph.append(x)

dx = [-1,1,0,0]
dy = [0,0,-1,1]



def dfs(x, y):
    global cnt
    cnt += 1
    graph[x][y] = 0

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if -1 < nx < n and -1 < ny < m and graph[nx][ny] == 1:
            dfs(nx, ny)

ans = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            cnt = 0
            dfs(i, j)
            ans.append(cnt)
print(len(ans))
ans.sort(reverse=True)
if len(ans) == 0:
    print(0)
else:
    print(ans[0])
