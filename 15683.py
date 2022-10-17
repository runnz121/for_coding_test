import copy

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
direction = {
    1: [[0], [1], [2], [3]],
    2: [[0, 2], [1, 3]],
    3: [[0, 1], [1, 2], [2, 3], [3, 0]],
    4: [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]],
    5: [[0, 1, 2, 3]]
}  # cctv 종류에 따른 감시 방향


# 각각 방향을 보고 모두 더하는 식으로 구현해야 함 ...
def watch(x, y, direction, tmp):
    for d in direction:
        print(d)
        nx, ny = x, y
        # 이동할 수 없을 때까지 이동하면서 '#'으로 변경
        while True:
            nx += dx[d]
            ny += dy[d]
            if nx < 0 or nx >= N or ny < 0 or ny >= M or tmp[nx][ny] == 6:  # 이동 가능한 범위를 벗어나거나 벽이면 break
                break
            elif tmp[nx][ny] == 0:  # 빈칸이면 감시 구역으로 변경
                tmp[nx][ny] = '#'


def dfs(n, graph):
    global ans
    tmp = copy.deepcopy(graph)

    if n == len(cctv):
        count = 0  # 빈칸 개수
        for t in tmp:
            count += t.count(0)
        ans = min(ans, count)  # 사각지대 최소 크기를 구한다
        return

    x, y, c = cctv[n]
    # 해당 cctv의 종류에 따른 감시 구역을 구한다
    for d in direction[c]:
        #print(d)
        watch(x, y, d, tmp)
        dfs(n + 1, tmp)
        tmp = copy.deepcopy(graph)


cctv = []  # cctv 리스트
ans = 1e9  # 사각지대 크기

# cctv 찾기
for i in range(N):
    for j in range(M):
        if graph[i][j] != 0 and graph[i][j] != 6:
            cctv.append([i, j, graph[i][j]])  # x위치, y위치, cctv 종류

dfs(0, graph)
print(ans)