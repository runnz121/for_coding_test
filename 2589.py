import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())

arr = []
for i in range(n):
    x = list(str(input()))
    arr.append(x)

dx = [-1, 1, 0, 0]
dy = [0,0,1,-1]

def bfs(cost, x, y):
    check = [[0] * m for _ in range(n)]
    check[x][y] = 1
    q = deque()
    q.append([cost, x, y])
    longest = 0
    while q:
        cost, x1, y1 = q.popleft()
        longest = max(longest, cost)
        for i in range(4):
            nx = x1 + dx[i]
            ny = y1 + dy[i]

            if 0 <= nx < n and 0 <= ny < m and check[nx][ny] == 0 and arr[nx][ny] == 'L':
                q.append([cost + 1, nx, ny])
                check[nx][ny] = 1
    return longest


max_dist = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == 'L':
            dist = bfs(0, i, j)
            max_dist = max(dist, max_dist)

print(max_dist)