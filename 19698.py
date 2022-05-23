
arr = list(map(int, input().split()))

y = arr[1] // arr[3]
x = arr[2] // arr[3]

if arr[0] < x * y:
    print(arr[0])
else:
    print(x * y)