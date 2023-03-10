n = int(input())

arr = []

for i in range(n):
    x = list(map(str, input().split('.')))
    arr.append(x)

db = dict()

for idx in arr:
    if idx[1] in db:
        db[idx[1]] += 1
    else:
        db[idx[1]] = 1

db = sorted(db.items(), key = lambda x : x[0])

for key, value in db:
    print(key , value)