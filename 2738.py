n, m = map(int, input().split())

arr1 = []
arr2 = []
arr3 = [[0] * m for _ in range(n)]

for i in range(n):
    arr1.append(list(map(int, input().split())))

for j in range(n):
    arr2.append(list(map(int, input().split())))

for i in range(n):
    for j in range(m):
        arr3[i][j] = arr1[i][j] + arr2[i][j]

for k in arr3:
    print(*k)