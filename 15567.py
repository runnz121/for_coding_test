n = int(input())

for i in range(1, n):
    if n-1 == i + i**2:
        print(i)
        exit()

