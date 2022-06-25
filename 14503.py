n, m = map(int, input().split())
r, c, d = map(int, input().split())

arr = []
dist = [0, 1, 2, 3]

for i in range(n):
    x = list(map(int, input().split()))
    arr.append(x)

cur = arr[r][c]


def find(x, y, d, cnt):
    global cur

    if d == 0:
        if arr[x][y - 1] == 0:
            d = dist[0 - 1]
            cur = [x][y - 1]
            arr[x][y - 1] = 0
            return [x, y - 1, d, cnt]
        else:
            d = dist[0 - 1]
            return [x, y, d, cnt + 1]

    elif d == 1:
        if arr[x - 1][y] == 0:
            d = dist[1 - 1]
            cur = [x - 1][y]
            arr[x - 1][y] = 0
            return [x - 1, y, d, cnt + 1]
        else:
            d = dist[1 - 1]
            return [x, y, d, cnt + 1]

    elif d == 2:
        if arr[x][y + 1] == 0:
            d = dist[2 - 1]
            cur = [x][y + 1]
            arr[x][y + 1] = 0
            return [x, y + 1, d, cnt + 1]
        else:
            d = dist[2 - 1]
            return [x, y, d, cnt + 1]

    elif d == 3:
        if arr[x + 1][y] == 0:
            d = dist[3 - 1]
            cur = [x + 1][y]
            arr[x + 1][y] = 0
            return [x + 1, y, d, cnt + 1]
        else:
            d = dist[3 - 1]
            return [x, y, d, cnt + 1]


def check(x, y, d):
    if d == 0:
        if arr[x + 1][y] == 1 or x + 1 >= n:
            return -1
        else:
            return 1

    elif d == 1:
        if arr[x][y - 1] == 1 or y - 1 < 0:
            return -1
        else:
            return 1

    elif d == 2:
        if arr[x - 1][y] == 1 or x - 1 < 0:
            return -1
        else:
            return 1

    elif d == 3:
        if arr[x][y + 1] == 1 or y + 1 >= m:
            return -1
        else:
            return 1


clean = 0
cnt = 1
while True:
    x, y, d, cnt = find(r, c, d, cnt)
    clean += 1
    if cnt == 4:
        if check(x, y, d) == 1:
            cnt -= 1
        else:
            print(clean)
        break
