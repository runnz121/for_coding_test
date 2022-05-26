t = 3

while t > 0:
    n = int(input())
    x = 0
    for k in range(n):
        x += int(input())
    if x == 0:
        print(0)
    elif x > 0:
        print('+')
    else:
        print('-')

    t -= 1