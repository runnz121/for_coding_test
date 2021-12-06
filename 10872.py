n = int(input())

def recurs(n):
    res = 1
    if n > 0:
        res = n * recurs(n-1)
    return res
print(recurs(n))