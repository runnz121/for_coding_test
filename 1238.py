import heapq

INF = int(1e9)

n, m, x = map(int, input().split())

# node
node = [[] for _ in range(n + 1)]

for _ in range(m):
    x, y, z = map(int, input().split())
    node[x].append((y, z))

def dijkstra(start):
    q = []
    # distance
    distance = [INF] * (n + 1)

    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for idx, node_cost in node[now]:
            cost = node_cost + dist

            if distance[idx] > cost:
                distance[idx] = cost
                heapq.heappush(q, (cost, idx))

    return distance

res = 0
for i in range(1, n + 1):
    # 시작지점에서 시작
    go = dijkstra(i)
    # 도착지점에서 시작
    back = dijkstra(x)
    # 시작지점에서 출발해서 도착한 지점 + 도착지점일때 시작한 지점위치
    res = max(res, go[x] + back[i])

print(res)