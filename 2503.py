n = int(input())

arr = []

poss = [str(i) for i in range(1, 10)]
check = [False] * 9

randomNum = []

tmp = []
def back(depth):

    global tmp
    global randomNum
    if depth == 3:
        randomNum.append(''.join(tmp))
        return

    for i in range(len(poss)):
        if check[i]:
            continue

        tmp.append(poss[i])
        check[i] = True
        back(depth + 1)
        tmp.pop()
        check[i] = False
back(0)

find = dict()
for i in range(n):
    a, b, c = map(int, input().split())
    a = list(str(a))

    for i in randomNum:
        bb = 0
        cc = 0
        i = list(i)

        for k in range(3):
            if i[k] == a[k]:
                bb += 1
            if i[k] != a[k] and a[k] in i:
                cc += 1

        #print( ''.join(i), bb, b, cc , c)

        if bb == b and cc == c:
            if ''.join(i) not in find:
                find[''.join(i)] = 1
            else:
                find[''.join(i)] += 1

cnt = 0
for key in find:
    if find[key] == n:
        cnt += 1

print(cnt)