n, k = map(int, input().split())

def sol(n, k):
    rev = ''

    while n > 0:
        n, mod = divmod(n, k)
        rev += str(mod)

    return rev[::-1]

x = sol(n,k)

x = str(x).split('0')

p = 0
for i in x:
    if i != '':
        p += int(i)

p = sol(p, k)

print(p)