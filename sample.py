import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

n, m, c = map(int, input().split())

graph = [[] for _ in range(n+1)]

#최단거리 테이블 무한으로 초기화
distance = [INF] * (n+1)

# 모든 간선 저옵 입력받기
for i in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y,z))


def dijkstra(start):
    q = []
    #시작 노드로 가기 위한 최단 경로는 0, 큐에 삽입
    heapq.heappush(q, (0,start))
    distance[start] = 0
    while q: # 큐에 존재시
        # 최단거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 다른 노드 확인
        for i in graph[now]:
            cost = dist + i[1]
        # 현재 노드를 거쳐서 다른 노드로 이동하는게 더 짧을 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(c)

count = 0
max_distance = 0
for d in distance:
    if d != INF:
        count += 1
        max_distance = max(max_distance, d)

print(count - 1, max_distance)