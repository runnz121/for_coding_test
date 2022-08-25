n = int(input())

arr = []

for i in range(n):
    x = list(map(str, input().split(',')))
    arr.append(x)

for k in arr:
    print(int(k[0]) + int(k[1]))