n, m = map(int, input().split())

arr = []
for i in range(n):
    arr.append(list(map(str, input().split())))

cnt1 = 0
for k in range(n):
    for i in arr[k]:
        tmp1 = 0
        for j in range(1, m):
            if i[j-1] == '-' and i[j]:
                tmp1 += 1
                if tmp1 == m-1:
                    cnt1 += 1
            else:
                cnt1 += 1
                tmp1 = 0

print(cnt1)