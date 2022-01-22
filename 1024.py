
a, b = map(int, input().split())

#
# 이 식을 n = x+ (x+1) + (x+2) + ... + (x+ (l-1))

# 정리하면 아래처럼 된다
# n = (x * l) + (0 + 1 + 2 + ... l-1)
# n= x*l + S_(l-1)
# x = (n - S_(l-1)) / l
# x = (n - (l-1)l /2) /l
# (x == start)

for i in range(b, 101):
    start = a - (i*(i + 1) / 2)

    if start % i == 0:
        start = int(start / i)

        if start >= -1:
            for j in range(1, i + 1):
                print(start + j, end= ' ')
            print()
            break
else:
    print(-1)
