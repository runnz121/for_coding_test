

n, m = map(int, input().split())

graph = []
check = [[False] * m for _ in range(n)]

for i in range(n):
    graph.append(list(map(int, input().split())))

total = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            total += 1

def cctv1(x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    # 사각지대 갯수
    cnt = 0

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        tmp = 0
        while True:
            if 0 > nx or 0 > ny or nx >= n or ny >= m:
                break
            if graph[nx][ny] == 6:
                break

            if graph[nx][ny] == 0:
                tmp += 1
            else:
                tmp -= 1

            nx += dx[i]
            ny += dy[i]

        cnt = max(cnt, tmp)
    return cnt

def cctv2(x, y):
    #가로 추출
    tmp1 = 0
    d1 = graph[x]
    for i in d1:
        if i == 6:
            break
        if i == 0:
            tmp1 += 1
        else:
            tmp1 -= 1

    #세로 추출
    tmp2 = 0
    d2 = list(zip(*graph))[y]
    for i in d2:
        if i == 6:
            break
        if i == 0:
            tmp2 += 1
        else:
            tmp2 -= 1

    return max(tmp1, tmp2)

def cctv3(x, y):

    cnt = 0

    dx = [-1, 1, 1, -1]
    dy = [1, 1, -1, -1]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        tmp1 = 0
        tmp2 = 0

        while True:
            if 0 <= nx or nx < n:
                if graph[nx][y] == 0:
                    tmp1 += 1

            if 0 <= ny or ny < m:
                if graph[x][ny] == 0:
                    tmp2 += 1

            if 0 > nx and 0 > ny and nx >= n and ny >= m:
                break
        cnt = max(cnt, tmp1 + tmp2)
    return cnt

def cctv4(x, y):
    maxCnt = 0
    for i in range(4):
        d11 = x
        d22 = y
        if i == 0 or i == 2:
            d22 = x
        else:
            d11 = y
        # 가로 추출
        tmp1 = 0
        d1 = graph[d11]
        for i in d1:
            if i == 6:
                break
            if i == 0:
                tmp1 += 1
            else:
                tmp1 -= 1

        # 세로 추출
        tmp2 = 0
        d2 = list(zip(*graph))[d22][:d22]
        for i in d2:
            if i == 6:
                break
            if i == 0:
                tmp2 += 1
            else:
                tmp2 -= 1
        total = tmp2 + tmp1
        maxCnt = max(total, maxCnt)
    return maxCnt

def cctv5(x, y):

    # 가로 추출
    d1 = graph[x]

    tmp1 = 0

    for i in d1:
        if i == 6:
            break
        if i == 0:
            tmp1 += 1


    d2 = list(zip(*graph))[y]

    tmp2 = 0
    for i in d2:
        if i == 6:
            break

        if i == 0:
            tmp2 += 1

    return tmp1 + tmp2


blind = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            blind += cctv1(i, j)
        if graph[i][j] == 2:
            blind += cctv2(i, j)
        if graph[i][j] == 3:
            blind += cctv3(i, j)
        if graph[i][j] == 4:
            blind += cctv4(i, j)
        if graph[i][j] == 5:
            blind += cctv5(i, j)


print(total - blind)