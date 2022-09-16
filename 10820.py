import sys

while True:
    small = 0
    capital = 0
    number = 0
    space = 0
    x = list(sys.stdin.readline().rstrip('\n'))
    if not x:
        break
    for i in range(len(x)):
        if 90 >= ord(x[i]) >= 65:
            capital += 1
        elif 122 >= ord(x[i]) >= 97:
            small += 1
        elif 57 >= ord(x[i]) >= 48:
            number += 1
        elif ord(x[i]) == 32:
            space += 1
    print(small, capital, number, space)
