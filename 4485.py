import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dijkstra():
    q = []
    # 힙에 넣기
    heapq.heappush(q, (graph[0][0], 0, 0))

    # 거리 테이블 초기화
    distance[0][0] = 0

    while q:
        # 비용, x, y (비용 기준으로 가장 적은비용을 꺼냄)
        cost, x, y = heapq.heappop(q)

        # 출력
        if x == n - 1 and y == n - 1:
            print(f'Problem {count}: {distance[x][y]}')
            break

        # 4방향 탐색
        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]

            # 조건 필터링
            if 0 <= new_x < n and 0 <= new_y < n:

                # 새로운 비용 = 가장 적은 비용 + 현재 비용
                new_cost = cost + graph[new_x][new_y]

                # 새로 산출된 값이 기존 값보다 작은 경우
                if new_cost < distance[new_x][new_y]:
                    distance[new_x][new_y] = new_cost
                    heapq.heappush(q, (new_cost, new_x, new_y))
count = 1

while True:
    n = int(input())
    if n == 0:
        break

    # graph [[5, 5, 4], [3, 9, 1], [3, 2, 7]]
    graph = [list(map(int, input().split())) for _ in range(n)]

    distance = [[INF] * n for _ in range(n)]

    dijkstra()
    count += 1