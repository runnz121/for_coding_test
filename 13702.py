import sys

n, k = map(int, input().split())

arr = []

for i in range(n):
    arr.append(int(sys.stdin.readline()))

arr.sort()

start = 0
end = max(arr)

ans = 0
while start <= end:
    mid = (start + end) // 2

    cnt = 0
    tmp = 0
    for i in arr:
        tmp = i // mid
        cnt += tmp

    if cnt >= k:
        start = mid + 1
        ans = mid
    else:
        end = mid -1
print(ans)


