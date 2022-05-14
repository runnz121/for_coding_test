a, b, c = map(int, input().split())

arr = []

for _ in range(a):
    i = int(input())
    if i <= b or i <= c or i <= ((b**2) + (c**2))**0.5:
        print("DA")
    else:
        print("NE")
