n = int(input())

cnt = 0

num = n%5

cnt = 0

if n == 1 or n==3:
    print(-1)
    exit(0)

elif num % 2 == 0:
    print(n//5 + num//2)
    exit(0)

else:
    print((n//5)-1 + (num + 5)//2)
