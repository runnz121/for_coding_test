from collections import deque
import sys
sys.setrecursionlimit(10000) # 메모리 초과로 인해 제한
# 보드
line = int(input())
board = [[0] * line for _ in range(line)]

# 사과위치
app = int(input())
for i in range(app):
    # 사과 위치 초기화
    app_w = list(map(int, input().split()))
    a = app_w[0]
    b = app_w[1]
    board[a-1][b-1] = 1 # 사과 입력 위치는 -1씩 해줘야된다

# 뱀방향
dir = int(input())
dir_w = deque()
for i in range(dir):
    dir_w.append(list(map(str, input().split())))

# 뱀이 차지하는 공간
snake = deque()
snake.append([0, 0])

# 오른,아래,위,왼쪽
dx = [0, 1, -1, 0]  # 상하
dy = [1, 0, 0, -1]  # 좌우

cnt = 0
# 사과체크 함수
def apple(nx, ny):
    if board[nx][ny] == 1:
        board[nx][ny] = 0 # 사과 먹으면 없애줌
        return False  # 사과가 존재하면 안줄여도 됨
    return True

# 1. 자기몸에 부딫치는지,
# 2. 벽에 부딫치는지
def check(nx, ny, snake1):

    if [nx, ny] in snake1:
       # print("check", nx, ny)
        return 2
    if nx >= line or nx < 0 or ny >= line or ny < 0:
        return 2
    return 1

# flag 반환
def flags(dir_w, cnt, flag):

  #  print(dir_w, cnt)
    if len(dir_w) > 0:
        if int(dir_w[0][0]) == cnt:
            res = dir_w.popleft()
            if (res[1] == 'D' and flag == 2) or (res[1] == 'L' and flag == 1):
                return 0 # 오른쪽 이동
            elif (res[1] == 'D' and flag == 0) or (res[1] == 'L' and flag == 3):
                return 1 # 아래로 이동
            elif (res[1] == 'L' and flag == 0) or (res[1] == 'D' and flag == 3):
                return 2 # 위로 이동
            elif (res[1] == 'L' and flag == 2) or (res[1] == 'D' and flag == 1):
                return 3 # 왼쪽 이동
    return flag


# 이동함수
def move(x, y, cnt1, flag1):

    flag = flags(dir_w, cnt1, flag1)

    nx = x + dx[flag]
    ny = y + dy[flag]

    # print("first", nx, ny, snake, cnt1)

    if check(nx, ny, snake) == 2:
        return cnt1

    snake.appendleft([nx, ny])

    if apple(nx, ny):  # true일때 -> 사과가 없을때 -> 한칸 다시 줄여줌
        snake.pop()

    # if not apple(nx, ny):
    #    print("in apple ",nx, ny)

    cnt1 = cnt1 + 1

   # print(nx, ny,"snake",snake, "time",cnt1)

    return move(nx, ny, cnt1, flag)

print(move(0,0, cnt, 0)+1)


