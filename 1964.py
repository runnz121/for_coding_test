n = int(input())

total = 0

for i in range(n,0,-1):
    total += i * 5 - (i * 2) + 1

print((total + 1)%45678)