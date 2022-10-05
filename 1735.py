a, b = map(int, input().split())
c, d = map(int, input().split())

def gcd(a,b):
    while a % b != 0:
        mod = a % b
        a = b
        b = mod
    return b

g = gcd(a*d + b*c, b * d)
print((a*d + b * c)//g, (b*d)//g)