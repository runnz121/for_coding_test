db = dict()

for i in range(1, 9):
    x = int(input())
    if x not in db:
        db[i] = x

res = sorted(db.items(), key = lambda x : x[1], reverse=True)

ans = []
sums = 0
for k in range(len(res)-3):
    sums += res[k][1]
    ans.append(res[k][0])
ans.sort()
print(sums)
print(*ans)