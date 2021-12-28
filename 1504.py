import sys
input = sys.stdin.readline
import heapq

INF = int(1e9)
# 노드, 간선
N, E = map(int, input().split())
graph = [[] for _ in range(N+1)]
distance = [INF] * (N+1)

for i in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

print(graph)
# 반드시 거쳐야 함
x, y = map(int, input().split())

def dijkstra(start):
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue
        for i in graph[now]:
            print(i)
            cost = dist + i[0]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(1)

for i in range(1, N+1):
    if distance[i] == INF:
        print(-1)
    else:
        print(min(distance))