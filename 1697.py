from collections import deque
n, k = map(int, input().split())

graph = [0] * 100001

def bfs():
    que = deque()
    que.append(n)

    while que:
        p = que.popleft()

        # 큐에서 나온 숫자와 지정한 숫자가 같으면
        # 그래프의 값을 출력하고 종료
        if p == k:
            print(graph[p])
            break

        #문제 조건
        dx = [p + 1, p - 1, 2 * p]

        for i in range(3):
            nx = dx[i]

            if 0 <= nx <= 100000 and not graph[nx]:
                # print(nx)

                # 해당 인덱스가 0 이면
                # 해당 인덱스 값을 1증가시키고
                # 큐에 넣음
                if graph[nx] == 0:
                    graph[nx] = graph[p] + 1
                    que.append(nx)

bfs()