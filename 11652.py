t = int(input())

db = dict()

for i in range(t):
    k = int(input())
    if k in db:
        db[k] += 1
    else:
        db[k] = 1

res = sorted(db.items(), key = lambda x: (-x[1],x[0]))
# print(res)
# res = sorted(res, key = lambda x:x[0])

print(res[0][0])