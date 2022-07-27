n, m = map(int, input().split())

arr = list(map(int, input().split()))

s = 0
e = 1

cnt = 0
nu = arr[s]
while e < n:

    if nu % m == 0:
        cnt += 1
        e += 1
        if e < n:
            nu += arr[e]
        else:
            break
    elif nu % m:
        nu -= arr[s]
        s += 1
    elif nu < m:
        e += 1
        if e < n:
            nu += arr[e]
        else:
            break
print(cnt)