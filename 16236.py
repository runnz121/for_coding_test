from collections import deque

n = int(input())

graph = []

for i in range(n):
    graph.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 체크 배열
check = [[-1] * n for _ in range(n)]

# 물고기 위치 및 크기 확인
def check_fish(graph):
    fish = []
    for i in range(n):
        for j in range(n):
            if graph[i][j] != 0 and graph[i][j] != 9:
                fish.append([graph[i][j],[i,j]])
    return fish

# 아기상어 위치 확인
def check_shark(graph):
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 9:
                return [i, j]
    return

#물고기와 아기상어 위치 갱신 (-2면 상어가 먹은거)
def check_loc(fish, shark_big, shark_loc):
    que = deque(fish)

    while que:
        big, local = que.popleft()
        # graph 에서 벗어나는 경우
        if 0 > graph[local[x]][local[y]] or graph[local[x]][local[y]] <= n:
            continue
        # 자기보다 물고기가 작고, 아직 안먹었을 경우
        if big <= shark_big and check[local[x][local[y]]] != -2:
            # 거리계산
            dx = abs(local[x] - shark_loc[0])
            dy = abs(local[y] - shark_loc[1])
            dist = dx + dy
            # 현재 상어 위치와 먹이의 거리 갱신
            check[local[x]][local[y]] = dist


# 물고기 위치, 크기
fish = check_fish(graph)
# 아기상어 초기, 잔여 물고기
baby_init = [2, 2]
# 아기상어 초기 위치
baby_loc_init = check_shark(graph)


if fish == 0:
    print(0)
# else:
#     while fish > 0:
#         check_loc(graph)
