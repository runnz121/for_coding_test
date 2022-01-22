import sys
import heapq
input = sys.stdin.readline

INF = int(1e9)
T = int(input())



def dijkstra(start):
    q = []
    heapq.heappush(q,(0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for p in graph[now]:
            cost = dist + p[1]

            if cost < distance[p[0]]:
                distance[p[0]] = cost
                heapq.heappush(q, [cost, p[0]])


for i in range(T):
    n, m, t = map(int, input().split())
    s, g, h = map(int, input().split())

    graph = [[] for _ in range(n+1)]
    target = []

    distance = [INF] * (n + 1)

    for j in range(m):
        a, b, d = map(int, input().split())
        graph[a].append([b, d])
        graph[b].append([a, d])

    for k in range(t):
        target.append(int(input()))

    print(dijkstra(0))


