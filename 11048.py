from collections import deque

n, m = map(int, input().split())

graph = []
dp = [[0] * m for _ in range(n)]
check = [[False] * m for _ in range(n)]

for i in range(n):
    listx = list(map(int, input().split()))
    graph.append(listx)

dp[0][0] = graph[0][0]

for i in range(n):
    for j in range(m):
        if i > 0 and j == 0:
            graph[i][j] = graph[i-1][j] + graph[i][j]

        if i == 0 and j > 0:
            graph[i][j] = max(graph[i][j-1] + graph[i][j], graph[i][j])

        if 0 <= i-1 < n and 0 <= j - 1 < m:
            graph[i][j] = max(graph[i-1][j] + graph[i][j], graph[i][j-1] + graph[i][j], graph[i-1][j-1] + graph[i][j], graph[i][j])
            check[i][j] = True
            #print(graph)


#print(graph)
print(graph[n-1][m-1])


#
# from collections import deque
#
# n, m = map(int, input().split())
#
# graph = []
# dp = [[0] * m for _ in range(n)]
# check = [[False] * m for _ in range(n)]
#
# for i in range(n):
#     listx = list(map(int, input().split()))
#     graph.append(listx)
#
# dp[0][0] = graph[0][0]
#
#
#
# def bfs(x, y):
#     q = deque()
#     q.append([x,y])
#     check[x][y] = True
#
#     dx = [1, 0, 1]
#     dy = [0, 1, 1]
#
#     while q:
#         a, b = q.popleft()
#
#         if a == n and b == m:
#             break
#
#         for i in range(3):
#             nx = a + dx[i]
#             ny = b + dy[i]
#            # print(nx, ny)
#
#             if 0 <= nx < n and 0 <= ny < m:
#                 if not check[nx][ny]:
#                     check[nx][ny] = True
#                 graph[nx][ny] = max(graph[x][y] + graph[nx][ny], graph[nx][ny])
#                 print(graph)
#                 q.append([nx, ny])
#
# bfs(0, 0)
#
# print(graph)
# print(graph[n-1][m-1])