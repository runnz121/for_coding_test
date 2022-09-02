n = int(input())

arr = []

for i in range(n):
    x, y = map(int, input().split())
    arr.append([x,y])


arr.sort(key = lambda x:x[0])


maxx = -int(1e9)
maxSum = -int(1e9)
for i in arr:
    res = i[0] - i[1]
    if res > maxSum:
        maxx = i[0]
        maxSum = res

if maxSum < 0:
    print(0)
else:
    print(maxx)