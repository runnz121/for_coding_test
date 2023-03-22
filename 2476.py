n = int(input())


res = []
for i in range(n):
    a, b, c = map(int, input().split())

    if a == b == c:
        res.append(10000 + a * 1000)

    elif a == b or a == c or b == c:
        if a == b:
            res.append(1000 + b * 100)
        elif a == c:
            res.append(1000 + a * 100)
        elif b == c:
            res.append(1000 + b * 100)
    else:
        p = max(a, b, c)
        res.append(p * 100)

print(max(res))