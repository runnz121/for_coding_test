import sys
import heapq

input = sys.stdin.readline

a, b = map(int, input().split())

INF = int(1e9)

distance = [INF] * (a + 1)

graph = [[] * (a + 1) for _ in range(a + 1)]

for _ in range(b):
    x, y, z = map(int, input().split())
    graph[x].append([y,z])

