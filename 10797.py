x = int(input())

arr = list(map(int, input().split()))


cnt = 0
for i in arr:
    if i == x:
        cnt += 1

print(cnt)