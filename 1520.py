import sys

sys.setrecursionlimit(10 ** 6)

a, b = map(int, input().split())

graph = []
check = [[False] * b for _ in range(a)]

for i in range(a):
    graph.append(list(map(int, input().split())))

ans = 0
sample = 0

def dfs(x, y, pre):

    global ans
    global sample

    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    print(x, y)

    if x == a and y == b:
        ans += 1
        return

    check[x][y] = True

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < a and 0 <= nx < b:
            if check[nx][ny] == False:
                if graph[nx][ny] < pre:
                    check[nx][ny] = True
                    dfs(nx, ny, graph[nx][ny])

dfs(0,0, graph[0][0])

print(ans)
print(sample)