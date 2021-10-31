from collections import deque

n, k = map(int, input().split())

graph = [] #전체 정보 담는 리스트
data = [] #바이러스 정보 담는 리스트

for i in range(n):
    #보드 정보를 한줄 단위로 입력
    graph.append(list(map(int, input().split())))
    for j in range(n):
        #해당 위치에 바이러스가 있으면,
        if graph[i][j] != 0:
            #바이러스 종류, 시간, 위치(x, y) 삽입
            data.append((graph[i][j], 0, i, j))

data.sort() #바이러스 번호 낮은순서대로 정렬
q = deque(data)
print(data)

ts, tx, ty = map(int, input().split())

dx = [-1,0,1,0]
dy = [0,1,0,-1]

while q:
    virus, s, x, y = q.popleft()

    #주어진시간이랑 큐에서 꺼낸 시간이랑 같을 경우
    if s == ts:
        break

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx and nx < n and 0 <= ny and ny < n:
            #아직 방문하지 않았다면 바이러스 넣기
            if graph[nx][ny] == 0:
                graph[nx][ny] = virus
                q.append((virus, s+1, nx, ny))



print(graph[tx-1][ty-1])