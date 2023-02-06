n = int(input())
for i in range(n):
    x = list(map(str, input().split()))
    lens = len(x)
    res = ""
    for idx in x:
        idx = list(idx)
        tmp1 = idx[::-1]
        lens -= 1
        for word in tmp1:
            tmp  = ''
            tmp += word
            res += tmp
        if lens != 0:
            res += ' '
    print(res)