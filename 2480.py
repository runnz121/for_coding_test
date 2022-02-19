from collections import Counter

arr = list(map(int, input().split()))

arr.sort()

if arr[0] == arr[1] == arr[2]:
    res = 10000 + arr[0]*1000
elif arr[0] == arr[1] or arr[1] == arr[2]:
    res = 1000 + arr[1] * 100
elif arr[0] != arr[1] != arr[2]:
    res = arr[2] * 100

print(res)