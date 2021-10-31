x = int(input())

for i in range(1, x + 1):
    a = list(i)
    print(a)
    s = i + sum(a)
    if (s == x):
        result = i
        break
print(result)