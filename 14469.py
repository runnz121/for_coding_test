n = int(input())

arr = []
for i in range(n):
    x, y = map(int, input().split())
    arr.append([x, y])

arr.sort()

res = 0
for k in range(n):
    if res > arr[k][0]:
        res += arr[k][1]
    else:
        res = arr[k][0] + arr[k][1]

print(res)