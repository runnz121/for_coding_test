import sys
import heapq
input = sys.stdin.readline
#노드, 간선
n, m = map(int, input().split())
start = int(input())
INF = int(1e9)
#노드의 갯수
graph = [[] for _ in range(n+1)]

#거리테이블
distance = [INF] * (n+1)

#해당 노드를 기준으로 (도착노드, 간선 거리)를 대입
for i in range(m):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))

def dijkstra(start):
    q = []
    #시작지점은 0
    heapq.heappush(q, (0, start))
    distance[start] = 0

    #큐에 데이터가 있다면
    while q:
        dist, now = heapq.heappop(q)
        print(distance)

        if distance[now] < dist:
            print('A',distance[now], distance)
            continue
        for i in graph[now]:
            print('B',i, graph, dist, i[1])
            # 총 거리 비용 = 해당 노드까지의 비용(미리 저장된것) + 해당 노드까지 가는데 든 간선 값
            cost = dist + i[1]
            # 새로 계산한 해당 노드까지의 거리비용 < 현재 거리테이블의 해당 노드의 저장되어있는 값
            if cost < distance[i[0]]:
                # 새로 갱신
                distance[i[0]] = cost
                # 다시 힙에 넣음
                heapq.heappush(q, (cost, i[0]))
dijkstra(start)

for i in range(1, n+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])