x = int(input())

arr = list(map(int, input().split()))

tmp = []

res = []

ans = 0

check = [False] * x

def back(depth):

    global ans
    global answer

    if depth == x:
        res.append(sum(abs(tmp[i] - tmp[i + 1]) for i in range(x - 1)))
        return

    for i in range(x):
        if check[i]:
            continue
        tmp.append(arr[i])
        check[i] = True
        back(depth + 1)
        check[i] = False
        tmp.pop()
back(0)

print(max(res))