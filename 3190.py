from collections import deque

#보드
line = int(input())
board = [[0] * line for _ in range(line)]

#사과위치
app = int(input())
for i in range(app):
    #사과 위치 초기화
    app_w = list(map(int, input().split()))
    a = app_w[0]
    b = app_w[1]
    board[a][b] = 1

#뱀방향
dir = int(input())
dir_w = deque()
for i in range(dir):
    dir_w.append(list(map(str, input().split())))


