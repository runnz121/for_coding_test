from collections import deque

graph = []

for i in range(5):
    x = list(str(input()))
    graph.append(x)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


# 7명 확인
def checkLength(arr):
    if len(arr) < 7:
        return True
    return False


# 이다솜 더 많은지 확인
def checkMoreIdasom(arr):
    count = 0
    for p in arr:
        if p == 'S':
            count += 1
    if count >= 4:
        return True
    return False

def back(depth):






# dfs 탐색
# def dfs(x, y, check):
#     check[x][y] = True
#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]
#         if 0 <= nx < 5 and 0 <= ny < 5 and check[nx ][ny] == False:
#             if checkLength(tmp_arr):
#                 tmp_arr.append(graph[nx][ny])
#                 dfs(nx, ny, check)
#                 check[nx][ny] = False
#                 tmp_arr.pop()
#             print(tmp_arr)
#             return tmp_arr

# bfs 탐색
def bfs(x, y):
    check = [[False] * 5 for _ in range(5)]
    check[x][y] = True

    que = deque()
    que.append(x, y)

    while que:

        x, y = que.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < 5 and 0 <= ny < 5 and check[nx][ny] == False:
                check[nx][ny] = True
                que.append([nx, ny])

result = 0
for i in range(5):
    for j in range(5):

        tmp_arr = []
        dfs(i, j, check)
        if checkMoreIdasom(tmp_arr):
            result += 1

print(result)
