import heapq
import sys
from collections import Counter
input = sys.stdin.readline
INF = int(1e9)

def solution(n, edge):
    answer = 0

    begin = 1

    # 노드 갯수
    n
    # 간선 갯수
    ver = len(edge)

    #2차원 리스트 생성
    graph = [[] * (n+1) for _ in range(n+1)]

    #최단 거리 테이블 초기화
    distance = [INF] * (n + 1)

    #간선 정보 입력 받기(배열을 graph로)
    for i in range(ver):
        x, y = edge[i][0], edge[i][1]
        #print(x, y)
        graph[x].append((y ,1))
        graph[y].append((x, 1))

    #print(graph) [[], [(3, 1), (2, 1)], [(4, 1)], [(6, 1), (2, 1)], [(3, 1)], [(2, 1)], []]

    # 다익스트라
    def dijkstra(start):
        q = []
        #시작노드 가기 위한 최단경로를 0으로 설정
        heapq.heappush(q, (0, start))
        distance[start] = 0

        while q:
            # 가장 최단거리가 짧은 노드 꺼내기

            # 거리길이, 현재 노드번호(처음은 -> 0,1)
            dist, now = heapq.heappop(q)

            # 현재 노드가 이미 처리되었다면 무시
            # 왜냐면 이미 최소값으로 설정되어있을 것이기 때문에
            if distance[now] < dist:
                continue

            # 현재 노드와 연결된 다르 노드 확인
            for i in graph[now]:
           #     print("i", i)
                cost = dist + i[1] # 여기서 현재 노드의 거리에서 지정된 노드의 거리로 가는데 드는 비용
                #print(cost)

                # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
                # 최단거리테이블에서 해당 노드의 최단거리를 갱신
                if cost < distance[i[0]]: # distance[3] = 1
                    distance[i[0]] = cost
                    heapq.heappush(q, (cost, i[0])) # 갱신된 것을 다시 큐에 넣어줌

    dijkstra(begin)

    ans = []
    for k in distance:
        if k != INF:
            ans.append(k)

    maxes = max(ans)

    answer = ans.count(maxes)

    #print(answer)
    #print(distance)
    return answer


n = 6
vertex = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
solution(n, vertex)