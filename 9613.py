n = int(input())

def gcd(a, b):
    while b > 0:
        a, b = b, a%b
    return a

for i in range(n):
    tmp = list(map(int, input().split()))
    ans = 0

    cnt = tmp[0]
    test = tmp[1:]

    for i in range(1, cnt):
        for j in range(i + 1, cnt+1):
            ans += gcd(tmp[i], tmp[j])
    print(ans)