a, b = map(int, input().split())
c, d = map(int, input().split())
e, f = map(int, input().split())
g, h = map(int, input().split())

maxx = 0

arr = []

arr.append(a)
arr.append(b)
arr.append(c)
arr.append(d)
arr.append(e)
arr.append(f)
arr.append(g)
arr.append(h)

sums = 0
for i in range(8):
    if i%2 == 1:
        sums += arr[i]
    else:
        sums -= arr[i]
    maxx = max(sums, maxx)

print(maxx)