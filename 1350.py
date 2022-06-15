n = int(input())
arr = list(map(int, input().split()))
cluster = int(input())

cnt = 0
for i in arr:
    if i != 0:
        while i > 0:
            i -= cluster
            cnt += 1

print(cnt * cluster)

