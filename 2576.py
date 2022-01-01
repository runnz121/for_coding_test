arr = []
ans = []
for i in range(7):
    arr.append(int(input()))

arr.sort()

for i in arr:
    if i % 2 != 0:
        ans.append(i)

if len(ans) > 0:
    ans.sort()
    print(sum(ans))
    print(ans[0])
else:
    print(-1)