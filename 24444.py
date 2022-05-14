from collections import deque

n, m, r = map(int, input().split())

arr = [[] for _ in range(n+1)] # 정점 갯수 기준

for i in range(m): # 간선갯수만큼 받음
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

for i in arr:
    i.sort()

visited = [False] * (n+1) # 정점 갯수 기준
visited[0] = True


#print(arr)

que = deque()
que.append(r)
visited[r] = True

comp = [i+1 for i in range(n)] #정점갯수 기준
#print(comp)

ans = []
ans.append(r)
while que:
    out = que.popleft()

    for i in range(len(arr[out])):
        idx = arr[out][i]
        if not visited[idx]:
            ans.append(idx)
            visited[idx] = True
            que.append(idx)

for k in comp:
    if k not in ans:
        ans.insert(k-1, 0)

for k in ans:
    print(k)


#
# import sys
# from collections import deque
#
# input = sys.stdin.readline
#
#
# def bfs(start):
#     Cnt = 1
#
#     queue = deque([start])
#     visited[start] = Cnt
#
#     while queue:
#         v = queue.popleft()
#
#         for i in graph[v]:
#             if visited[i] == 0:
#                 Cnt += 1
#                 queue.append(i)
#                 visited[i] = Cnt
#
#
# N, M, R = map(int, input().split())
#
# graph = [[] for _ in range(N + 1)]
# visited = [0] * (N + 1)
#
# for _ in range(M):
#     A, B = map(int, input().split())
#     graph[A].append(B)
#     graph[B].append(A)
#
# for i in graph:
#     i.sort()
#
# bfs(R)
#
# for i in range(1, N + 1):
#     print(visited[i])

# 6 5 1
# 1 4
# 2 3
# 4 6
# 1 3
# 2 6
# 1
# 4
# 2
# 3
# 0
# 5


# 7 4 1
# 1 4
# 2 3
# 1 5
# 3 6
# 1
# 0
# 0
# 2
# 3
# 0
# 0