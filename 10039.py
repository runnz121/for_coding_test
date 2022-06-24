sums = 0

for _ in range(5):
    x = int(input())

    if x < 40:
        sums += 40
    else:
        sums += x

print(sums//5)