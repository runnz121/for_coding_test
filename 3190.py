N = int(input())
apples = int(input())

graph = [[0]*N for _ in range(N)]

for i in range(apples):
    a,b = list(map(int,input().split()))
    graph[a][b] = 2 # 사과가 있는 위치2로 표시

dir = []
change = int(input())
for i in range(change):
    chan = list(input().split())
    dir.append((int(chan[0]), chan[1]))

#print(N, apples, dir[1][1], graph)


#우, 하, 좌, 상->오른쪽 기준으로 회전하게 짬
dx = [1,0,-1,0]
dy = [0,1,0,1]

def move(x,y):
    time = 0
    sneak = 1
    graph[0][0] = 1

    #함수 종료조건 벽에 닿을경우
    if x > N or y > N:
        return time

    time += 1 # 시간 증가
    i = 0
    cmd_dir = timecheck(time) #매 초마다 바꾸는 방향인지 확인
    direction = i + cmd_dir

    if direction < 0:
        direction = 3

    #뱀 이동
    nx = x + dx[direction]
    ny = y + dy[direction]

    #자기몸을 만났을 경우 종료
    if graph[nx][ny] == 1:
        return time

    #사과가 있을 경우
    if graph[nx][ny] == 2:
        sneak += 1 #길이증가
        graph[nx][ny] = 1 #사과 없에주고 현재 몸이 있음을 표시 -> 머리부분
    else:
        graph[nx][ny] = 1
        graph[x][y]= 0

    move(nx,ny)

#시간을 입력받아 방향을 바꾸는 시간인지 체크
def timecheck(time):
    for direction in dir:
        if direction[0] == time:
            if direction[1] == 'D':
                return 1
            else:
                return -1
        else:
            return 0