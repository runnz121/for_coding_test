n, k = map(int, input().split())


def recur(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    else:
        return n * recur(n-1)
# 이항계수 공식 nCr = n! / ((n-k)! * k!)
print((recur(n) // (recur(n-k) * recur(k)))%10007)