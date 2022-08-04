db = dict()

for i in range(8):
    x = int(input())
    db[i] = x

res = sorted(db.items(), key = lambda x : x[1], reverse=True)

ans = []
sums = 0
for k in range(len(res)-3):
    sums += res[k][1]
    ans.append(res[k][0] + 1)
ans.sort()
print(sums)
print(*ans)