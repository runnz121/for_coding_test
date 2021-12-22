a, b = map(int, input().split())
x = 1

def recurs(a):
    if a == 0:
        return 1
    if a == 1:
        return 1
    else:
        return a * recurs(a-1)

#nCr = n! / ((n-k)! * k!)
print(recurs(a) // (recurs(a-b) * recurs(b)))