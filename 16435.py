n, l = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()

length = l
for i in range(n):
    if arr[i] <= length:
        length += 1
    else:
        print(length)
        exit(0)
print(length)