x = list(input())

res = ""
for i in range(len(x)):
    if i > 0 and (len(x) - i) % 3 == 0:
        res += ","
    res += x[i]

print(res)