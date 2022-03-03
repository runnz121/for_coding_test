from collections import deque

num = int(input())
x, y = map(int, input().split())

rel = int(input())

graph = [[] for _ in range(num+1)]


for i in range(rel):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False for i in range(num + 1)]
res = [0] * (num + 1)

def bfs(start):
    que = deque()
    que.append(start)
    visited[start] = True

    while que:
        k = que.popleft()
        for i in graph[k]:
            if not visited[i]:
                que.append(i)
                res[i] = res[k] + 1 # 꺼낸 기준에서 1을 더해야됨 -> 한다리 건너서 왔다는 뜻이기 때문
                visited[i] = True
bfs(x)

print(graph)
print(res)
print(res[y])
