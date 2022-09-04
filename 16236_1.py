from collections import deque
import sys
input = sys.stdin.readline
n = int(input())

graph = []

for i in range(n):
    arr = list(map(int, input().split()))
    graph.append(arr)

shark_loc = []
shark_big = 2
shark_need = 0
shark_time = 0
eat = 0
food = []
#
# print(graph)

# 상어 위치 갱신
def shark_location():
    global shark_loc
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 9:
                shark_loc = [i,j]
                break

# 모든 먹이 찾기(현재 상어 크기와 비교해서 작은 것들만 담음)
def find_all_food():
    global food
    for i in range(n):
        for j in range(n):
            if 0 < graph[i][j] < 7:
                if graph[i][j] < shark_big:
                    dist = bfs(i,shark_loc[0],j,shark_loc[1])
                    tmp = [graph[i][j], i,j, dist] # 먹이 크기, 먹이 위치(x, y), 현재 상어 위치와의 거리
                    food.append(tmp)
    #print("inner", food)

def bfs(i, x, j, y): # 그래프 x, 상어 x , 그래프 y, 상어 y

    global graph
    global shark_big
    check = [[0] * n for _ in range(n)]

    min_dist = int(1e9)
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    que = deque()
    que.append([x,y])

    check[x][y] = 1

    while que:
        k = que.popleft()
        if k[0] == i and k[1] == j:
            min_dist = min(check[i][j]-1, min_dist)

        for p in range(4):
            nx = k[0] + dx[p]
            ny = k[1] + dy[p]

            if 0 <= nx < n and 0 <= ny < n:
                if check[nx][ny] == 0:
                    if graph[nx][ny] <= shark_big:
                        check[nx][ny] = check[k[0]][k[1]] + 1
                        que.append([nx, ny])
    if check[i][j] == 0:
        graph[i][j] = -1
    #print('check',check)
   # print('min_dist', min_dist)
    if min_dist > 0:
        min_dist = min(check[i][j], min_dist)
        #print("if min_dist", min_dist)
    else:
        min_dist = 0
    return min_dist


# 먹이 위치 비교(1:가장 가까운 위치 , 2:가장 위에 있는 물고기, 3:가장 왼쪽에 있는 물고기
def select_shortest():
    global food

    # food 거리, x, y 순서
    food = sorted(food, key = lambda x :(x[3], x[1], x[2]))


# 상어 위치 이동
def move_shark(foods):
    global shark_loc
    global shark_big
    global shark_need
    global shark_time
    global graph

    if len(foods) >= 1:
        if foods[0][3] > 0:
            # 샤크 위치 갱신
            graph[shark_loc[0]][shark_loc[1]] = 0
            shark_loc = [foods[0][1], foods[0][2]]
            # 샤크 필요 충족
            shark_need += 1
            # 샤크크기 충족
            if shark_need == shark_big:
                shark_need = 0
                shark_big += 1

            # 샤크 최소시간증가
            shark_time += foods[0][3]
            # 먹은 먹이 9 처리
            graph[foods[0][1]][foods[0][2]] = 9


def main():
    # 처음 상어 위치 갱신
    shark_location()
    global food

    while True:
        food = []
        # print(shark_big)

        # 먹이 갱신
        find_all_food()

        # print(food)
        # print('loc', shark_loc)
        # 해당되는 먹이가 없는 경우 엄마 소환!
        if len(food) == 0:
            print(shark_time)
            exit()

        # 먹이위치 비교
        select_shortest()


        # 상어 위치 이동
        move_shark(food)
        # print(graph)
        # print ('shark_need',shark_need)
        # print("sharktime" , shark_time)

main()

# 반례
#https://www.acmicpc.net/board/view/73362

