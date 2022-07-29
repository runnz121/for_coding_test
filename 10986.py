n, m = map(int, input().split())

arr = list(map(int, input().split()))
#
# dp = [[0] * n for _ in range(n)]

cnt = 0
for i in range(1, n):
    arr[i] += arr[i-1]
    if arr[i] % m == 0:
        cnt += 1

i = 0
while True:

    for k in range(i, n):
        if (arr[k] - arr[i]) % m == 0 and (arr[k] - arr[i]) != 0:
            cnt += 1

    i += 1

    if i == n-1:
        break

print(cnt)

# 1 3 6 7 9
# 0 2 5 6 8
# 0 0 3 4 6
# 0 0 0 1 3
# 0 0 0 0 2
