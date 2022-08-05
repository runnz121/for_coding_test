n = int(input())

arr =[]

mins = int(1e9)

for i in range(n):
    a, b = map(int, input().split())
    arr.append([a,b])

tot = []
tmp1 = []
tmp2 = []

check = [False] * n

def back(depth, end):

    global tot
    global tmp

    sums = 1
    mins = 0

    if depth == end:
        for i in range(len(tmp1)):
            sums *= tmp1[i]
            mins += tmp2[i]
        tot.append(abs(sums - mins))
        return

    for i in range(n):
        if check[i]:
            continue
        tmp1.append(arr[i][0])
        tmp2.append(arr[i][1])
        check[i] = True
        back(depth + 1, end)
        check[i] = False
        tmp1.pop()
        tmp2.pop()

for k in range(1, n+1):
    back(0, k)

print(min(tot))