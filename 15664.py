

n, m = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()

res = []
tmp = []
check = [False] * n


def back(depth, start):

    if depth == m:
        print(*tmp)
        return
    duple = 0
    for i in range(start, n):
        if not check[i] and duple != arr[i]:
            check[i] = True
            tmp.append(arr[i])
            duple = arr[i]
            back(depth + 1, i)
            check[i] = False
            tmp.pop()



back(0, 0)

