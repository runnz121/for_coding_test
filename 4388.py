while True:
    n, m = map(int, input().split())
    cnt = 0

    if n ==0 and m == 0:
        break

    a = list(str(n))
    b = list(str(m))

    if len(a) != len(b):
        if len(a) < len(b):
            while len(a) < len(b):
                a.insert(0,'0')
        else:
            while len(a) > len(b):
                b.insert(0, '0')

    carry = 0
    for i in range(len(a)-1, -1, -1):
        if int(a[i]) + int(b[i]) + carry >= 10:
            cnt += 1
            carry = 1
        else:
            carry = 0

    print(cnt)