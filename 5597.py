arr = []
for i in range(28):
    x = int(input())
    arr.append(x)

arr.sort()

ans = []

for i in range(1, 31):
    if i not in arr:
        ans.append(i)

ans.sort()

for x in ans:
    print(x)