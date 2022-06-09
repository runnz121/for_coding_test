a, b = map(int, input().split())

cnt = 0
ans = ''


def found(n, cnt):

    global ans

    if n == b:
        ans += str(cnt)
        return

    if n > b:
        ans += str('')
        return

    double = n * 2
    stradd = str(n) + '1'
    add = int(stradd)
    found(n * 2, cnt + 1)
    found(add, cnt + 1)

found(a, 0)

if ans =='':
    print(-1)
else:
    print(int(ans)+1)