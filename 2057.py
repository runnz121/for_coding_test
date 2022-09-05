n = int(input())

start = 2432902008176640000

if n == 0:
    print("NO")
    exit()

for i in range(20, -1, -1):
    if i == 0:
        i = 1
    start /= i
    if n >= start:
        n -= start

if n == 0:
    print("YES")
else:
    print("NO")