def cal(a, b):
    sum = 0
    while a > 0:
        sum += a % b
        a = a // b
    return sum
for i in range(1000, 10000):
    f = cal(i, 10)
    s = cal(i, 12)
    t = cal(i, 16)
    if f == s and f == t:
        print(i)