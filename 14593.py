n = int(input())

if n == 1:
    print(0)
    exit(0)
if n == 2:
    print(2)
    exit(0)
if n == 0:
    print(0)
    exit(0)
else:
    print(n * (n - 1))