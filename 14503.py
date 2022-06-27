import sys

sys.setrecursionlimit(10**6)

n, m = map(int, input().split())
r, c, d = map(int, input().split())

arr = []
dist = [0, 1, 2, 3]

for i in range(n):
    x = list(map(int, input().split()))
    arr.append(x)

clean = 0

if arr[r][c] == 0:
    clean += 1

def find(x, y, d, cnt):
    global clean

    if x < 0 or y < 0 or x >= n or y >= m:
        print(clean)
        return

    if d == 0:
        if arr[x][y - 1] == 0:
            d = dist[0 - 1]
            clean += 1
            return x, y - 1, d, cnt
        else:
            d = dist[0 - 1]
            return x, y, d, cnt + 1

    elif d == 1:
        if arr[x - 1][y] == 0:
            d = dist[1 - 1]
            clean += 1
            return x - 1, y, d, cnt + 1
        else:
            d = dist[1 - 1]
            return x, y, d, cnt + 1

    elif d == 2:
        if arr[x][y + 1] == 0:
            d = dist[2 - 1]
            clean += 1
            return find(x, y + 1, d, cnt + 1)
        else:
            d = dist[2 - 1]
            return x, y, d, cnt + 1

    elif d == 3:
        if arr[x + 1][y] == 0:
            d = dist[3 - 1]
            clean += 1
            return x + 1, y, d, cnt + 1
        else:
            d = dist[3 - 1]
            return x, y, d, cnt + 1


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
cnt = 0
while True:
    x, y, dis, cnt1 = find(r, c, d, cnt)

    if cnt1 == 4:
        if check(x, y, dis) == -1:
            print(clean)
            break
        else:
            cnt1 -= 1
    if cnt > 5:
        print(clean)
        break

    r = x
    c = y
    d = dis
    cnt = cnt1