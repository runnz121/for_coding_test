n, m, r = map(int, input().split())
graph = [[] for _ in range(m + 1)]
for i in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
