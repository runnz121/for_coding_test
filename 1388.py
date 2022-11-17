from collections import deque
n, m = map(int, input().split())

check = []
arr = []
arr_col = []
for i in range(n):
    arr.append(list(map(str, input().split())))
    check.append([False] * m)

for k in range(n):
    arr_col.append(list(arr[k][0]))


def check_row(x, y):
    cnt = 1
    while y < m:
        if arr_col[x][y] == '-':
            check[x][y] = True
            y += 1
        else:
            break
    return cnt

def check_col(x, y):
    cnt = 1
    while x < n:
        if arr_col[x][y] == '|':
            check[x][y] = True
            x += 1
        else:
            break
    return cnt


total = 0
for i in range(n):
    for j in range(m):
        if arr_col[i][j] == '-' and check[i][j] == False:
            total += check_row(i, j)
        elif arr_col[i][j] == '|' and check[i][j] == False:
            total += check_col(i, j)

print(total)