n, m = map(int, input().split())

INF = int(1e9)

graph = [[INF] * (n + 1) for _ in range(n + 1)]

# 자기 자신을 0처리
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1


for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])


ans = []
for x in graph:
    sums = 0
    for i in x:
        if i != INF:
            sums += i
    ans.append(sums)

mins = INF
for x in ans:
    if x != 0:
        if x < mins:
            mins = x

for i in range(len(ans)):
    if ans[i] == mins:
        print(i)
        exit()