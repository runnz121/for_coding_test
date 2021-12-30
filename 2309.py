from itertools import combinations

arr = []
ans = []

for i in range(9):
    arr.append(int(input()))

res = list(combinations(arr,7))

for i in res:
    i = list(i)
    i.sort()
    if sum(i) == 100:
        ans.append(i)
        break

for i in ans[0]:
    print(i)