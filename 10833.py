n = int(input())

res = 0
for i in range(n):
    x, y = map(int, input().split())
    cnt = y // x
    y = y - (x * cnt)
    res += y
print(res)