import sys
input = sys.stdin.readline
import heapq

INF = int(1e9)
# 노드, 간선
N, E = map(int, input().split())
graph = [[] for _ in range(N+1)]

for i in range(E):
    a, b, c = map(int, input().split())
    # 서로 왕복임으로(무방향 서로 이어줌)
    graph[a].append((b, c))
    graph[b].append((a, c))

#print(graph)
# 반드시 거쳐야 함
v1, v2 = map(int, input().split())

def dijkstra(start):
    q = []
    # 거리 테이블을 매 계산마다 초기화 해줌
    # 그래야 각 경우에 대해서(아래 설명) 거리 테이블이 초기화 되기 때문
    distance = [INF] * (N + 1)
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue
        for i in graph[now]:
            #print(i)
            # 간선 가중치 값을 계산해야 함으로 1번째 원소값(0번은 해당 노드) 을 더해줘야됨
            cost = dist + i[1]
            if cost < distance[i[0]]: # 거리테이블의 해당 노드의 간선 가중치 값보다 작은 경우
                distance[i[0]] = cost # 최소값으로 갱신
                heapq.heappush(q, (cost, i[0]))
    return distance


one = dijkstra(1)
x = dijkstra(v1)
y = dijkstra(v2)
print(one, x, y)
print(one, x[N], y[N])
# 갈수 있는 방법은
# 1. 시작점 -> v1 -> v2 -> n
# 2. 시작점 -> v2 -> v1 -> n
# 이 두 가지 방법중 작은것을 출력

# 크게 보면
# 시작 -> v1 or v2
# v1 or v2 -> n
# 이다


# 정점의 도착지가 N (단순히 그냥 갯수와 같은것)
cnt = min(one[v1] + x[v2] + y[N], one[v2] + y[v1] + x[N])
print(cnt if cnt < INF else -1)