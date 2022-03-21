from collections import deque
import sys

input = sys.stdin.readline
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs():
    q = deque()
    q.append([0,0,1])
    visit =[[[0] * 2 for i in range(m)] for i in range(n)]
    visit[0][0][1] = 1
    #print(visit)
    while q:
        a, b, w = q.popleft()

        # 주어진 위치에 도착했을시 결과값을 반환
        if a == n - 1 and b == m - 1:
            return visit[a][b][w]

        # 4방향 탐색
        for i in range(4):
            x = a + dx[i]
            y = b + dy[i]

            # 범위 조건
            if 0 <= x < n and 0 <= y < m:

                # 벽을 뚫을 수 있고 길이 막혀 있는 경우(w가 1이면 아직 벽 뚫는 기회를 안씀)
                if s[x][y] == 1 and w == 1:
                    # 해당 부분을 1 로 처리하고 누적합 처리함
                    visit[x][y][0] = visit[a][b][1] + 1
                    q.append([x,y,0])
    

                    # 그게 아니라면 그냥 누적합만 처리함(w가 0이면 벽 뚫는 기회를 씀)
                elif s[x][y] == 0 and visit[x][y][w] == 0:
                    visit[x][y][w] = visit[a][b][w] + 1
                    q.append([x,y,w])
    return -1

n, m = map(int, input().split())
s = []
for i in range(n):
    s.append(list(map(int, list(input().strip()))))
print(bfs())