N = int(input())
apples = int(input())

graph = [[0] * N for _ in range(N)]

for i in range(apples):
    a, b = list(map(int, input().split()))
    graph[a][b] = 2  # 사과가 있는 위치2로 표시

dir = []
change = int(input())
for i in range(change):
    chan = list(input().split())
    dir.append((int(chan[0]), chan[1]))

# print(N, apples, dir[1][1], graph)


# 우, 하, 좌, 상->오른쪽 기준으로 회전하게 짬
dx = [1, 0, -1, 0]
dy = [0, 1, 0, 1]


# 시간을 입력받아 방향을 바꾸는 시간인지 체크
def timecheck(time):
    for direction in dir:
        if direction[0] == time:
            if direction[1] == 'D':
                return 1
            else:
                return -1
        else:
            return 0

time = 1
sneak = 1

def move(x, y, flag, beforex, beforey):
    global time
    global sneak
    graph[0][0] = 1

    # 꼬리 움직이기
    if flag != 1:
        graph[beforex][beforey] = 0

    # 함수 종료조건 벽에 닿을경우
    if x > N or y > N:
        return print(time)

    time += 1  # 시간 증가
    i = 0
    cmd_dir = timecheck(time)  # 매 초마다 바꾸는 방향인지 확인
    direction = i + cmd_dir

    if direction < 0:
        direction = 3

    # 뱀 이동
    nx = x + dx[direction]
    ny = y + dy[direction]

    if nx > N or ny > N:
        return print(time)
    else:
        # 자기몸을 만났을 경우 종료
        if graph[nx-1][ny-1] == 1:
            return print(time)

        # 사과가 있을 경우
        if graph[nx-1][ny-1] == 2:
            sneak += 1  # 길이증가
            graph[nx][ny] = 1  # 사과 없에주고 현재 몸이 있음을 표시 -> 머리부분
            flag = 1
        else:
            graph[nx-1][ny-1] = 1
            graph[x][y] = 0
            flag = -1
        move(nx, ny, flag, x, y)


move(0, 0, -1, 0, 0)