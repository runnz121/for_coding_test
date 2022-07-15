n = int(input())

cnt = 0
for i in range(n+1):
    for k in str(i):
        if k in ['3', '6', '9']:
            cnt += 1

print(cnt)