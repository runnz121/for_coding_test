n = int(input())

arr = []
for i in range(n):
    x = list(map(int, input().split()))
    arr.append(x)

arr = sorted(arr, key = lambda x : (x[0], x[1], x[2]))

for i in arr:
    print(*i)