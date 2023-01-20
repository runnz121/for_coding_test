from collections import deque
n, m = map(int, input().split())

graph = []

for i in range(n):
    arr = list(map(int, input()))
    graph.append(arr)


dx = [-1,1,0,0]
dy = [0,0,-1,1]

def check_inner(check_list):

    under_line = check_list[n-1]
    for check in under_line:
        if check:
            return True
    return False

def bfs(x, y):

    check = [[False] * m for _ in range(n)]
    que = deque()
    que.append([x, y])
    check[x][y] = True

    while que:
        x, y = que.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0 and check[nx][ny] == False:
                check[nx][ny] = True
                que.append([nx, ny])

    return check_inner(check)



for i in range(m):
    if graph[0][i] == 0:
        res = bfs(0, i)
        if res:
            print("YES")
            exit(0)
print("NO")
exit(0)