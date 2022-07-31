a, b, c = map(int, input().split())

r = [a^b, (a^b)^b]

print(r[0] if c%2 == 1 else r[1])