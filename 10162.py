n = int(input())

arr = [300, 60, 10]

ans = []

i =  0
cnt = 0
while True:
    if n == 0 or n < 10:
        ans.append(cnt)
        break

    if n >= arr[i]:
        n -= arr[i]
        cnt += 1
    else:
        ans.append(cnt)
        cnt = 0
        i += 1

if n != 0:
    print(-1)
else:
    if len(ans) != 3:
        while len(ans) < 3:
            ans.append(0)
    print(*ans)