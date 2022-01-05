n = int(input())
from collections import deque

graph = [[]*n for _ in range(n)]

for i in range(n):
    graph[i] = list(map(int,input()))


def bfs(graph, x, y):
    count = 1
    # 들어온 좌표는 방문 처리하기 위해 0으로 변경
    graph[x][y] = 0

    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    que = deque()
    que.append([x,y])

    # 큐 존재시
    while que:
        x, y = que.popleft()

        # 4방향 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue

            if graph[nx][ny] == 0:
                continue

            # 해당 좌표가 1이라면 0으로 방문 처리하고 큐에다 다시 넣음
            # 그리고 갯수 1증가시킴
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                que.append([nx, ny])
                count += 1

    return count


# 방문 하면 0으로 변경됨으로 해당 마을을 다시 탐색할순 없음
# 따라서 한번의  BFS가 끝나면 더이상 확장이 불가능함
# graph의 해당 좌표가 1일 경우 bfs에 들어가는 거임
# 그리고 그 좌표 기준으로 bfs를 처리하는 거임
ans = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
           # print("마을 갯수")
            ans.append(bfs(graph,i,j))

ans.sort()
print(len(ans))
for i in range(len(ans)):
    print(ans[i])

#https://hongcoding.tistory.com/71