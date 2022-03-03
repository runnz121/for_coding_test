import sys

num = int(input())
x, y = map(int, input().split())

rel = int(input())

graph = [[] for _ in range(num+1)]

sys.setrecursionlimit(100000)

for i in range(rel):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (num + 1)
res = [0]*(num+1)


def dfs(start):
    visited[start] = True

    for i in graph[start]:
        if not visited[i]:
            res[i] = res[start] + 1
            dfs(i)
dfs(x)

if res[y] > 0:
    print(res[y])
else:
    print(-1)