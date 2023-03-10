n, m = map(int, input().split())


a = [list(map(int, list(input()))) for _ in range(n)]
b = [list(map(int, list(input()))) for _ in range(n)]


def revers(x, y):
    for i in range(x, x + 3):
        for j in range(y, y + 3):
            a[i][j] = 1 - a[i][j]

def check():
    for i in range(n):
        for j in range(m):
            if a[i][j] != b[i][j]:
                return False
    return True


count = 0

for i in range(n - 2):
    for j in range(m - 2):
        if a[i][j] != b[i][j]:
            revers(i, j)
            count += 1

if check():
    print(count)
else:
    print(-1)