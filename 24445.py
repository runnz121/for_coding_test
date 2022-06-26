from collections import deque

n, m, r = map(int, input().split())

check = [False] * (n + 1)

graph = [[] for _ in range(n + 1)]

for i in range(n):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

ans = [0] * (n + 1)


def bfs(start):
    cnt = 0
    queue = deque()
    queue.append(start)
    check[start] = True

    while queue:
        v = queue.popleft()
        graph[v].sort(reverse=True)
        cnt += 1
        ans[v] = cnt

        for k in graph[v]:
            if not check[k]:
                check[k] = True
                queue.append(k)


bfs(r)

for i in range(1, len(ans)):
    print(ans[i])
