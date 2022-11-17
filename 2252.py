from collections import deque
import sys
input = sys.stdin.readline

# 사람수 = 노드, 키비교횟수 = 간선갯수
n, m = map(int, input().split())

# 진입차수
indegree = [0] * (n + 1)

graph = [[] for i in range(n + 1)]


for i in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    indegree[y] += 1

res = []
que = deque()

# 진입차수가 0인 것을 큐에 넣음
for i in range(1, n + 1):
    if indegree[i] == 0:
        que.append(i)

while que:
    now = que.popleft()
    res.append(now)
    for i in graph[now]:
        indegree[i] -= 1
        if indegree[i] == 0:
            que.append(i)

# def topology(find):
#     q = deque()
#     q.append(find)
#     global res
#     while q:
#         now = q.popleft()
#         res.append(now)
#
#         for i in graph[now]:
#             indegree[i] -= 1
#
#             if indegree[i] == 0:
#                 q.append(i)
#
#
#         topology(i)


print(*res)
