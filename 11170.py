n = int(input())

for i in range(n):
    x, y = map(int, input().split())
    tmp = 0
    for i in range(x, y+1):
        x = list(str(i))

        for k in x:
            if k == '0':
                tmp += 1
    print(tmp)