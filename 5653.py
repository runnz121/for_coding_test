n = int(input())

arr = []
for i in range(n):
    x = list(map(str, input().split()))

    arr.append(x)

arr = sorted(arr, key = lambda x : (int(x[3]), int(x[2]), int(x[1])))

print(arr[n-1][0])
print(arr[0][0])