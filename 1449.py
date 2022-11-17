n, m = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()

start = arr[0]

cnt = 1

for loc in arr[1:]:
    if loc in range(start, start + m):
        continue
    else:
        start = loc
        cnt += 1

print(cnt)