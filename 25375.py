n = int(input())

while n > 0:
    a, b = map(int, input().split())


    def gcd(a, b):
        for i in range(min(a, b), 0, -1):
            if a % i == 0 and b % i == 0 and (a // i) + (b // i) == b:
                return 1
        return 0

    print(gcd(a, b))


    n -= 1
