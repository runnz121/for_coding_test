import heapq
import sys

n, m = map(int, input().split())

graph = [[] * (n+1) for _ in range(m+1)]

INF = int(1e9)

# 노드 간선 입력 받기
for i in range(m):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])

distance = [INF] * (n+1)

start = 1

distance[start] = 0

for i in range(start+1, n+1):

    for j in graph[i]:
        print(j)
        distance[i] = min(distance[i-1] + j[1], j[1])

print(distance)