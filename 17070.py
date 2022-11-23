n = int(input())

arr = []
check = [[False for _ in range(n)] for _ in range(n)]

for i in range(n):
    x = list(map(int, input().split()))
    arr.append(x)

print(arr)