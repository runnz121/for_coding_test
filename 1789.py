s = int(input())

sums = 0
i = 1
while True:
    sums += i
    if sums == s:
        print(i)
        break
    if sums > s:
        print(i-1)
        break
    i += 1