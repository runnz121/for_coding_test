n = int(input())

rank = 0
arr = []
for i in range(n):
    x = int(input())
    arr.append(x)

arr.sort()

ans = 0

for k in arr:
    rank += 1
    un = k - rank

    ans += abs(un)

print(ans)