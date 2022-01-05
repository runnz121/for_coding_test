n = int(input())

arr = []

for i in range(n):
    arr.append(int(input()))

arr.sort()

max_val = int(-1e9)

for i in range(n):
    if max_val < arr[i]*(n-i):
        max_val = arr[i] * (n-i)
    # print(arr[i]*(n-i))

print(max_val)