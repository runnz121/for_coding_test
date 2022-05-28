n = int(input())

current = 1
for i in range(n):
    x, y = map(int, input().split())

    if x == current:
        current = y
    elif y == current:
        current = x

print(current)