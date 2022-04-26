a, b, c = map(int, input().split())

step = 0

while b != 1 or c != 1:
    if b == c:
        break

    if b % 2 == 0:
        b = b//2
    else:
        b = b//2 + 1

    if c % 2 == 0:
        c = c//2
    else:
        c = c//2 + 1
    step += 1

print(step)
