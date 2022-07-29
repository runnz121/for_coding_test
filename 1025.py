n = int(input())

arr = []

for i in range(n):
    arr.append(int(input()))

if (arr[1] - arr[0]) == (arr[2] - arr[1]):
    x = arr[1] - arr[0]
    print(arr[n-1] + x)
else:
    x = arr[1] // arr[0]
    print(arr[n-1] * x)