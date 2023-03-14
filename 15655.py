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

    for i in range(start, n):
        if not check[i]:
            tmp.append(arr[i])
            check[i] = True
            back(depth + 1, i)
            tmp.pop()
            check[i] = False


back(0, 0)
