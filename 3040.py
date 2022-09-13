import copy

start = 9

arr = []

check = [False] * start

for i in range(start):
    x = int(input())
    arr.append(x)

tmp = []
ans = []
def back(depth, init):

    global tmp

    tmp1 = copy.deepcopy(tmp)

    if depth == 7:
        ans.append(tmp1)
        return

    for i in range(init, start):
        if check[i]:
            continue

        check[i] = True
        tmp.append(arr[i])
        back(depth + 1, i)
        check[i] = False
        tmp.pop()

back(0, 0)
#print(ans)

for k in ans:
    if sum(k) == 100:
        for i in k:
            print(i)
        break