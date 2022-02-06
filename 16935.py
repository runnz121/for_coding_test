n, m, t = map(int, input().split())

arr = [] * n

for i in range(n):
    arr.append(list(map(int, input().split())))

r = list(map(int, input().split()))
# r을 t번 적용한다


# arr[0][0] -> arr[0][7]

# 위 아래 변환
def logic1():
    global arr
    arr = arr[::-1]

# 좌 우 변환
def logic2():
    global arr
    for i in range(n):
        arr[i] = arr[i][::-1]

# 90도변 -> zip이 위에서 아래로 묶어서 이걸 맨 처음열로 반환 ->
# A = [1,2,3]
# B = [4,5,6]
# C = [7,8,9]
# 의 값은 (위에서 세로로 묶음이 1행에 출력됨)
# (1, 4, 7)
# (2, 5, 8)
# (3, 6, 9)

# 90도 오른쪽
def logic3():
    global arr,n,m
    n,m = m,n
    arrcp = [list(row)[::-1] for row in list(zip(*arr))]
    arr = arrcp

#90도 왼쪽
def logic4():
    global arr,n,m
    n,m = m,n
    arrcp = [list(row) for row in list(zip(*arr))[::-1]]
    arr = arrcp

def logic5():
    global arr
    arrcp = [[0] *m for _ in range(n)]
    halfn = n//2
    halfm = m//2

#   1 -> 2
    for i in range(halfn):
        for j in range(halfm):
            arrcp[i][halfm+j] = arr[i][j]

#   2 -> 3
    for i in range(halfn):
        for j in range(halfm, m):
            arrcp[halfn+i][j] = arr[i][j]

#   3 -> 4
    for i in range(halfn, n):
        for j in range(halfm, m):
            arrcp[i][j-halfm] = arr[i][j]

#   4 -> 1
    for i in range(halfn, n):
        for j in range(halfm):
            arrcp[i-halfn][j] = arr[i][j]

    # 배열 복사
    for i in range(n):
        for j in range(m):
            arr[i][j] = arrcp[i][j]

def logic6():
    global arr
    arrcp = [[0] * m for _ in range(n)]
    halfn = n // 2
    halfm = m // 2

#   1 -> 4
    for i in range(halfn):
        for j in range(halfm):
            arrcp[halfn+i][j] = arr[i][j]

#   4 -> 3
    for i in range(halfn,n):
        for j in range(halfm):
            arrcp[i][j + halfm] = arr[i][j]

#   3 -> 2
    for i in range(halfn, n):
        for j in range(halfm, m):
            arrcp[i-halfn][j] = arr[i][j]

#   2 -> 1
    for i in range(halfn):
        for j in range(halfm,m):
            arrcp[i][j-halfm] = arr[i][j]

    for i in range(n):
        for j in range(m):
            arr[i][j] = arrcp[i][j]

for t in r:
    if t == 1:
        logic1()
    elif t == 2:
        logic2()
    elif t == 3:
        logic3()
    elif t == 4:
        logic4()
    elif t == 5:
        logic5()
    elif t == 6:
        logic6()

for k in arr:
    print(*k)