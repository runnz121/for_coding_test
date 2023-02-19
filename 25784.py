n = list(map(int, input().split()))

n.sort()

if n[0] + n[1] == n[2]:
    print(1)
    exit(0)

elif n[0] * n[1] == n[2]:
    print(2)
    exit(0)

print(3)