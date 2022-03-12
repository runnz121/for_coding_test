INF = int(1e9)

x, y = map(int, input().split())

graph = [[INF] * (x + 1) for _ in range(x + 1)]

# 자기자신 초기화
for a in range(1, x+1):
    for b in range(1, x + 1):
        if a == b:
            graph[a][b] = 0

# 최단거리테이블 초기화
for _ in range(y):
    a, b, c = map(int, input().split())
    graph[a][b] = c


# 거쳐가는것과, 직접 가는것 비교
for k in range(1, x + 1): # 거처가는 부분
    for a in range(1, x + 1):
        for b in range(1, x + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

#
# print(graph)

mins = INF

for x in range(1, x + 1):
    for y in range(1, x + 1):
        if graph[x][y] != 0 and graph[x][y] != INF:
            if graph[y][x] != 0 and graph[y][x] != INF:
                mins = min(mins, graph[y][x] + graph[x][y])

if mins == INF:
    print(-1)
else:
    print(mins)