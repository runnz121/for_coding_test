n = int(input())

arr = []
for i in range(n):
    x = list(map(int, input().split()))
    arr.append(x)

arr1 = sorted(arr, reverse = True, key = lambda x : x[2])

res = []
db = dict()
countryCnt = 0
for i in arr1:
    if i[0] not in db or db[i[0]] != 2:
        res.append(i)
        if i[0] not in db:
            db[i[0]] = 1
        else:
            db[i[0]] += 1
    else:
        continue
    if len(res) == 3:
        break

for x in res:
    print(x[0], x[1])