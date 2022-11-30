t = int(input())

db = dict()
for i in range(t):
    name, status = map(str, input().split())
    if status == 'enter':
        db[name] = 1
    else:
        db[name] -= 1

ans = []
for key, value in db.items():
    if value == 1:
        ans.append(key)

ans.sort(reverse=True)

for i in ans:
    print(i)
