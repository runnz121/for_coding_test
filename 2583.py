import sys
from collections import deque
input = sys.stdin.readline

m, n, k = map(int, input().split())

arr = []
answer = []
maps = [[0] * n for _ in range(m)]

for i in range(k):
    a, b, c, d = map(int, input().split())
    for x in range(b, d):
        for y in range(a, c):
            maps[x][y] = 1

#maps.reverse()

def bfs(xx, yy):
    que = deque()
    count = 1
    maps[xx][yy] = 1


    que.append([xx, yy])

    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    while que:
        x, y = que.popleft()
       # print(x, y)


        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < m and 0 <= ny < n:
                if maps[nx][ny] == 0:
                    count += 1
                    maps[nx][ny] = 1
                    que.append([nx, ny])

  #  print(count)
    return count

#print(maps)
for a in range(m):
    for b in range(n):
        if maps[a][b] == 0:
           # print(a,b)
            answer.append(bfs(a, b))
           # print(maps)
#print("here", maps)
answer.sort()
print(len(answer))
print(*answer)
