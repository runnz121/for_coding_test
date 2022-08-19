import heapq

n = int(input())
m = int(input())

INF = int(1e9)

graph = [[] for i in range(n + 1)]

distance = [INF] * (n + 1)

for i in range(m):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])

# x가 시작 노드
x, y = map(int, input().split())


def dijkstra(start):
    q = []

    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        # 처음 0, start(노드) 들어감
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
dijkstra(x)

print(distance[y])