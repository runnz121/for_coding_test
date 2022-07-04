n = int(input())

arr = [500, 100, 50, 10, 5, 1]

n = 1000 - n

cnt = 0
for i in arr:
    while n > 0:
        if n >= i:
            n -= i
            cnt += 1
        else:
            break
print(cnt)