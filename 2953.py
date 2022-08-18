arr = []

maxx = -int(1e9)

ans = []

for i in range(5):
    x = list(map(int, input().split()))
    tmp = sum(x)

    if tmp > maxx:
        maxx = tmp
        ans = [i + 1, tmp]

print(*ans)