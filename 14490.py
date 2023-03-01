s = list(map(int, input().split(':')))


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

big = max(s[0], s[1])
small = min(s[0], s[1])

res = gcd(big, small)

print(str(s[0]//res) + ':' + str(s[1]//res))