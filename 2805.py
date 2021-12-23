a, b = map(int, input().split())

arr = list(map(int, input().split()))

arr.sort()

start, end = 1, max(arr)

while start <= end:
    mid = (start + end) // 2
    total = 0
    res = 0
    for i in arr:
        res = i - mid
        if res >= 0:
            total += res
        else:
            total +=i

    if total >=