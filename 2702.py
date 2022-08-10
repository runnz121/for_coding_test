n = int(input())

while n > 0:
    a, b = map(int, input().split())

    maxx = -int(1e9)
    mins = int(1e9)

    #최대공약수
    for i in range(1, max(a, b)+1):
        if a%i ==0 and b%i == 0:
            maxx = max(i, maxx)

    mins = (a//maxx) * (b//maxx) * maxx

    print(mins, maxx)


    n -= 1