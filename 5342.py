

while True:
    n = int(input())
    if n == 0:
        break
    res = 0
    for i in range(1, n + 1):
        res += i

    print(res)